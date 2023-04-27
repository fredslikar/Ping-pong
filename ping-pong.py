import random
import turtle
from turtle import Turtle

border: Turtle = turtle.Turtle()
border.speed(0)
window = turtle.Screen()
border.hideturtle()
window.tracer(10)

window.title('Ping-pong')
window.setup(width=1.0, height=1.0)
window.bgcolor('black')

border.color('green')
border.begin_fill()
border.goto(-500, 300)
border.goto(500, 300)
border.goto(500, -300)
border.goto(-500, -300)
border.goto(-500, 300)
border.end_fill()

border.goto(0, 300)
border.setheading(270)
border.color('white')
for i in range(75):
    if i % 2 == 0:
        border.forward(8)
    else:
        border.up()
        border.forward(8)
        border.down()

rocket_l = turtle.Turtle()
rocket_l.color('white')
rocket_l.shape('square')
rocket_l.shapesize(stretch_len=1, stretch_wid=5)
rocket_l.penup()
rocket_l.goto(-450, 0)

rocket_r = turtle.Turtle()
rocket_r.color('white')
rocket_r.shape('square')
rocket_r.shapesize(stretch_len=1, stretch_wid=5)
rocket_r.penup()
rocket_r.goto(450, 0)

speed_rockets = 10


def move_up_l():
    y = rocket_l.ycor() + speed_rockets
    if y > 250:
        y = 250
    rocket_l.sety(y)


def move_down_l():
    y = rocket_l.ycor() - speed_rockets
    if y < -250:
        y = -250
    rocket_l.sety(y)


def move_up_r():
    y = rocket_r.ycor() + speed_rockets
    if y > 250:
        y = 250
    rocket_r.sety(y)


def move_down_r():
    y = rocket_r.ycor() - speed_rockets
    if y < -250:
        y = -250
    rocket_r.sety(y)


FONT = ('Arial', 44)
score_l = 0
tablo_l = turtle.Turtle()
tablo_l.color('white')
tablo_l.penup()
tablo_l.hideturtle()
tablo_l.setpos(-250, 305)
tablo_l.write(score_l, font=FONT)

score_r = 0
tablo_r = turtle.Turtle()
tablo_r.color('white')
tablo_r.penup()
tablo_r.hideturtle()
tablo_r.setpos(250, 305)
tablo_r.write(score_l, font=FONT)

ball: Turtle = turtle.Turtle()
ball.shape('circle')
ball.color('white')
ball.penup()
ball.speed_x = 3
ball.speed_y = 3
ball.speed(10)
ball.setpos(0, random.randint(-150, 150))

window.listen()
window.onkeypress(move_up_l, 'w')
window.onkeypress(move_down_l, 's')
window.onkeypress(move_up_r, 'Up')
window.onkeypress(move_down_r, 'Down')

while True:
    window.update()
    change_speed = random.randint(-2, 2)
    change_pos = random.randint(-150, 150)
    ball.setx(ball.xcor() + ball.speed_x)
    ball.sety(ball.ycor() + ball.speed_y)

    if ball.xcor() > 490:
        score_l = score_l + 1
        tablo_l.clear()
        tablo_l.write(score_l, font=FONT)
        ball.speed_x = -ball.speed_x + change_speed
        ball.speed_y = -ball.speed_y + change_speed
        ball.setpos(0, change_pos)
        if ball.speed_x == 0:
            ball.speed_x = ball.speed_x + change_speed
        if ball.speed_y == 0:
            ball.speed_y = ball.speed_y + change_speed

    if ball.xcor() < -490:
        score_r = score_r + 1
        tablo_r.clear()
        tablo_r.write(score_r, font=FONT)
        ball.speed_x = -ball.speed_x + change_speed
        ball.speed_y = -ball.speed_y + change_speed
        ball.setpos(0, change_pos)
        if ball.speed_x == 0:
            ball.speed_x = ball.speed_x + change_speed
        if ball.speed_y == 0:
            ball.speed_y = ball.speed_y + change_speed

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.speed_y = -ball.speed_y

    if rocket_r.xcor() + 5 > ball.xcor() > rocket_r.xcor() - 15 and rocket_r.ycor() - 50 < ball.ycor() < rocket_r.ycor() + 50:
        ball.speed_x = - ball.speed_x

    if rocket_l.xcor() - 5 < ball.xcor() < rocket_l.xcor() + 15 and rocket_l.ycor() - 50 < ball.ycor() < rocket_l.ycor() + 50:
        ball.speed_x = - ball.speed_x

    if ball.speed_x < - 5:
        ball.speed_x = - 5

    if ball.speed_x > 5:
        ball.speed_x = 5

    if ball.speed_y < - 5:
        ball.speed_y = - 5

    if ball.speed_y > 5:
        ball.speed_y = 5

    print(ball.speed_x)
    print(ball.speed_y)
    print('00000000')

window.mainloop()
