# -*- coding: utf-8 -*
import cv2
import numpy as np

img = cv2.imread("C:\\Users\\Administrator\\Desktop\\2.jpg", cv2.IMREAD_COLOR)

img2 = cv2.imread("C:\\Users\\Administrator\\Desktop\\3.jpg", cv2.IMREAD_COLOR)

img3 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img4 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img5 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)


def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(str(x) + ":" + str(y))
        # print(img4[x, y])
        cv2.circle(img, (x, y), 500, (255, 0, 0), 1)


def nothing(x):
    pass


#
# cv2.imread() cv2.imwrite()读入读出
# cv2.IMREAD_COLOR读入格式

# cv2.WINDOW_NORMA窗口格式


# cv2.line(img,(0,0),(1500,1500),(255.0,0),5,cv2.LINE_AA)
# cv2.rectangle(img,(100,100),(1500,1500),(0,255,0),5,cv2.LINE_AA)
# cv2.circle(img,(1500,1500),500,(0,0,255),1)
# cv2.ellipse(img,(1500,1500),(250,300),0,0,360,255,cv2.LINE_AA)
# cv2.putText(img,'OG! TI9 CHANPIONS',(500,500),cv2.LINE_AA,4,(255,255,255),cv2.LINE_AA)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# 鼠标事件
cv2.setMouseCallback('image', draw_circle)
# cv2.createTrackbar('R', 'image', 0, 255, nothing)
# cv2.createTrackbar('B', 'image', 0, 255, nothing)
# cv2.createTrackbar('G', 'image', 0, 255, nothing)

switch = '0:OFF\n1:ON'
# cv2.createTrackbar(switch, 'image', 0, 1, nothing)

# ball = img[280:340, 330:390]
# img[273:333, 100:160] = ball
# rbg=img[:,:,0|1|2]

print(img2.shape)

lower_light = np.array([1, 1, 1])
up_light = np.array([255, 255, 255])

pts1 = np.float32([[0, 0], [3000, 0], [510, 3625], [2095, 3646]])
pts2 = np.float32([[0, 0], [3000, 0], [0, 4000], [3000, 4000]])

M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img2, M, (3000, 4000))

while 1:
    # cv2.imshow("image", cv2.add(img, img2))
    # cv2.imshow("image", cv2.addWeighted(img, 0.8, img2, 0.2,0))
    img = cv2.medianBlur(img, 5)
    img[0:3000, 620:110] = [0, 0, 0]
    img[0:3000, 620:1550] = [0, 0, 0]
    ret, mask = cv2.threshold(img3, 100, 255, cv2.THRESH_BINARY)
    th2 = cv2.adaptiveThreshold(img3, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    th3 = cv2.adaptiveThreshold(img3, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    # cv2.imshow("image", ret)

    mask_inv = cv2.bitwise_not(mask)

    th3 = cv2.bitwise_not(th3)
    # cv2.imshow("image", mask_inv)
    # print(img.shape)
    img = cv2.bitwise_and(img, img, mask=mask)

    img4 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask1 = cv2.inRange(img4, lower_light, up_light)
    # cv2.imshow("image", img4[0:2000, 0:1500])
    # cv2.imshow("image", cv2.bitwise_and(img, img, mask=mask1)[0:2000, 0:1500])

    # cv2.imshow("image", dst)
    blur = cv2.GaussianBlur(img5, (5, 5), 0)
    blur = cv2.bilateralFilter(img5, 9, 75, 75)
    ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    kernel = np.ones((5, 5), np.uint8)
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    imgCanny = cv2.Canny(img4, 4000, 300)

    imgg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgg, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # print (contours[0])
    imag = cv2.drawContours(img, contours, -1, (255, 255, 255), cv2.FILLED)
    img = cv2.imread("C:\\Users\\Administrator\\Desktop\\2.jpg", cv2.IMREAD_COLOR)
    i = 0
    for x in contours:
        i = i + 1
        M = cv2.moments(x)
        if M['m10'] == 0 or M['m10'] == 0:
            # print(np.mean((x[:, :, 0])))
            # print (cv2.moments(x))
            cv2.circle(img, (int(np.mean((x[:, :, 0]))), int(np.mean((x[:, :, 1])))), 100, (0, 0, 255), 1)
            continue
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])
        cv2.circle(img, (cx, cy), 100, (0, 0, 255), 1)
    # cv2.putText(img, str(i), (cx, cy), cv2.LINE_AA, 4, (255, 255, 255), 2)

    cv2.imshow("image", img4)
    # k = cv2.waitKey(0)
    if cv2.waitKey(10000000) == 27:
        break
    # r = cv2.getTrackbarPqos('R', 'image')
# print(r)
cv2.destroyAllWindows()
