#사인그래프 그리기
import turtle
import math

swidth,sheight=800,400
turtle.shape('turtle')
turtle.setup(width=swidth+5,height=sheight+5)
turtle.screensize(swidth,sheight)

scale_x=1
scale_y=100

turtle.penup()

for x in range(-360,361):
    screen_x=x*scale_x
    radian=x*(math.pi/180)
    screen_y=math.sin(radian)*scale_y
    turtle.goto(screen_x,screen_y)
    turtle.pendown()