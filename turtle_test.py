import turtle
# from turtle import *


# 绘制一个蟒蛇
def draw_snake(radius, angle, length):
    # 设置画笔朝向，顺时针转40度
    turtle.seth(-40)
    for i in range(length):
        # 以radius为半径，画出angle角度的圆弧，逆时针
        turtle.circle(radius, angle)
        turtle.circle(-radius, angle)
    turtle.circle(radius, angle/2)
    # 根据画笔方向向前移动40像素
    turtle.fd(40)
    turtle.circle(16, 180)
    turtle.fd(40*2/3)


# 启动图形窗口
turtle.setup(650, 350, 400, 200)
# 抬起画笔,之后的移动不绘制图形
turtle.penup()
# 移动画笔的反方向移动
turtle.fd(-250)
# 放下画笔，之后的移动会绘制图形
turtle.pendown()
# 设置画笔大小，50像素
turtle.pensize(20)
# 设置画笔颜色
turtle.pencolor("purple")
draw_snake(40, 80, 4)
# 隐藏画笔
turtle.hideturtle()
# 绘制结束
turtle.done()
