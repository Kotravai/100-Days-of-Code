from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Verdana", 16, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.value = 0
        self.read_highscore()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def read_highscore(self):
        with open("data.txt") as high_scr:
            high_score = int(high_scr.read())
        return high_score

    def update_scoreboard(self):
        self.clear()
        self.write(f"score:{self.value} || High Score: {self.read_highscore()}", False, ALIGNMENT, FONT)

    def reset_score(self):
        if self.value > self.read_highscore():
            with open("data.txt", "w") as high_scr:
                high_scr.write(str(self.value))
        self.value = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER!", False, ALIGNMENT, FONT)

    def increase_score(self):
        self.value += 1
        self.update_scoreboard()



