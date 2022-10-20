from typing import TypeVar
import cv2 as cv


class BaseImageDetector(object):
    def __init__(self):
        pass

    def detectImage(self, imageToDetect: cv.Mat) -> tuple(float, float):
        return (-1, -1)
