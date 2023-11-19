import turtle
import time
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Breakout Clone")
screen.bgcolor("black")
screen.setup(width=600, height=600)

# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.speed(0)
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2

# Bricks
bricks = []

def create_bricks():
    colors = ["red", "orange", "yellow", "green", "blue"]
    for y in range(100, 250, 50):
        for x in range(-250, 251, 50):
            brick = turtle.Turtle()
            brick.shape("square")
            brick.color(random.choice(colors))
            brick.shapesize(stretch_wid=1, stretch_len=2)
            brick.penup()
            brick.goto(x, y)
            bricks.append(brick)

create_bricks()

# Paddle movement
def move_left():
    x = paddle.xcor()
    if x > -250:
        paddle.setx(x - 20)

def move_right():
    x = paddle.xcor()
    if x < 240:
        paddle.setx(x + 20)

# Keyboard bindings
screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# Main game loop
while True:
    screen.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.dy *= -1

    # Paddle collision
    if (
        -250 < ball.xcor() < -240
        and paddle.ycor() + 50 > ball.ycor() > paddle.ycor() - 50
    ) or (
        240 < ball.xcor() < 250
        and paddle.ycor() + 50 > ball.ycor() > paddle.ycor() - 50
    ):
        ball.dx *= -1

    # Brick collision
    for brick in bricks:
        if (
            brick.xcor() - 25 < ball.xcor() < brick.xcor() + 25
            and brick.ycor() + 10 > ball.ycor() > brick.ycor() - 10
        ):
            brick.hideturtle()
            bricks.remove(brick)
            ball.dy *= -1

    # Game over
    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1

    # Check for win
    if not bricks:
        ball.goto(0, 0)
        ball.dy *= -1
        create_bricks()

    time.sleep(0.01)