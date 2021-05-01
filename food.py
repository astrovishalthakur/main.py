from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.speed("fastest")
        self.pu()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.refresh()

    def refresh(self):
        food_x = random.randint(-270, 270)
        food_y = random.randint(-270, 270)
        self.goto(food_x, food_y)