import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("green")
wn.setup(width=800,height=600)
wn.tracer(0)



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

#function

def paddle_b_up():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)


def paddle_b_down():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)


#Gameplay
while True:
     wn.update()