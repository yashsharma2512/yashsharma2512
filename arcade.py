import turtle

screen = turtle.getscreen()
screen.bgcolor('black')

timothy = turtle.Turtle()
timothy.color('white')
timothy.shape('turtle')
timothy.width(5)

#FUNCTIONS


def square():
    timothy.forward(100)
    timothy.right(90)
    timothy.forward(100)
    timothy.right(90)


def up():
    timothy.setheading(90)
    timothy.forward(100)

def down():
    timothy.setheading(270)
    timothy.forward(100)
def right():
    timothy.setheading(0)
    timothy.forward(100)
def left():
    timothy.setheading(180)
    timothy.forward(100)

turtle.listen()

turtle.onkey(up,'Up')
turtle.onkey(down,'Down')
turtle.onkey(left,'Left')
turtle.onkey(right,'Right')






turtle.done( )
