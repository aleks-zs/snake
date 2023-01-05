from turtle import Turtle


MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.body = []
        self.initial_snake()
        self.head = self.body[0]

    def initial_snake(self):
        initial_x = 0
        initial_y = 0
        for s in range(3):
            self.add_part((initial_x, initial_y))
            initial_x -= 20

    def add_part(self, position):
        body_part = Turtle(shape='square')
        body_part.color('white')
        body_part.penup()
        body_part.goto(position)
        self.body.append(body_part)

    def extend_snake(self):
        self.add_part(self.body[-1].position())

    def move(self):
        for s in range(len(self.body) - 1, 0, -1):
            new_x = self.body[s - 1].xcor()
            new_y = self.body[s - 1].ycor()
            self.body[s].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
