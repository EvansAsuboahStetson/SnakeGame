from turtle import Turtle

with open("highscore.txt") as my_file:
    content= my_file.read()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score=0
        self.highscore=int(content)
        self.penup()
        self.goto(0, 270)
        self.updatescore()
        self.hideturtle()
    def updatescore(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", move=False, align='center', font=('Arial', 24, 'normal'))

    def increase(self):
        self.score+=1
        self.clear()
        self.updatescore()
    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", mode='w') as my_file:
                my_file.write(f"{self.highscore}")
        self.score = 0
        self.updatescore()



   #def gameOver(self):
   #    self.goto(0.00,0.00)
   #    self.write("Wawie3 Aba", move=False, align='center', font=('Arial', 24, 'normal'))





