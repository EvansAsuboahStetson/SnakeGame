from turtle import Screen,Turtle
import time
from snake import Snakes
from food import Food
from scoreboard import  Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Capochino")
screen.tracer(0)

segments=[]
positions=[(0,0),(-20,0),(-40,0)]
snakes= Snakes()
food=Food()
scores =Scoreboard()

screen.listen()
screen.onkey(snakes.up,"Up")
screen.onkey(snakes.down,"Down")
screen.onkey(snakes.left,"Left")
screen.onkey(snakes.right,"Right")


game_is_on= True


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snakes.move()

    #detect collision with food
    if snakes.head.distance(food)<15:
        print("Collided")
        food.refresh()
        scores.increase()
        snakes.extend()
    #detect colliion with wall
    if snakes.head.xcor()>280 or snakes.head.xcor()<-280 or snakes.head.ycor()>280 or snakes.head.ycor()<-280:
        scores.reset()
        snakes.reset()

    #detect collision with tail
    for segment in snakes.segments[1:]:
       if snakes.head.distance(segment)<10 :
           scores.reset()
           snakes.reset()






screen.exitonclick()