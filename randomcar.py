from turtle import Turtle
import random

# Constants for car movement and speed increase
MOVE = 5
INCREASE_BY = 10
COLORS = ["yellow", "blue", "green", "red", "gray"]

class Carrand:
    def __init__(self):
        self.cars_speed = MOVE  # Initial speed of the cars
        self.cars_list = []  # List to keep track of all the cars

    def move_car(self):
        # Move each car in the cars_list backward by the current car speed
        for i in self.cars_list:
            i.backward(self.cars_speed)

    def speed_up(self):
        # Increase the speed of the cars
        self.cars_speed += INCREASE_BY

    def cars(self):
        # Randomly create a new car
        rand_no = random.randint(1, 6)
        if rand_no == 1:  # Approximately 1 in 6 chance to create a new car
            new_car = Turtle("square")  # Create a new turtle object shaped like a square
            new_car.color(random.choice(COLORS))  # Set the car's color to a random choice from COLORS
            new_car.shapesize(stretch_wid=1, stretch_len=2)  # Stretch the car shape to be a rectangle
            new_car.penup()  # Lift the pen to avoid drawing lines
            y = random.randint(-250, 250)  # Choose a random y-coordinate for the car
            new_car.goto(350, y)  # Place the car at the right edge of the screen
            self.cars_list.append(new_car)  # Add the new car to the cars_list
