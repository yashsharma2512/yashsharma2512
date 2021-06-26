import turtle
import freegames as fg
timothy = turtle.Turtle()
screen = turtle.getscreen()
screen.screensize(200,200)
anthony = turtle.Turtle()
color = input('What color would you like to use for timothy??')
timothy.color(color)
color1 =input('What color would you like to use for anthony??')
anthony.color(color1)
x = turtle.numinput('NUM','Number')
y = turtle.numinput('NUM2','Number again')
anthony.width(x)
timothy.width(y)
screen.addshape('car.gif')
turtle.shape('car.gif')
def up():
    timothy.forward(100)
def turn():
    timothy.right(50)
turtle.listen()
turtle.onkey(up,'Up')
turtle.onkey(turn,'Right')















turtle.done()