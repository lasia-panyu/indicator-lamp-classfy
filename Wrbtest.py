# -*- coding: utf-8 -*-
2 """
3 Created on Fri Jan 3 21:06:22 2014
4
5 @author: duan
6 """

import numpy as np
import cv2
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello Flask!'
if __name__ == '__main__':
    app.run(debug=True)  