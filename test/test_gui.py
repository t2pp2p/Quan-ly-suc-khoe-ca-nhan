import turtle as tu
import random

# Set up the screen
wn = tu.Screen()
wn.bgcolor("black")
wn.title("Frozen Snow Flower")
wn.setup(width=800, height=800)

# Create turtle
roo = tu.Turtle()
roo.speed(0)
roo.pensize(2)

# Define colors
colors = ["#A9D8E6", "#6AC0D4", "#C1A9F7", "#D8E6F7"]

def draw_tree(length, pensize, color):
    if length < 10:
        return
    roo.pensize(pensize)
    roo.pencolor(color)
    roo.forward(length)
    roo.left(30)
    draw_tree(length * 0.7, pensize - 1, random.choice(colors))
    roo.right(60)
    draw_tree(length * 0.7, pensize - 1, random.choice(colors))
    roo.left(30)
    roo.backward(length)

def draw_snow_flower(sides, length, pensize):
    for _ in range(sides):
        color = random.choice(colors)
        draw_tree(length, pensize, color)
        roo.right(360 / sides)

# Draw the snow flower
draw_snow_flower(12, 120, 10)

# Hide turtle and wait for user to click to exit
roo.hideturtle()
wn.exitonclick()
