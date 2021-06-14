import turtle
import random
import time

screen = turtle.getscreen()
screen.bgcolor('black')
#player one
timothy = turtle.Turtle()
timothy.color('red')
timothy.shape('turtle')
#player two
anthony = turtle.Turtle()
anthony.color('blue')
anthony.shape('turtle')
#positioning the players 
anthony.penup()
timothy.penup()
timothy.goto(-300,200)
anthony.goto(-300,-200)

#setting up a finishing Line
timothy.goto(300,-250)
timothy.left(90)
timothy.pendown()
timothy.color('white')
timothy.width(3)
timothy.forward(500)
style = ('garamond',15)
timothy.write('FINISH',font=style)

#lets take timothy back home
timothy.penup()
timothy.color('red')
timothy.goto(-300,200)
timothy.right(90)

#tell both players to draw a line when they move
timothy.pendown()
anthony.pendown()

dice = [1,2,3,4,5,6,0]

#the actual Game
for i in range(30):
    if timothy.pos() >= (300,250):
        print('Player One Wins')
        break
    elif anthony.pos()>=(300,-250):
        print('Player Two Wins')
        break
    else:
        roll = random.choice(dice)
        timothy.forward(30*roll)
        time.sleep(1)

        roll2 = random.choice(dice)
        anthony.forward(30*roll2)
        time.sleep(1)

turtle.done()