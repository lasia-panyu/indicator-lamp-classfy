# -*- coding: utf-8 -*
import cv2
import numpy as np
import matplotlib

_as1.as_ctypes()
img = cv2.imread("C:\\Users\\Administrator\\Desktop\\2.jpg", cv2.IMREAD_COLOR)

img2 = cv2.imread("C:\\Users\\Administrator\\Desktop\\3.jpg", cv2.IMREAD_COLOR)

img1 = cv2.imread("C:\\Users\\Administrator\\Desktop\\2.jpg", cv2.IMREAD_COLOR)


def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(str(x) + ":" + str(y))
        # print(img4[x, y])
        # cv2.circle(img, (x, y), 500, (255, 0, 0), 1)


imgori = cv2.imread("C:\\Users\\Administrator\\Desktop\\2.jpg", cv2.IMREAD_COLOR)
img[620:1150, 0:3000] = [0, 0, 0]
img[1600:2700, 0:800] = [0, 0, 0]
img[300:450, 400:550] = [0, 0, 0]
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY)

img = cv2.bitwise_and(img, img, mask=mask)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 127, 255, 0)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# imag = cv2.drawContours(img, contours, -1, (255, 255, 255), cv2.FILLED)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.setMouseCallback('image', draw_circle)
while 1:
    i = 9
    for x in contours:
        i = i + 1
        M = cv2.moments(x)
        if M['m10'] == 0 or M['m10'] == 0:
            # print(np.mean((x[:, :, 0])))
            # print (cv2.moments(x))
            cv2.circle(img1, (int(np.mean((x[:, :, 0]))), int(np.mean((x[:, :, 1])))), 100, (0, 0, 255), 1)
            continue
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        cv2.circle(img1, (cx, cy), 100, (0, 0, 255), 1)
    cv2.imshow("image", img1)
    if cv2.waitKey(10000000) == 27:
        cv2.destroyAllWindows()
