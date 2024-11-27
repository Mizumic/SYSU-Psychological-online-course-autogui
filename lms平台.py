import pyautogui
import time
#将路径改为相对路径
pyautogui.click(2381, 27)  # 鼠标点击(2381,27)坐标位置，（将pycharm最小化）


def click_image(image_path, confidence=0.6):
    try:
        # 尝试在屏幕上定位指定的图像
        image_location = pyautogui.locateOnScreen(image_path, confidence=confidence)
        # 如果找到了图像位置
        if image_location:
            # 点击图像所在位置
            pyautogui.click(image_location)
            return True
        else:
            # 如果未找到图像，则返回 False
            return False
    except pyautogui.ImageNotFoundException:
        # 如果图像未找到，则捕获 ImageNotFoundException 异常并返回 False
        return False


def click_image_left(image_path, offset=1800, confidence=0.6):
    try:
        # 尝试在屏幕上定位指定的图像
        image_location = pyautogui.locateOnScreen(image_path, confidence=confidence)
        # 如果找到了图像位置
        if image_location:
            # 计算图像左侧的位置
            left_x = image_location.left - offset
            center_y = image_location.top + image_location.height // 2
            # 点击图像左侧的位置
            pyautogui.click(left_x, center_y)
            return True
        else:
            # 如果未找到图像，则返回 False
            return False
    except pyautogui.ImageNotFoundException:
        # 如果图像未找到，则捕获 ImageNotFoundException 异常并返回 False
        return False


def If_Exist(image_path, confidence=0.8):
    """
    检查屏幕上是否存在指定的图像。
    :param image_path: 图像文件的路径
    :param confidence: 识别的置信度阈值，默认为0.8
    :return: 如果图像存在则返回True，否则返回False
    """
    # 使用pyautogui.locateOnScreen方法查找图像
    try:
        location = pyautogui.locateOnScreen(image_path, confidence=confidence)
        if location:
            return True
        else:
            return False
    except pyautogui.ImageNotFoundException:
        # 如果图像未找到，则捕获 ImageNotFoundException 异常并返回 False
        return False


time.sleep(0.5)  # 进行1秒的延时
while True:
    time.sleep(2)
    if not click_image(".\\image\\end1.png"):
        pyautogui.scroll(-1000000)  # 只要没有见到页面底部就不断往下翻
    if not click_image(".\\image\\end2.png"):
        pyautogui.scroll(-1000000)  # 只要没有见到页面底部就不断往下翻
    elif If_Exist(".\\image\\Finished.png"):  # 识别到任务点已完成的图片
        time.sleep(0.5)
        # 进行1秒的延时

        pyautogui.scroll(-1000)  # 鼠标向下滚动1000个单位
        pyautogui.click(x=2053, y=1302, clicks=1, button='left')  # 点击下一步
    elif click_image(".\\image\\stop.png"):  # 中途视频意外暂停时对播放按钮进行点击
        pyautogui.scroll(-1000)  # 鼠标向下滚动1000个单位
    elif click_image(".\\image\\tl.png"):
        while not click_image(".\\image\\end2.png"):
            pyautogui.scroll(-100000)  # 如果进入讨论，就一直往下翻，直到拖到底部。
            if click_image(".\\image\\yy.png"):
                pyautogui.click(x=1913, y=1290, clicks=1, button='left')  # 点击下一步
    else:
        continue