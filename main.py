import turtle as turtle
import random

print(
    "Welcome to your drawing app! Select a shape you want to draw. After typing the number and hitting enter, go to the result tab!"
)

turtle.penup()
turtle.left(90)
turtle.forward(250)
turtle.left(90)
turtle.forward(300)
turtle.pendown()

turtle.write("Drawing App!", font=("Arial", 16, "normal"))

turtle.penup()
turtle.left(90)
turtle.forward(50)
turtle.pendown()

turtle.write("To draw a shape, go to the Console tab and choose an option!",
             font=("Arial", 16, "normal"))

turtle.penup()
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.pendown()


def star():
    for num in range(5):
        turtle.color("black")
        turtle.forward(110)
        turtle.left(216)


def square():
    for num in range(4):
        turtle.color("blue")
        turtle.forward(100)
        turtle.right(90)


def hexagon():
    for num in range(6):
        turtle.color("red")
        turtle.forward(100)
        turtle.right(60)


def dodecagon():
    for num in range(12):
        turtle.color("purple")
        turtle.forward(50)
        turtle.right(30)


selection = input(
    "1. Star\n2. Square\n3. Hexagon\n4. Dodecagon\n Select a number: ")
if selection == "1":
    print("Excellent choice! Go to the result tab to see your creation.")
    star()
elif selection == "2":
    print("Excellent choice! Go to the result tab to see your creation.")
    square()
elif selection == "3":
    print("Excellent choice! Go to the result tab to see your creation.")
    hexagon()
elif selection == "4":
    print("Excellent choice! Go to the result tab to see your creation.")
    dodecagon()
