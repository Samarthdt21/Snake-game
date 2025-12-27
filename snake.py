from turtle import Turtle
X=[(0,0),(-20,0),(-40,0)]  #turtle size is 20x20 at (0,0)


class Snake:
    def __init__(self):
        self.turtles=[]
        self.create_snake()
        self.head=self.turtles[0]

    def create_snake(self):
        for turtle_index in X:
            self.add_turtle(turtle_index)

    def add_turtle(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.color("red")
        new_turtle.penup()
        new_turtle.goto(position)
        self.turtles.append(new_turtle)

    def extend(self):
        self.add_turtle(self.turtles[-1].position())

    def move(self):
        for turtle_num in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[turtle_num - 1].xcor()
            new_y = self.turtles[turtle_num - 1].ycor()
            self.turtles[turtle_num].goto(new_x, new_y)
        self.turtles[0].forward(20)

    def move_up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def move_left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def move_right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)









