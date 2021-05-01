from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Score(Turtle):
    def __init__(self):
        self.sc = 0
        with open("data.txt", mode='r') as file:
            high_scoree = int(file.read())
        self.high_score = high_scoree
        super().__init__()
        self.pu()
        self.color("white")
        self.sety(270)
        self.update()
        self.hideturtle()

    def update(self):
        self.clear()
        self.write(arg=("score: " + str(self.sc) + " High score: " + str(self.high_score)), move=False, align=ALIGNMENT,
                   font=FONT)

    def reset(self):
        if self.sc > self.high_score:
            self.high_score = self.sc
            with open("data.txt", mode='w') as file:
                file.write(str(self.high_score))
            self.sc = 0

    def inc_sc(self):
        self.sc += 1
