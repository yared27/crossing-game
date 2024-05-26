from turtle import Screen
from crossor import Crossor
from randomcar import Carrand
from score import Score
import time

# Set up the screen for the game
screen = Screen()
screen.tracer(0)  # Disable automatic screen updates

# Create game objects
side_crossor = Crossor()  # The player-controlled character
car = Carrand()  # The cars that will move across the screen
scores = Score()  # The scorekeeping system

# Configure the screen's appearance and input handling
screen.bgcolor("white")  # Set the background color to white
screen.screensize(600, 600)  # Set the screen size to 600x600 pixels
screen.listen()  # Enable the screen to listen for key presses
screen.onkey(side_crossor.move_crossor, "Up")  # Move the player character up when the "Up" key is pressed

# Start the game loop
is_game_on = True
while is_game_on:
    screen.update()  # Update the screen with all the drawings
    time.sleep(0.1)  # Pause for a short duration to control game speed

    car.cars()  # Create new cars
    car.move_car()  # Move the cars across the screen

    # Check for collisions between the player character and any cars
    for cars in car.cars_list:
        if cars.distance(side_crossor) < 27:  # If the distance between the player and a car is less than 27
            is_game_on = False  # End the game
            scores.game_over()  # Display the game over message

    # Check if the player character has reached the finish line
    if side_crossor.is_finsh_line():
        side_crossor.set_position()  # Reset the player character's position
        car.speed_up()  # Increase the speed of the cars
        scores.increase_level()  # Increase the game level and update the score

# Exit the game when the screen is clicked
screen.exitonclick()
