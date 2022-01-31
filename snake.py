from turtle import Turtle,Screen
import random
start_positions=[(0,0),(-20,0),(-40,0)]

LEFT= 180
UP=90
RIGHT=0
DOWN=270
Move_Forward=20
class Snakes:
    def __init__(self):
        self.segments = []
        self.createsnake()
        self.head = self.segments[0]

    def createsnake(self):
        for body in start_positions:
            self.add_segments(body)
    def add_segments(self,postion):
        snake = Turtle("square")
        snake.color("green")
        snake.penup()
        snake.goto(postion)
        self.segments.append(snake)
    def extend(self):
        self.add_segments(self.segments[-1].position())
    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.head.forward(Move_Forward)
    def reset(self):
        for segment in range(len(self.segments)):
            self.segments[segment].goto(1000,1000)
        self.segments.clear()
        self.createsnake()
        self.head = self.segments[0]


    def up(self):
            if self.head.heading()!=DOWN:
                self.head.setheading(UP)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading()!= LEFT:
            self.head.setheading(RIGHT)



