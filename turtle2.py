import time

t = turtle.Turtle()
t.shape('turtle')

colors = ['red', 'green', 'blue', 'yellow']


def forward_and_left(a):
    """Функция, которая двигает вперед, делает поворот"""
    t.forward(distance=50)
    t.left(angle=a)
    time.sleep(1)


for i in range(4):
    t.color(colors[i])
    forward_and_left(a=90)


turtle.done()
