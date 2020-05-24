# Made by Jordan Leich on 5/23/2020

loops = int(input("How many loops (spirals) do you wish to create? "))
print()

from turtle import *
from random import *
import turtle
try:
    turtle.speed(int(input("Do you want a slow turtle (1) or a fast turtle (0): ")))
    print()
except:
    print("Error, ending program... ")
    print()
    quit()
wn = turtle.Screen
turtle.setup(600, 600)
t = turtle.Turtle()
turtle.bgcolor("black")
x = 0
while x < loops:
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    turtle.colormode(255)
    pencolor(r, g, b)
    fd(25 + x)
    rt(90.555)
    x = x + 1
exitonclick()
