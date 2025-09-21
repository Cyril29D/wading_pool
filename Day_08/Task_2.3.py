from turtle import *


def draw_polygon(sides):

    side_length = 50

    for i in range(sides):
        forward(side_length)
        left(360 / sides)


def main():
    sides = textinput("Sides", "Number of sides")
    clear()
    draw_polygon(int(sides))


while True:
    main()
