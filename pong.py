#Simple Pong game using turtle module @MEDHA

import turtle
import winsound

win=turtle.Screen()
win.title("Pong Game by MEDHA")
win.bgcolor("yellow")
win.setup(width=700, height=500)
win.tracer(0)

#Score track
left_score=0
right_score=0

pen=turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0,210)
pen.write("Player A: 0 Player B: 0",align="center",font=("Courier",20,"normal"))

#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("black")
ball.penup()
ball.goto(0,0)
ball.dx=0.3
ball.dy=-0.3

#Left Bar
leftbar=turtle.Turtle()
leftbar.speed(0)
leftbar.shape("square")
leftbar.color("black")
leftbar.shapesize(stretch_wid=4,stretch_len=1)
leftbar.penup()
leftbar.goto(-300,0)

#Right Bar
rightbar=turtle.Turtle()
rightbar.speed(0)
rightbar.shape("square")
rightbar.color("black")
rightbar.shapesize(stretch_wid=4,stretch_len=1)
rightbar.penup()
rightbar.goto(300,0)

#Functionalities
def leftbar_up():
	y=leftbar.ycor()
	y+=20
	leftbar.sety(y)
def leftbar_down():
	y=leftbar.ycor()
	y-=20
	leftbar.sety(y)
def rightbar_up():
	y=rightbar.ycor()
	y+=20
	rightbar.sety(y)
def rightbar_down():
	y=rightbar.ycor()
	y-=20
	rightbar.sety(y)

#Keyboard reading
win.listen()
win.onkeypress(leftbar_up,"q")
win.onkeypress(leftbar_down,"a")
win.onkeypress(rightbar_up,"Up")
win.onkeypress(rightbar_down,"Down")
while True:
    win.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    if(leftbar.ycor()>=250):
    	leftbar.sety(250)
    if(leftbar.ycor()<=-250):
    	leftbar.sety(-250)
    if(rightbar.ycor()>=250):
    	rightbar.sety(250)
    if(rightbar.ycor()<=-250):
    	rightbar.sety(-250)
    if(ball.ycor()>240):
    	ball.sety(240)
    	ball.dy *= -1
    	winsound.PlaySound("hit.wav",winsound.SND_ASYNC)

    if(ball.ycor()<-240):
    	ball.sety(-240)
    	ball.dy *= -1
    	winsound.PlaySound("hit.wav",winsound.SND_ASYNC)

    if(ball.xcor()>350):
    	ball.goto(0,0)
    	ball.dx *= -1
    	left_score+=1;
    	pen.clear()
    	pen.write("Player A: {} Player B: {}".format(left_score,right_score),align="center",font=("Courier",20,"normal"))

    if(ball.xcor()<-350):
    	ball.goto(0,0)
    	ball.dx *= -1
    	right_score+=1
    	pen.clear()
    	pen.write("Player A: {} Player B: {}".format(left_score,right_score),align="center",font=("Courier",20,"normal"))

    if(ball.xcor()>290 and ball.xcor()<300 and (ball.ycor()<=rightbar.ycor()+40) and (ball.ycor()>=rightbar.ycor()-40)):
    	ball.setx(290)
    	ball.dx *= -1
    	winsound.PlaySound("hit.wav",winsound.SND_ASYNC)

    if(ball.xcor()< -290 and ball.xcor()> -300 and (ball.ycor()<=leftbar.ycor()+40) and (ball.ycor()>=leftbar.ycor()-40)):
    	ball.setx(-290)
    	ball.dx *= -1
    	winsound.PlaySound("hit.wav",winsound.SND_ASYNC)
