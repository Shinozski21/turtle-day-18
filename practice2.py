import turtle as t
import random
shin = t.Turtle()
t.colormode(255)

shin.pensize(15)
shin.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

colors = ["red", "blue", "green", "purple"]
directions = [0, 90, 180, 270]

for _ in range(400):
    shin.color(random_color())
    shin.forward(30)
    shin.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()















