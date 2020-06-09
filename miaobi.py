#需要配置好adb。
#运行前打开淘宝，进入领喵币活动页面。
#2020/6/3 解决了因为有些页面加载慢，等待时间结束后任务没有完成的问题。方法是增加一次滑动
#目前只能浏览店铺，后面的淘宝农场之类的没有处理。建议使用前先手动完成农场任务。
import os
import time
import  cv2 as cv
from PIL import Image
from match_tools import mathch_center


MAX_TIMES = 50  # 自定义最大浏览次数

#用来执行命令，这里加了延迟
def execute_cmd(args):
    DELAY_SECOND = 2#延迟时间， 因为网络和手机响应速度不同，反应慢的可以改大一些。
    time.sleep(DELAY_SECOND) #等待上一步操作响应完成
    os.system(args)
    #print('执行{}'.format(args))#test


#截图保存到手机上， 上传到电脑上
def screencap():
    execute_cmd('adb shell screencap -p /sdcard/screen.png')
    execute_cmd('adb pull /sdcard/screen.png')



# 进入领喵币中心
def enter_miaobi_center():
    # 截图
    screencap()
    target = cv.imread('screen.png')
    tpl = cv.imread('lingmiaobi.png')
    centers = mathch_center(tpl,target)
    pos = next(centers)
    execute_cmd('adb shell input tap {} {}'.format(pos[0], pos[1]))

# 浏览店铺
def browse_stores():
    BROWSER_WAIT = 16  #浏览等待15秒
    COUNT = 0  # 计数
    for i in range(0, MAX_TIMES):
        screencap()
        target = cv.imread('screen.png')
        tpl = cv.imread('quliulan.png')
        centers = mathch_center(tpl, target)
        pos = next(centers)
        print(pos)#调试用
        # 点击去浏览
        execute_cmd('adb shell input tap {} {}'.format(pos[0], pos[1]))
        # 下滑浏览,防止第一次没滑动成功，滑动两次
        execute_cmd('adb shell input swipe 900 1500 900 500 200')
        execute_cmd('adb shell input swipe 900 1500 900 500 200')
        COUNT = COUNT+1
        print('进入第{}个店铺,浏览页面中，请等待{}s...'.format(COUNT,BROWSER_WAIT))
        time.sleep(BROWSER_WAIT)
        # 返回
        execute_cmd('adb shell input keyevent 4')
    print('END')

if __name__ == '__main__':

    print('开始时间：'+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) )
    try:
       enter_miaobi_center()
    except:
        print("进入喵币中心失败，可能已经进入领喵币中心，尝试进入浏览页面...")

    try:
        browse_stores()
    except:
        print('浏览失败')

    print('结束时间：'+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())) )


