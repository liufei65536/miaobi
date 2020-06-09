import cv2 as cv
import numpy as np

def mathch_center(tpl,target):
    th,tw = tpl.shape[:2] #获取模板图像的高宽
    result = cv.matchTemplate(target, tpl, cv.TM_CCOEFF_NORMED)  # result是我们各种算法下匹配后的图像
    threshold = 0.9    #阈值，1表示完全匹配
    loc = np.where(result>=threshold)
    #返回所有匹配图像的中心点
    for pt in zip(*loc[::-1]):  # *号表示可选参数
        br = (pt[0] + tw, pt[1] + th)  # 右下点
        center = (int)((pt[0] + br[0]) / 2), (int)((pt[1] + br[1]) / 2)
        yield  center