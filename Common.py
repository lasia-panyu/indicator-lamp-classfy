# -*- coding: utf-8 -*
import cv2
import Common as cn
import numpy as np
from

cap = cv2.VideoCapture(1)
# -1.0
cap.set(cv2.CAP_PROP_DC1394_MODE_MANUAL, 0.25)
cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)
cap.set(cv2.CAP_PROP_ISO_SPEED, 0.25)
cap.set(cv2.CAP_PROP_ISO_SPEED, 30)
fps1 = cap.get(cv2.CAP_PROP_AUTO_EXPOSURE)
fps = cap.get(cv2.CAP_PROP_ISO_SPEED)

hsv = []
gray = []
