import os
import time

from PIL import Image
from miaobi import screencap
from match_tools import mathch_center
import cv2 as cv

if __name__ == '__main__':
    #screencap()
    target = cv.imread('screen.png')
    tpl = cv.imread('lingmiaobi.png')
    centers = mathch_center(tpl, target)
    center = next(centers)
    print(center)

    cv.imshow("input image", target)  # 通过名字将图像和窗口联系
    cv.waitKey(0)

    #execute_cmd('adb shell input tap {} {}'.format(center[0], center[1]))

