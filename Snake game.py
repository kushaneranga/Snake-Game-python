# simple snake game
# made by - "Kushan Eranga"

import turtle
import time
import random

delay = 0.1  # snake speed
# score
score = 0
meals_count = 0
high_score = 0
# create a screen
sc = turtle.Screen()
sc.title("~Snake Game~")
sc.setup(width=500, height=580)
sc.bgcolor("light blue")
sc.tracer(0)
# Snake
snake = turtle.Turtle()
snake.shape("circle")
snake.color("brown")
snake.speed(0)
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

# snake meals
meals = turtle.Turtle()
meals.shape("circle")
meals.color("green")
meals.speed(0)
meals.penup()
# or |meals.goto(0,50)|<- this code you can trope decided place
x = random.randint(-230, 230)
y = random.randint(-240, 230)
meals.goto(x, y)
# ------------------------------
tails = []

# pen / Score Board
pen = turtle.Turtle()
pen.speed()
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score:0  Meals:0  High score:0", align="center", font=("Courier", 14, "normal"))


# Function

def move_up():
    if snake.direction != "down":  # if snake moving up, couldn't move down
        snake.direction = "up"  # original


def move_down():
    if snake.direction != "up":
        snake.direction = "down"  # original


def move_right():
    if snake.direction != "left":
        snake.direction = "right"  # original


def move_left():
    if snake.direction != "right":
        snake.direction = "left"  # original


# ----------------------------------------
def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 10)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 10)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 10)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 10)


# key
sc.listen()
sc.onkeypress(move_up, "w")
sc.onkeypress(move_down, "s")
sc.onkeypress(move_right, "d")
sc.onkeypress(move_left, "a")

# main game loop update
while True:
    sc.update()
    # screen border
    if snake.xcor() > 230 or snake.xcor() < -230 or snake.ycor() > 240 or snake.ycor() < -270:
        time.sleep(0.5)  # delay time (s)
        snake.goto(0, 0)  # center
        snake.direction = "stop"

        # hide the tail
        for tail in tails:  # tail / tails
            tail.goto(700, 700)  # out of screen value
# reset for snake hit the boundary
        # clear the tail
        tails.clear()
        # reset the score
        score = 0
        meals_count = 0
        # reset the speed
        delay = 0.1
        # Update the score
        pen.clear()
        pen.write("Score: {} Meals: {}  High Score: {}".format(score, meals_count, high_score), align="center",
                  font=("Courier", 14, "normal"))
    # drop the meals to a random place
    if snake.distance(meals) < 10:
        x = random.randint(-230, 230)
        y = random.randint(-240, 230)
        meals.goto(x, y)

        new_tail = turtle.Turtle()
        new_tail.speed(0)
        new_tail.shape("circle")
        new_tail.color("brown")
        new_tail.penup()
        tails.append(new_tail)
        # Snake speed increase automatically (related line No:5)
        delay -= 0.001
        # Score result
        score += 5
        meals_count += 1
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} Meals: {}  High Score: {}".format(score, meals_count, high_score), align="center",
                  font=("Courier", 14, "normal"))

    for index in range(len(tails) - 1, 0, -1):
        x = tails[index - 1].xcor()
        y = tails[index - 1].ycor()
        tails[index].goto(x, y)

    if len(tails) > 0:
        x = snake.xcor()
        y = snake.ycor()
        tails[0].goto(x, y)

    move()
    # check for snake collision with the body tails
    for tail in tails:
        if tail.distance(snake) < 10:
            time.sleep(0.5)
            snake.goto(0, 0)
            snake.direction = "stop"

            for tail in tails:
                tail.goto(700, 700)
# reset for snake bit a tail
            # clear the tails
            tails.clear()
            # reset the score
            score = 0
            meals_count = 0
            # reset the speed
            delay = 0.1
            # Update the score
            pen.clear()
            pen.write("Score: {} Meals: {}  High Score: {}".format(score, meals_count, high_score), align="center",
                      font=("Courier", 14, "normal"))

    time.sleep(delay)
