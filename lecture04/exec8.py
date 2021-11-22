import turtle

# Make turtle t draw a square with the given side length
def square(t, side):
    for n in range(4):
        t.forward(side)
        t.left(90)

# Make turtle t draw a spiral.
def spiral(t, start, end, incr):
    t.down()
    length = start
    while (length < end) != (length > end):
            t.forward(length)
            t.left(90)
            length += incr

def main():
    # Create instances of turtles
    wn = turtle.Screen()
    a = turtle.Turtle()
    b = turtle.Turtle()

    # Control a behavior
    a.up()
    a.goto(-200, 0)
    a.speed(100)

    # Control b behavior
    b.up()
    b.goto(100, 0)
    b.speed(100)

    # This should draw a spiral
    spiral(a, 10, 200, 10)
    spiral(b, 200, 0, -5)

    # Wait for click, then close window
    turtle.exitonclick()

main()