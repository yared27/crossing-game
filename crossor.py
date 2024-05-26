from turtle import Turtle

# Define a constant for the finish line y-coordinate
FNISH_LINE = 300

class Crossor(Turtle):
    def __init__(self):
        super().__init__()  # Initialize the Turtle superclass
        self.penup()  # Lift the pen to avoid drawing lines
        self.color("yellow")  # Set the color of the turtle to yellow
        self.shape("turtle")  # Set the shape of the turtle
        self.setheading(90)  # Set the turtle's direction to face upwards
        self.set_position()  # Set the initial position of the turtle
        self.move_by = 10  # Set the distance the turtle moves with each step
        self.shapesize(stretch_wid=2, stretch_len=1)  # Stretch the turtle shape for better visibility

    def set_position(self):
        self.goto(0, -300)  # Move the turtle to the starting position at the bottom of the screen

    def move_crossor(self):
        self.screen.update()  # Update the screen
        self.fd(10)  # Move the turtle forward by 10 units

    def is_finsh_line(self):
        if self.ycor() > FNISH_LINE:  # Check if the turtle has crossed the finish line
            return True  # Return True if the turtle has crossed the finish line
        else:
            return False  # Return False if the turtle has not crossed the finish line
