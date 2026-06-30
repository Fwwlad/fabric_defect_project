from ultralytics import YOLO


class CoffeeCupDetector:

    def __init__(self):
        self.model = YOLO("yolov8n.pt")

    def predict(self, image):
        return self.model(image)