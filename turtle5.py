import math
import turtle
import random
import time

t = turtle.Turtle()
t.shape('turtle')

colors = ['green', 'blue', 'red', 'yellow']


def forward_and_left():
    """Функция, которая двигает вперед, меняет цвет на случайный и делает поворот"""
    t.forward(distance=50)
    t.left(90)
    time.sleep(1)


for i in range(4):
    t.color(colors[i])
    forward_and_left()

t.left(45)
t.color(colors[2])
t.forward(distance=math.sqrt(2*50**2))
turtle.done()
