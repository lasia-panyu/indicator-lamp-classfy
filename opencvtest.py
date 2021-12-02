# -*- coding: utf-8 -*
import numpy as np
import cv2
import os
import sys
from matplotlib import pyplot as plt

#def draw_circle(event,x,y,flags,param):
#    if event == cv2.EVENT_LBUTTONDBLCLK:
#        cv2.circle(img.(x,.y),100,(255,0,0),-1)

img = cv2.imread("C:\\Users\\Administrator\\Desktop\\2.png",cv2.IMREAD_GRAYSCALE)
#hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
#print (hist)
#plt.hist(img.ravel(),256,[0,256])
#plt.show()

"""
img.revel(） 转为数组
calhist 计算直方图 img：图像 [0]：通道值灰度单值 rbg hsv个  None:范围 [256]:直方图x轴个数 [0, 256]:范围
np.bincount numpy 计算直方图
cv2.equalizeHist 灰度均值化
createCLAHE 对比度受限的自适应直方图均衡化
"""
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
hist = np.bincount(img.ravel(), minlength=256)
plt.hist(img.ravel(), 256, [0, 256])

#plt.show()




clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
cl1 = clahe.apply(img)
md1=cv2.medianBlur(img,1)
md2=cv2.medianBlur(img,7)
equ = cv2.equalizeHist(img)
md1 = cv2.equalizeHist(md1)
#cv2.imshow('equalization', np.hstack((img, equ,md1,md2)))  # 并排显示
img = cv2.imread("C:\\Users\\Administrator\\Desktop\\2.png",cv2.IMREAD_GRAYSCALE)
ret,mask=cv2.threshold(img,175,255,cv2.THRESH_BINARY)
maskf=cv2.bitwise_not(mask)
img = cv2.imread("C:\\Users\\Administrator\\Desktop\\2.png",cv2.IMREAD_COLOR)
x1=cv2.bitwise_and(img,img,mask=mask)
#cv2.imshow("img",x1)
image, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
img = cv2.imread("C:\\Users\\Administrator\\Desktop\\2.png",cv2.IMREAD_COLOR)
image=cv2.drawContours(img, contours, -1, (0, 255, 255), 1)
#plt.hist(x1.ravel(),256,[0,256]);
#plt.show()
cv2.imshow("1212",image)
cv2.waitKey(0)
#gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
#image, contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#image=cv2.drawContours(img, contours, -1, (0, 255, 255), 1)

#print (img.ravel())
#cv2.imshow("img", hsv)

#cv2.waitKey(0)
#hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#lower_b=np.array([0 , 0 , 100])
#high_b=np.array([50 , 50 , 150])
##mask=cv2.inRange(hsv,lower_b,high_b)
#res=cv2.bitwise_and(img,img,mask=mask)
#cv2.namedWindow("mask",cv2.WINDOW_NORMAL)
#cv2.imshow("img",img)
#cv2.imshow("mask",mask)
#cv2.imshow("res",es)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#cv2.namedWindow("image",cv2.WINDOW_NORMAL)
#cv2.line(img,(0,0),(511,511),(255,0,0),5)
#cv2.rectangle(img,(0,0),(511,511),(0,255,0),5)
#cv2.circle(img,(500,500),100,(0,0,255),-1)
#cv2.putText(img,'opencv',(500,500),cv2.FONT_HERSHEY_SIMPLEX,4,(255,255,255),2)
#cv2.imshow("image",img)

#k=cv2.waitKey(0)
#if k==27:
#  cv2.destroyAllWindows()
#elif k == ord('s'):
#  cv2.imwrite("C:\\Users\\Administrator\\Desktop\\11.jpg",img)
#  cv2.destroyAllWindows()

#cv2.imwrite()

#cap = cv2.VideoCapture(0)

#while(True):
#    ret,frame=cap.read()
#    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#    cv2.imshow("frame",gray)
#    if cv2.waitKey(1) == ord('q'):
#        break
#cap.retrieve()
#cv2.destroyAllWindows()