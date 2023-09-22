from turtle import Turtle, Screen
import random




t = Turtle()

t.shape("circle")
t.color("red")
colors = ["CornflowerBlue", "DarkOrchid"]
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        t.forward(100)
        t.right(angle)

for shape_side in range(3,11):
    t.color(random.choice(colors))
    draw_shape(shape_side)

screen = Screen()
screen.exitonclick()