# -*- coding: utf-8 -*-
2 """
3 Created on Fri Jan 3 21:06:22 2014
4
5 @author: duan
6 """

import numpy as np
import cv2
from flask import Flask
cap = cv2.VideoCapture(0)

while(True):

  ret, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  cv2.imshow('frame',ret)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

# When everything done, release the capture
# cap.release()
cv2.destroyAllWindows()
app = Flask(__name__)


