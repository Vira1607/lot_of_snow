import random
from turtle import *

shape("turtle")
speed(10)
# pencolor("white")
pensize(6)

Screen().bgcolor("turquoise")
colours = ["#ccff99", "#ccffcc", "#99ffcc", "#ffffcc", "#ffcccc", "#ccccff", "#cc99ff", "#ffccff"]


def vshape(size):
    right(25)
    forward(size)
    backward(size)
    left(50)
    forward(size)
    backward(size)
    right(25)


def snowflakeArm(size):
    for x in range(0, 4):
        forward(size)
        vshape(size)
    backward(size * 4)


def snowflake(size):
    for x in range(0, 6):
        color(random.choice(colours))
        snowflakeArm(size)
        right(60)


# snowflake()

for i in range(0, 10):
    size = random.randint(5, 30)
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    penup()
    goto(x, y)
    pendown()
    snowflake(size)

# def snowflake():
# for x in range (0,18):
# color(random.choice(colours))
# snowflakeArm()
# right(20)
# snowflake()

# def snowflake():
# for x in range (0,10):
##color(random.choice(colours))
# snowflakeArm()
# right(36)
# snowflake()

import time

time.sleep(10)
