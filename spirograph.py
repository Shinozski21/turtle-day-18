import turtle as t
import random

shin = t.Turtle()


t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g, b)
    return random_color

def draw_spirograph(size_of_gap):
    for _ in range(int(360/ size_of_gap)):
        shin.speed("fastest")
        shin.color(random_color())
        shin.circle(100)
        shin.setheading(shin.heading() + size_of_gap)

draw_spirograph(5)




screen = t.Screen()
screen.exitonclick()