import os

import cv2

from model import CoffeeCupDetector
from config import RESULT_FOLDER

detector = CoffeeCupDetector()


def process_image(input_path: str):

    image = cv2.imread(input_path)

    results = detector.predict(image)

    result = results[0]

    output = result.plot()

    filename = os.path.basename(input_path)

    output_path = os.path.join(
        RESULT_FOLDER,
        filename
    )

    cv2.imwrite(output_path, output)

    count = 0

    for cls in result.boxes.cls:

        class_name = result.names[int(cls)]

        if class_name == "cup":
            count += 1

    return {
        "result_path": output_path,
        "defect_count": count,
        "defect_area": 0,
        "processing_time": 0
    }