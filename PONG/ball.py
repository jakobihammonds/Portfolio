#imports
import turtle as t
import time as ti
import random as r

COURT_WIDTH=1000
COURT_HEIGHT=600
PADDLE_WIDTH=50
PADDLE_HEIGHT=0


wn = t.Screen()
wn.setup(width=1100,height=700)
ball = t.Turtle("circle")
ball.color("red")
ball.penup()
ball.speed(0)
wn.title("Pong")



def ballCourt():
    draw=t.Turtle(shape="circle")
    draw.teleport(-500,300)
    draw.goto(500,300)
    draw.teleport(-500,-300)
    draw.goto(500,-300)
    draw.teleport(0,-300)
    draw.pendown()
    draw.lt(90)
    for i in range(600//50):
        draw.fd(26)
        draw.penup()
        draw.fd(26)
        draw.pendown()
    draw.hideturtle()

    leftPlayer = t.Turtle("square")
    leftPlayer.color("Blue")
    leftPlayer.penup()
    leftPlayer.speed(0)
    leftPlayer.turtlesize(4,1)
    leftPlayer.setx(-COURT_WIDTH/2)



    rightPlayer = t.Turtle("square")
    rightPlayer.color("Red")
    rightPlayer.penup()
    rightPlayer.speed(0)
    rightPlayer.turtlesize(4,1)
    rightPlayer.setx(COURT_WIDTH/2)
        


    def leftPlayerUp():
        if leftPlayer.ycor()<(COURT_HEIGHT/2-PADDLE_WIDTH):
            leftPlayer.sety(leftPlayer.ycor()+10)
    def rightPlayerUp():
        if rightPlayer.ycor()<(COURT_HEIGHT/2-PADDLE_WIDTH):
            rightPlayer.sety(rightPlayer.ycor()+10)   
    def leftPlayerDown():
        if leftPlayer.ycor()>(-COURT_HEIGHT/2+PADDLE_WIDTH):
            leftPlayer.sety(leftPlayer.ycor()-10)
    def rightPlayerDown():
        if rightPlayer.ycor()>(-COURT_HEIGHT/2+PADDLE_WIDTH):
            rightPlayer.sety(rightPlayer.ycor()-10)
        
    #events
    wn.onkeypress(leftPlayerUp,"w")
    wn.onkeypress(leftPlayerDown,"s",)
    wn.onkeypress(rightPlayerUp,"Up")
    wn.onkeypress(rightPlayerDown,"Down")
    wn.listen()

def resetBall():
     ball.setposition(0,0)
     #randomizer for who serves first
     if r.randint(0,1)==0:    #left first
          ball.setheading(r.randint(150,210))
     else:
          ball.setheading(r.randint(-30,30))

def moveTheBall():
    ball.fd(2)
    x,y = ball.position()
    #top wall and bottom wall
    if y>(COURT_HEIGHT/2) or y<(COURT_HEIGHT/2):
        ball.setheading(-ball.heading())
    #left/right wall reset/score
    elif x<(-COURT_WIDTH)/2 or x>(COURT_WIDTH/2):
        resetBall()
    wn.ontimer(moveTheBall,1)
#game
ballCourt()
moveTheBall()

wn.mainloop()
