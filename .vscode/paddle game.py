import turtle

wn = turtle.Screen()
wn.title("PaddleBall")
wn.bgcolor("green")
wn.setup(width=800,height=600)
wn.tracer(0)

# score 1

#score 2


# Bat A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("circle")
paddleA.shapesize(stretch_wid=7, stretch_len=1)
paddleA.color("pink")
paddleA.penup()
paddleA.goto(-350,0)


#Bat B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("circle")
paddleB.shapesize(stretch_wid=7, stretch_len=1)
paddleB.color("pink")
paddleB.penup()
paddleB.goto(350,0)



#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.color("pink")
ball.penup()
ball.goto(0,0)
ball.dx=0.3
ball.dy=0.2

#function

def paddle_a_up():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)




def paddle_a_down():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)



# Keyboard
wn.listen()
wn.onkeypress(paddle_a_up, "e")
wn.onkeypress(paddle_a_down, "d")
# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(-200,230)
soc = pen.write("Playa One: 0  Playa Two : 0", font=("Courier",24,"normal"))
#function

def paddle_b_up():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)


def paddle_b_down():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)

# Keyboard
wn.listen()
wn.onkeypress(paddle_b_up, "o")
wn.onkeypress(paddle_b_down, "l")
#Gameplay
while True:
     wn.update()

    
    # ball movement
     ball.setx(ball.xcor() +ball.dx)
     ball.sety(ball.ycor() +ball.dy)
     
    #  border
     if ball.ycor() >290:
         ball.sety(290)
         ball.dy *= -1
        
     if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy *= -1
        
     if ball.xcor() >385:
         ball.goto(0,0)
         ball.dx *= -1
     if ball.xcor() <-385:
        ball.goto(0,0)
        ball.dx *= -1
    # // paddle and ball  
     if (ball.xcor()>340 and ball.xcor()<350)and (ball.ycor()< paddleB.ycor()+ 60 and ball.ycor()> paddleB.ycor() - 60):
            ball.setx(340)
            ball.dx *= -1
     if (ball.xcor()>-390 and ball.xcor()< -350)and (ball.ycor()< paddleA.ycor()+ 60 and ball.ycor()> paddleA.ycor() - 60):
            ball.setx(-340)
            ball.dx *= -1
    
