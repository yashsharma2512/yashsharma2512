import turtle 

#screen
screen = turtle.Screen()
screen.title('pong game')
screen.bgcolor('teal')
screen.setup(1000,600)


#left paddle
left = turtle.Turtle()
left.shape('square')
left.color('light pink')
left.penup()
left.goto(-400,0)

left.shapesize(6,2)

#right paddle
right = left.clone()
right.goto(400,0)

#center ball
ball = turtle.Turtle()
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx = 5
ball.dy = -5

#score
ls = 0
rs = 0

# display score
ref = turtle.Turtle()
ref.hideturtle()
ref.color('white')
ref.penup()
ref.goto(-220, 220)
ref.write(f'LEFT SCORE :{ls}              RIGHT SCORE :{rs}', font = ('Agency FB', '30' ))

#move paddles
def leftup():
    y = left.ycor()
    y+=20
    left.sety(y)
def lefdown():
    y = left.ycor()
    y-=20
    left.sety(y)

def rightup():
    y = right.ycor()
    y+=20
    right.sety(y)
def rightdown():
    y = right.ycor()
    y-=20
    right.sety(y)
#key binds
screen.listen()
screen.onkeypress(leftup, 'w')
screen.onkeypress(lefdown, 's')
screen.onkeypress(rightup, 'Up')
screen.onkeypress(rightdown, 'Down')
while True:
    screen.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Check borders 
    if ball.ycor() >280:
        ball.sety(280)
        ball.dy *= -1

    if ball.ycor() <-280:
        ball.sety(-280)
        ball.dy *=-1

    if ball.xcor() >500:
        ball.goto(0,0)
        ball.dy *=-1
        ls+=1
        ref.clear()
        ref.write(f'LEFT SCORE :{ls}              RIGHT SCORE :{rs}', font = ('Agency FB', '30' ))

    if ball.xcor() <-500:
        ball.goto(0,0)
        ball.dy *=-1
        rs+=1
        ref.clear()
        ref.write(f'LEFT SCORE :{ls}              RIGHT SCORE :{rs}', font = ('Agency FB', '30' ))


    #PADDLE COLLISION
    if ( ball.xcor()>360 and ball.xcor()<400) and (ball.ycor()<right.ycor() +40 and ball.ycor() >right.ycor()-40):
        ball.setx(360)
        ball.dx *=-1
    if ( ball.xcor()<-360 and ball.xcor()>-400) and (ball.ycor()<left.ycor() +40 and ball.ycor() >left.ycor()-40):
        ball.setx(-360)
        ball.dx *=-1

turtle.done()