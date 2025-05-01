import turtle

print("-50에서 50 범위 사각형의 꼭지점 좌표를 입력하시오.")

x1 = int(input("첫 번째 사각형의 좌측 상단 x좌표: "))
y1 = int(input("첫 번째 사각형의 좌측 상단 y좌표: "))
x2 = int(input("첫 번째 사각형의 우측 하단 x좌표: "))
y2 = int(input("첫 번째 사각형의 우측 하단 y좌표: "))

x3 = int(input("두 번째 사각형의 좌측 상단 x좌표: "))
y3 = int(input("두 번째 사각형의 좌측 상단 y좌표: "))
x4 = int(input("두 번째 사각형의 우측 하단 x좌표: "))
y4 = int(input("두 번째 사각형의 우측 하단 y좌표: "))

def is_overlap(x1, y1, x2, y2, x3, y3, x4, y4):
    return not (x2 <= x3 or x4 <= x1 or y2 >= y3 or y4 >= y1)

def draw_rect(x1, y1, x2, y2, color):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.color(color)
    turtle.goto(x2, y1)
    turtle.goto(x2, y2)
    turtle.goto(x1, y2)
    turtle.goto(x1, y1)

draw_rect(x1, y1, x2, y2, 'blue')
draw_rect(x3, y3, x4, y4, 'red')

if is_overlap(x1, y1, x2, y2, x3, y3, x4, y4):
    print("사각형이 겹칩니다")
else:
    print("사각형이 겹치지 않습니다")

turtle.done()
