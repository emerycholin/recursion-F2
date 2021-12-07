import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def spiral(myTurtle, linelen):
    while linelen > 0:
        myTurtle.forward(linelen)
        myTurtle.right(90)
        linelen = linelen - 5
                
spiral(myTurtle,100)
myWin.exitonclick()      