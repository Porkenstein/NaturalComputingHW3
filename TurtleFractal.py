import turtle
import re

turtle.mode("logo")
t = turtle.Turtle()
t.ht()

def draw (prodRule, rotate, length):
    location = []
    heading = []
    for i in prodRule:
        if i == "G":
            t.fd(length)
        if i == "F":
            t.fd(length)
        if i == "-":
            t.left(rotate)
        if i == "+":
            t.right(rotate)
        if i == "[":
            location.append(t.pos())
            heading.append(t.heading())
        if i == "]":
            t.penup()
            t.setpos(location.pop())
            t.seth(heading.pop())
            t.pendown()

def generateProduction(initial, Frule, Grule, iteration):

    for i in range(0, iteration):
        new = ''
        for j in initial:
            if j == "G":
                new += Grule
            if j == "F":
                new += Frule
            if j == "[":
                new += "["
            if j == "]":
                new += "]"
            if j == "+":
                new += "+"
            if j == "-":
                new += "-"
        initial = new
    return initial

def test():
    Frule = "G[-F]G[+F]F"
    Grule = "GG"
    initial = "F"
    rotate = 45
    
    initial = generateProduction(initial, Frule, Grule, 2)

    draw(initial, rotate, 25)

def fractal1():
    initial = "G"
    rotate = 22.5
    Frule = 'FF'
    Grule = "F+[[G]-G]-F][-FG]+G"
    iterations = 8

    for i in range(0, 8):
        new = ''

        for j in initial:
            if j == "G":
                new += Grule
            if j == "F":
                new += Frule
        initial = new
                   
def fractal2():
    Frule = "FF+[+F-F-F]-[-F+F+F]"
    Grule = ""
    initial = "F"
    rotate = 22.5
    iteration = 4

    initial = generateProduction(initial, Frule, Grule, iteration)

    draw(initial, rotate, 5)

def fractal3():
    Frule = "FF"
    Grule = "F[+FFG][G]-FG"
    initial = "G"
    iteration = 6
    rotate = 22.5

    initial = generateProduction(initial, Frule, Grule, iteration)

    draw(initial, rotate, 1)

def fractal4():
    Frule = "FF"
    Grule = "F[-G]F[+G]-G"
    initial = "G"
    iteration = 9
    rotate = 20

    initial = generateProduction(initial, Frule, Grule, iteration)

    draw(initial, rotate, 0.25)


def fractal5():
    Frule = "FF"
    Grule = "F[-G][+G]FG"

def fractal6():
    Frule = "FF"
    Grule = "FG[-F[G]-G][G+G][+F[G]+G]"
    initial = "G"
    iteration = 5
    rotate = 22.5

    initial = generateProduction(initial, Frule, Grule, iteration)

    draw(initial, rotate, 0.25)


def fractal7():
    Frule = "FFF"
    Grule = "G[-G]-FG+[G+G]"

def fractal8():
    Frule = "F"
def fractal9():
    Frule = "F-F"
def fractal10():
    Frule = "FF-F"


def main():
    
    fractal4()
    input("Press Enter to continue...")


if __name__ == '__main__':
    main()

