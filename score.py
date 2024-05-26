from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1  # Initialize the level to 1
        self.hideturtle()  # Hide the turtle (we only need it for writing text)
        self.penup()  # Lift the pen to avoid drawing lines
        self.goto(-280, 280)  # Position the turtle at the top-left corner of the screen
        self.update_level()  # Display the initial level

    def update_level(self):
        self.clear()  # Clear the previous level display
        self.write(f"LEVEL: {self.level}", align="left", font=("Arial", 15, "normal"))  # Write the current level

    def increase_level(self):
        self.level += 1  # Increase the level by 1
        self.update_level()  # Update the level display

    def game_over(self):
        self.color("red")  # Set the text color to red
        self.goto(0, 0)  # Move the turtle to the center of the screen
        self.hideturtle()  # Hide the turtle again (it might have been shown during movement)
        self.write("GAME OVER", align="center", font=("Arial", 15, "normal"))  # Display "GAME OVER" message
