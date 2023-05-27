import turtle
import winsound

# Background stuff
bg = turtle.Screen()
bg.setup(800, 600)
bg.bgcolor('black')
bg.tracer(0)
bg.title('Pong')


# Score
scoreA = scoreB = 0
pen = turtle.Turtle()
pen.color('White')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A: {scoreA}  Player B: {scoreB}", align="center", font=("Courier", 24, "normal"))


def write_it():
    winsound.PlaySound('ding', winsound.SND_ASYNC)
    ball.home()
    pen.clear()
    pen.write(f"Player A: {scoreA}  Player B: {scoreB}", align="center", font=("Courier", 24, "normal"))


# The Ball
ball = turtle.Turtle()
ball.color('white')
ball.shape('square')
ball.penup()
hit_x = hit_y = 0.05


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.color('white')
paddle_a.shape('square')
paddle_a.shapesize(5, 1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.color('white')
paddle_b.shape('square')
paddle_b.shapesize(5, 1)
paddle_b.penup()
paddle_b.goto(350, 0)


# Functions
def a_up():
    if paddle_a.ycor() <= 250:
        paddle_a.sety(paddle_a.ycor() + 20)


def a_down():
    if paddle_a.ycor() >= -230:
        paddle_a.sety(paddle_a.ycor() - 20)


def b_up():
    if paddle_b.ycor() <= 250:
        paddle_b.sety(paddle_b.ycor() + 20)


def b_down():
    if paddle_b.ycor() >= -230:
        paddle_b.sety(paddle_b.ycor() - 20)


turtle.listen()
turtle.onkeypress(a_up, 'w')
turtle.onkeypress(a_down, 's')
turtle.onkeypress(b_up, 'Up')
turtle.onkeypress(b_down, 'Down')

# Main Game Loop
while True:
    bg.update()
    ball.setpos(ball.xcor() + hit_x, ball.ycor() + hit_y)
    ball_x = ball.xcor()
    ball_y = ball.ycor()
    if ball_y >= 290 or ball_y <= -290:
        hit_y *= -1
        winsound.PlaySound('bounce', winsound.SND_ASYNC)
    elif (paddle_b.xcor() - 10 <= ball_x <= paddle_b.xcor() and paddle_b.ycor() - 50 <= ball_y <= paddle_b.ycor() + 50
            or paddle_a.xcor() <= ball_x <= paddle_a.xcor() + 10 and paddle_a.ycor() - 50 <= ball_y <= paddle_a.ycor() + 50):
        hit_x *= -1
        winsound.PlaySound('bounce', winsound.SND_ASYNC)
    elif abs(ball_x) >= 400:
        if ball_x > 0:
            scoreA += 1
        else:
            scoreB += 1
        write_it()
        hit_x *= -1
