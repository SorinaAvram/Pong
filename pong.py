import turtle

wn = turtle.Screen()

#attributes
wn.title("Pong")
wn.bgcolor("pink")
wn.setup(width=800, height=600)
wn.tracer(0) #stops window from updating => speeds up game

#score variables
score_p1 = 0
score_p2 = 0

#paddle1
paddle1 = turtle.Turtle()
paddle1.speed(0) #sets the speed at max, otherwise game is really slow
paddle1.shape("square")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.color("blue")
paddle1.penup()
paddle1.goto(-350,0)


#paddle2
paddle2 = turtle.Turtle()
paddle2.speed(0) #sets the speed at max, otherwise game is really slow
paddle2.shape("square")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.color("blue")
paddle2.penup()
paddle2.goto(350,0)


#ball
ball = turtle.Turtle()
ball.speed(0) #sets the speed at max, otherwise game is really slow
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0,0)
ball.dx = 0.17 #dx = delta; moves by 1 pixels on x coordinate
ball.dy = 0.17 #dy = delta; moves by 1 pixels on y coordinate

#display score board 

pen=turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0  Player 2: 0", align="center", font=("Courier",24, "normal"))


#add animations and stuff

#move paddle1
def paddle1_up():
    y = paddle1.ycor()
    y += 20
    paddle1.sety(y)

def paddle1_down():
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)

#move paddle2
def paddle2_up():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)

def paddle2_down():
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)

#listen to keyboard input to move paddle
wn.listen()
wn.onkeypress(paddle1_up, "w") #calls function paddle1_up
wn.onkeypress(paddle1_down, "s") #calls function paddle1_up
wn.onkeypress(paddle2_up, "Up") #calls function paddle1_up
wn.onkeypress(paddle2_down, "Down") #calls function paddle1_up

#first, create main game loop 
while True:
    wn.update()#it updates the screen

#move ball
    ball.setx(ball.xcor() + ball.dx) # it will move by 1 pixels
    ball.sety(ball.ycor() + ball.dy) # it will move by 1 pixels

# create a border /check border: ball will bounce once it reaches border
    if ball.ycor() > 280: # from ball initial position to top 300; ball is 20 by 20 so 300-20=280
        ball.sety(280)
        ball.dy *=-1  #reverses the directions
    if ball.ycor() < -280: 
        ball.sety(-280)
        ball.dy *=-1
        
    if ball.xcor() > 380: # from ball initial position to left 300; ball is 20 by 20 so 300-20=280
        ball.goto(0, 0)
        ball.dx *=-1
        score_p1 += 1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_p1, score_p2), align="center", font=("Courier",24, "normal"))
    if ball.xcor() < -380: # from ball initial position to left 300; ball is 20 by 20 so 300-20=280
        ball.goto(0, 0)
        ball.dx *=-1
        score_p2 += 1
        
#ball colides with paddles
    if ball.xcor()>340 and (ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() - 40):
        ball.setx(340)
        ball.dx *=-1

    if ball.xcor()<-340 and (ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() - 40):
        ball.setx(-340)
        ball.dx *=-1

















        

