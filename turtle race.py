import turtle
import random
import time

#Creating a Screen!!!
screen = turtle.getscreen()
screen.bgcolor('teal')

#Creating Our Players

timothy = turtle.Turtle()
timothy.color('red')
timothy.shape('turtle')

#second player
anthony = turtle.Turtle()
anthony.color('blue')
anthony.shape('turtle')

#position our players
timothy.penup()
anthony.penup()
timothy.goto(-300,200)
anthony.goto(-300,-200)

#making the finish line
turtle.penup()
turtle.goto(300,-250)
turtle.left(90)
turtle.pendown()
turtle.color('white')
turtle.width(5)
turtle.forward(500)
turtle.write('FINISH', font=24)

#now lets play
timothy.pendown()
anthony.pendown()

dice = [1,2,3,4,5,6,0]

#create our game
for i in range(30):
    if timothy.pos() >=(300,250):
        print('Timothy jeet Gaya')
        break
    elif anthony.pos()>= (300,-250):
        print('ANthony Jeet Gaya')
        break
    else:
        roll = random.choice(dice)
        timothy.forward(roll *30)
        time.sleep(1)
        roll2 = random.choice(dice)
        anthony.forward(30*roll2)
        time.sleep(1)

turtle.done()

