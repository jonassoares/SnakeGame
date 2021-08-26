from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
START_POSITION = [[0, 0], [40, 0], [60, 0]]


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.snake_head = self.snake_body[0]

    def create_snake(self):
        """ Create the snake body to start the game """

        for position in START_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        snake_part = Turtle(shape="square")
        snake_part.color("white")
        snake_part.penup()
        snake_part.goto(position)
        self.snake_body.append(snake_part)

    def extend_snake(self):
        self.add_segment(self.snake_body[-1].position())

    def move_snake(self):
        """" Allow snake to move  """
        for part_pos in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[part_pos].setpos(self.snake_body[part_pos - 1].pos())
        self.snake_head.forward(MOVE_DISTANCE)

    def change_snake_direction_up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(90)

    def change_snake_direction_down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(270)

    def change_snake_direction_left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(180)

    def change_snake_direction_right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(0)
