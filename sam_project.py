import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed(1) 
t.penup()
t.goto(0, 0)  

# Define a function to draw each letter
def draw_s():
    t.pendown()
    t.forward(90)
    t.right(180)
    t.forward(90)
    t.left(90)
    t.forward(90)
    t.left(90)
    t.forward(90)
    t.right(90)
    t.forward(90)
    t.right(90)
    t.forward(90)
    t.penup()

def draw_a():
    t.pendown()
    t.right(90)
    t.forward(180)
    t.right(90)
    t.forward(90)
    t.right(90)
    t.forward(180)
    print(t.pos())
    t.backward(60)
    t.right(90)
    t.forward(90)
    t.penup()

def draw_m():
    t.pendown()
    t.right(90)
    t.forward(180)
    t.right(135)
    t.forward(90)
    t.left(90)
    t.forward(90)
    t.right(135)
    t.forward(180)
    t.penup()

# Draw the letters
draw_s()
t.goto(95, -180)
draw_a()
t.goto(190, -180)
draw_m()

# Hide the turtle
t.hideturtle()

# Keep the window open until manually closed
turtle.done()
