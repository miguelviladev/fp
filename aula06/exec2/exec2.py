import os
import turtle

def main():
    path = f"{os.path.dirname(__file__)}/instructions.txt"
    t = turtle.Turtle()
    with open(path, "r") as file:
        for n in file.read().splitlines():
            if n == "UP":
                t.up()
            elif n == "DOWN":
                t.down()
            else:
                t.goto(int(n.split()[0]), int(n.split()[1]))
    turtle.Screen().exitonclick()

main()