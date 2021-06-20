import turtle
import random
import time

#we created a screen
screen = turtle.getscreen()
screen.bgcolor('teal')

#We create the first player 
timothy = turtle.Turtle()
timothy.color('red')
timothy.shape('turtle')

#Second Player

anthony = turtle.Turtle()
anthony.color('blue')
anthony.shape('turtle')

#setting up our players
#make sure they dont draw a line right now
timothy.penup()
anthony.penup()
#make the turtle go to their starting positions
timothy.goto(-300,200)
anthony.goto(-300,-200)

#ask player one to draw the finishing line

timothy.goto(300,-250)
timothy.left(90)
timothy.color('white')
timothy.width(5)
timothy.pendown()
timothy.forward(500)
timothy.write('FINISH',font=25)
timothy.width(1)
timothy.color('red')
timothy.penup()
timothy.goto(-300,200)
timothy.right(90)



#let turtles draw

timothy.pendown()
anthony.pendown()

dice = [1,2,3,4,5,6,0]

for i in range(30):
    if timothy.pos() >= (300,250):
        print('Timothy Jeet Gaya')
        break
    elif anthony.pos() >= (300,-250):
        print('Anthont ROXXX')
        break
    else:
        roll = random.choice(dice)
        timothy.forward(30*roll)
        time.sleep(1)

        roll2 = random.choice(dice)
        anthony.forward(30*roll2)
        time.sleep(1)
turtle.done()