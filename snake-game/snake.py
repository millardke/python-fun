from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for segment_index in range(0, 3):
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(-20 * segment_index, 0)
            self.segments.append(segment)

    def move(self):
        for segment_index in range(len(self.segments) - 1, 0, -1):
            new_x, new_y = self.segments[segment_index - 1].pos()
            self.segments[segment_index].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)