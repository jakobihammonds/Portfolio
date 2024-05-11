# Imports #
import turtle as t
import random as r
import time
##---Game Configuration
bodyParts = []
wn = t.Screen()
wn.setup(width=600,height=600)
wn.bgcolor("gray")
delay=0.01
#   Basic Setup for Snake
""" head turtle is the front of the snake """
head=t.Turtle(shape="square")
head.speed(0)
head.penup()
head.direction="stop" #direction obj is pointing
#   Basic Setup for Food
""" food turtle is the orange the snake eats """
food=t.Turtle(shape="circle")
food.speed(0)
food.penup()
food.teleport(100,100)
food.color("orange")

##---Functions
#game over
def hideTheBody():
    global bodyParts
    head.teleport(0,0)
    for eachBodyPart in bodyParts:
            eachBodyPart.goto(1000,1000)
    bodyParts=[]
#
def up():
    if head.direction != "down":
        head.direction="up"
#move down
def down():
    if head.direction != "up":
        head.direction="down"
#move right
def right():
    if head.direction != "left":
        head.direction="right"
#move left
def left():
    if head.direction != "right":
        head.direction="left"
def move():
    if head.direction=="up":
        head.sety(head.ycor()+20) # not the only way to do this
    elif head.direction=="right":
        head.setx(head.xcor()+20)
    elif head.direction=="down":
        head.sety(head.ycor()-20)
    elif head.direction=="left":
        head.setx(head.xcor()-20)
def headFood():
    if head.distance(food) < 20:
        food.teleport(r.randint(-290,290),r.randint(-290,290))
        bodyPart=t.Turtle(shape="square")
        bodyPart.speed(0)
        bodyPart.penup()
        bodyParts.append(bodyPart)
        print(bodyParts)
        
def wallHead(bodyParts):
    if head.ycor()>290 or head.xcor()>290 or head.ycor()<-290 or head.xcor()<-290:
        hideTheBody()
def bodyColl():
    for eachBodyPart in bodyParts:
        if head.distance(eachBodyPart)<10:
            hideTheBody()        


##---               Events
#---KEYBOARD BINDINGS | wn.onkeypress(command,"key binding")
wn.onkeypress(up,"w")
wn.onkeypress(right,"d")
wn.onkeypress(down,"s")
wn.onkeypress(left,"a")
wn.listen()


##--- Main Loop
while True:     #   Keeps code running
    wn.update() #   Update and Refresh Screen #   can also use "wn.mainloop()"
    headFood()
    wallHead(bodyParts)
    move()
    bodyColl()
#TODO check for body coll
#TODO move body parts - move end of snake to replace the neck every iteration of moving forward 
    for i in range(len(bodyParts)-1,0,-1):
        newX=bodyParts[i-1].xcor()
        newY=bodyParts[i-1].ycor()
        bodyParts[i].goto(newX,newY)
    #move neck to head
    if len(bodyParts)>0:   
        newX=head.xcor()
        newY=head.ycor()
        neck=bodyParts[0]
        bodyParts[0].goto(newX,newY)        

        

    time.sleep(delay)
