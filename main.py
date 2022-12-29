from turtle import Screen
import turtle as t
import random

color_list = [(101, 190, 171), (100, 164, 209), (207, 137, 182), (213, 230, 240), (56, 179, 154)]
t.colormode(255)
flork = t.Turtle()
flork.pensize(20)
flork.speed(10)
# flork.hideturtle()


# def kordinat_ayarlama():
#     flork.penup()
#     flork.right(180)
#     flork.forward(280)
#     flork.left(90)
#     flork.forward(200)
#     flork.left(90)
#     flork.pendown()

flork.penup()
flork.setheading(225)
flork.forward(350)
flork.setheading(0)
flork.pendown()


def hıza_almak():
    flork.penup()
    flork.right(180)
    flork.forward(509)
    flork.right(90)
    flork.forward(50)
    flork.right(90)
    flork.pendown()


# kordinat_ayarlama()

flork.color(random.choice(color_list))
for _ in range(10):
    for _ in range(10):
        flork.color(random.choice(color_list))
        # flork.dot(20, "black") -Bunlada yapabilirsin
        flork.forward(1)
        flork.penup()
        flork.forward(49)
        flork.pendown()
        flork.forward(1)
        flork.penup()
    hıza_almak()

screen = Screen()
screen.exitonclick()