# python-GetsScreenPixelColor
为色盲患者提供，识别屏幕中不同的颜色。

# 目标：
    原意为色盲患者识别屏幕的颜色，识别折线图中不同的折线颜色。
# 原理：
    通过键盘输入按键（默认空格键）获取当前鼠标的像素值，显示在屏幕上，同时显示像素的颜色名称，方便找到一样颜色的折线。
# 使用方式：
    1.python GetPixel.py
    2.跳转到要识别的页面，点击选中程序框
    3.鼠标移动到要识别的颜色上
    4.按下空格键显示RGB颜色(选中程序框之后可多次识别)
    5.退出程序
# 参数：
    key:设定的键盘按键
    show_position:显示RGB颜色的位置

# 需要：
    安装tkinter, macOS建议使用python3.7.0，自带tkinter6.8，同时运行tkinker系统不会崩溃。
    pip install pillow
    pip install PyUserInput
    pip install webcolors
