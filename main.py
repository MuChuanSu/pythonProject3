import turtle
import winsound

# set up the game window/screen
window = turtle.Screen()
window.title("Pong Game")
window.bgcolor("black")
window.setup(width=800, height=600)

window.tracer(0)
# this line turn the animation offso it will run faster


# setup players

playerA = turtle.Turtle()
# create an object
playerA.speed(0)  # fastest speed

playerA.shape("square")
playerA.shapesize(stretch_len=1, stretch_wid=5)
playerA.color("white")
playerA.penup()
playerA.goto(-350, 0)
##
playerB = turtle.Turtle()
# create an object
playerB.speed(0)  # fastest speed

playerB.shape("square")
playerB.shapesize(stretch_len=1, stretch_wid=5)
playerB.color("white")
playerB.penup()
playerB.goto(350, 0)

# set up the ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2  # move 1 pixels every time, speed of the ball
ball.dy = 0.2
# turtle object for showing scores
scorePen = turtle.Turtle()
scorePen.color("white")
scorePen.speed(0)
scorePen.penup()
scorePen.hideturtle()
scorePen.goto(0, 260)
scorePen.write("Player A: 0 X Player B: 0", align="center", font=("Courier", 24, "normal"))
# this is initial score, only shows once when the game starts



# Score variable
scoreA = 0
scoreB = 0
# define functions for moving

def move_a_up():
    y = playerA.ycor()
    y += 40
    playerA.sety(y)
    # set y cor to new y


def move_a_down():
    y = playerA.ycor()
    y -= 40
    playerA.sety(y)


def move_b_up():
    y = playerB.ycor()
    y += 40
    playerB.sety(y)
    # set y cor to new y


def move_b_down():
    y = playerB.ycor()
    y -= 40
    playerB.sety(y)


# keyboard binding


window.listen()
window.onkeypress(move_a_up, "w")
window.onkeypress(move_a_down, "s")
window.onkeypress(move_b_up, "Up")
window.onkeypress(move_b_down, "Down")
# call function move_a_up when w key is pressed


# Loop the game
while True:
    window.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Y border check, make the ball bounce before it leaves the screen
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        # bounces the ball back
        winsound.PlaySound("C:/Users/newxz/PycharmProjects/pythonProject3/hit.wav", winsound.SND_ASYNC)


    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        # bounces the ball back
        winsound.PlaySound("C:/Users/newxz/PycharmProjects/pythonProject3/hit.wav", winsound.SND_ASYNC)


    # X border check
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        # reset the ball position and speed
        # playerA scores
        ball.dx = 0.2  # move 1 pixels every time, speed of the ball
        ball.dy = 0.2
        scoreA += 1
        scorePen.clear()
        scorePen.write("Player A: " + str(scoreA) + " X Player B: " + str(scoreB), align="center", font=("Courier", 24, "normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        # reset the ball position
        # playerB scores
        scoreB += 1
        ball.dx = 0.2
        ball.dy = 0.2
        scorePen.clear()
        scorePen.write("Player A: " + str(scoreA) + " X Player B: " + str(scoreB), align="center", font=("Courier", 24, "normal"))
        winsound.PlaySound("C:/Users/newxz/PycharmProjects/pythonProject3/score.wav",winsound.SND_ASYNC)

    # check ball and player collisions
    # if the ball is touching the players and in the range of player square, bounce back
    # playerB
    if ball.xcor() > 340 and ball.ycor() < playerB.ycor() + 40 and ball.ycor() > playerB.ycor() - 40:
        ball.dx *= -1
        winsound.PlaySound("C:/Users/newxz/PycharmProjects/pythonProject3/hit.wav", winsound.SND_ASYNC)
        ball.dx *= 1.2

    # playerA
    if ball.xcor() < -340 and ball.ycor() < playerA.ycor() + 40 and ball.ycor() > playerA.ycor() - 40:
        ball.dx *= -1
        winsound.PlaySound("C:/Users/newxz/PycharmProjects/pythonProject3/hit.wav", winsound.SND_ASYNC)
        ball.dx *= 1.2

    # limit player movements to prevent them go out of border
    if playerA.ycor() > 240:
        playerA.sety(240)

    if playerA.ycor() < -240:
        playerA.sety(-240)

    if playerB.ycor() > 240:
        playerB.sety(240)

    if playerB.ycor() < -240:
        playerB.sety(-240)

#test