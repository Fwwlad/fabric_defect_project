import cv2
import shutil
import os

from config import RESULT_FOLDER


def process_image(input_path: str):

    filename = os.path.basename(input_path)

    output_path = os.path.join(
        RESULT_FOLDER,
        filename
    )

    shutil.copy(input_path, output_path)

    return {
        "result_path": output_path,
        "defect_count": 0,
        "defect_area": 0.0,
        "processing_time": 0.0
    }