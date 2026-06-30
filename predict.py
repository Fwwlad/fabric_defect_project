import os
import time

import cv2

from model import CoffeeCupDetector
from config import RESULT_FOLDER

detector = CoffeeCupDetector()


def process_image(input_path: str):
    start_time = time.time()

    image = cv2.imread(input_path)

    results = detector.predict(image)

    result = results[0]

    image_with_boxes = image.copy()

    cup_count = 0

    for box, cls in zip(result.boxes.xyxy, result.boxes.cls):

        class_name = result.names[int(cls)]

        if class_name != "cup":
            continue

        cup_count += 1

        x1, y1, x2, y2 = map(int, box)

        cv2.rectangle(
            image_with_boxes,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        cv2.putText(
            image_with_boxes,
            "Cup",
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

    processing_time = round(time.time() - start_time, 3)

    filename = os.path.basename(input_path)

    output_path = os.path.join(
        RESULT_FOLDER,
        filename
    )

    cv2.imwrite(output_path, image_with_boxes)
    
    return {
        "result_path": output_path,
        "cup_count": cup_count,
        "processing_time": processing_time
    }