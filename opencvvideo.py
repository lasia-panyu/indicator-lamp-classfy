# -*- coding: utf-8 -*
import cv2
import img as img
import numpy as np
import Common as cn
import pymysql
import time
from navive import  navice


def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(str(x) + ":" + str(y))
        img[0:50, 0:50] = img[y, x]
        print(img[y, x])
    # print(img[x, y])
    # print(img4[x, y])
    # cv2.circle(img, (x, y), 500, (255, 0, 0), 1)


def valueP(x, y, z, x1, y1, z1):
    if abs(x - x1) <= 20 and abs(y - y1) <= 20 and abs(z - z1) <= 20:
        return "ojbk"

    else:
        return "sb"


img1 = cv2.imread("C:\\Users\\Administrator\\Desktop\\1234.png", cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
img = img1
# cap = cv2.VideoCapture(1)

# -1.0
#

conn = pymysql.connect(
    host='localhost',
    user='root', password='123456',
    database='lasia',
    charset='utf8')
cursor = conn.cursor()

sql = "select * from jflight where position1 = 1 "
res = cursor.execute(sql)
result = cursor.fetchall()
for row in result:
    id = row[0]
    value = str(row[1])
    # print(value)
    # print(value.split(" "))
    y = row[2]
    x = row[3]
    desc = ''
    print(img[x, y])
    if valueP(img[x, y][0], img[x, y][1], img[x, y][2], int(value.split(" ")[0]), int(value.split(" ")[1]),
              int(value.split(" ")[2])) == "ojbk":
        print("ojbk")
        desc = 'ojbk'
    else:
        print("sb")
        desc = 'sb'
    print("update jflight set date = \"%s\",desc=\"%s\" where id=%d" % (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), desc, id))
    cursor.execute("update jflight set jflight.date = \"%s\",jflight.desc=\"%s\" where id=%d" % (
        time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), desc, id))
    conn.commit()
    print(row)
    max
    # print(value)
# print(res)
# img = np.zeros([359, 518, 3])

# img[0:359, 0:259] = img1[0:359, 0:259]


# img = cv2.resize(img, (518, 1077), cv2.INTER_CUBIC)


cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

# lower_blue = np.array([40, 40, 40])
# upper_blue = np.array([120, 180, 70])

# print(img[174:194, 44:64])
# for x in range(20):
#    print(img[174 + x, 44 + x])

while True:

    # ret, frame = cap.read()
    frame = img1
    cn.gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cn.hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # light_mask = cv2.inRange(img1, lower_blue, upper_blue)
    # res = cv2.bitwise_and(frame, frame, mask=light_mask)

    # ret, thresh1 = cv2.threshold(cn.gray, 40, 255, cv2.THRESH_BINARY)
    # img = cv2.bitwise_and(img1, img1, mask=
    # x = img[174:194, 44:64]
    # img=cv2.resize(img, (1000, 1500), cv2.INTER_CUBIC)
    # cv2.imshow('image', dimg)
    # img[:, :, :] = [0, 0, 0]
    # img[174:194, 44:64] = x
    cv2.imshow('image', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# cap.release()
cv2.destroyAllWindows()
