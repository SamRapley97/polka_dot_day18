from turtle import Turtle as t, Screen as s
import colorgram
import random

tim = t()
screen = s()
screen.colormode(255)

tim.pu()
x_position = -200
y_position = 200
tim.sety(y_position)
tim.setx(x_position)

colors = colorgram.extract("./image.webp", 30)

def horizontal_row():
    for _ in range(10):
        tim.color(colors[random.randint(0, 29)].rgb)
        tim.dot(20)
        tim.fd(50)

y = 0
while y < 10:
    horizontal_row()
    tim.pu()
    tim.color("white")
    y_position -= 50
    tim.sety(y_position)
    print(tim.position())
    tim.setx(x_position)
    y += 1











screen.exitonclick()
