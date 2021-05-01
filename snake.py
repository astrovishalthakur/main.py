from turtle import Turtle
MoveDistance = 20
position = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        self.head.shape("circle")
        self.head.color("orchid")

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def add_segment(self, i):
        new_segment = Turtle()
        new_segment.pu()
        new_segment.color("pink")
        new_segment.shape("square")
        new_segment.speed("fastest")
        new_segment.goto(i)
        self.snake_body.append(new_segment)

    def create_snake(self):
        for i in position:
            # here i is x and y coordinates both. eg. i = (0 , 20)
            self.add_segment(i)

    def move(self):
        for segment in range(len(self.snake_body) - 1, 0, -1):
            xcor = self.snake_body[segment - 1].xcor()
            ycor = self.snake_body[segment - 1].ycor()
            self.snake_body[segment].goto(xcor, ycor)
        self.head.forward(MoveDistance)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for seg in self.snake_body:
            seg.hideturtle()
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]
        self.head.shape("circle")
        self.head.color("orchid")