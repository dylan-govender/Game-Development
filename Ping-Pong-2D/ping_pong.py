import turtle

display = turtle.Screen()  # Creating a window display
display.title("Ping Pong")  # Title
display.bgcolor("black")  # Background color
display.setup(width=800, height=600)  # Size of the window
display.tracer(0)  # Manually Update the window so game run faster (Window Tracer)

# Score
scoreA = 0
scoreB = 0

# Paddle A (The platform the ball land on)
paddleA = turtle.Turtle()
paddleA.speed(0)  # Set paddle to max speed
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)

# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)  # Set paddle to max speed
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)  # Set paddle to max speed
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("{}                             {}".format(scoreA, scoreB), align="center", font=("Comic Sans MS", 24, "normal"))


# Player Movement function
def MovePaddleAUp():
    y = paddleA.ycor()
    y += 50
    paddleA.sety(y)


def MovePaddleADown():
    y = paddleA.ycor()
    y -= 50
    paddleA.sety(y)


def MovePaddleBUp():
    y = paddleB.ycor()
    y += 50
    paddleB.sety(y)


def MovePaddleBDown():
    y = paddleB.ycor()
    y -= 50
    paddleB.sety(y)


# Ball Movement
ball.dx = 0.4  # Delta x / y function move x and y direction
ball.dy = -0.4

# Key board binding
display.listen()
display.onkeypress(MovePaddleAUp, "w")
display.onkeypress(MovePaddleADown, "s")
display.onkeypress(MovePaddleBUp, "Up")
display.onkeypress(MovePaddleBDown, "Down")

# Main game loop
while True:
    display.update()  # Every time the loop runs the display updates

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Ball Movement Restriction
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreA += 1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scoreB += 1

    # Paddle and ball collision
    if (ball.xcor() > 330) and (ball.xcor() < 340) and (ball.ycor() < paddleB.ycor() + 50) and (ball.ycor() > paddleB.ycor() - 50):
        ball.setx(330)
        ball.dx *= -1

    if (ball.xcor() < -330) and (ball.xcor() > -340) and (ball.ycor() < paddleA.ycor() + 50) and (ball.ycor() > paddleA.ycor() - 50):
        ball.setx(-330)
        ball.dx *= -1

    pen.clear()
    pen.write("{}                             {}".format(scoreA, scoreB), align="center", font=("Comic Sans MS", 24, "normal"))
