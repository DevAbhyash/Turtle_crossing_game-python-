from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=1
        self.create_Board()


    def create_Board(self):
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=250)
        self.write(arg=f"LEVEL:{self.score}", align='center', font=FONT)

    def increase_score(self):
        self.clear()
        self.score +=1
        self.create_Board()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="GAME IS OVER!", align='center', font=FONT)


