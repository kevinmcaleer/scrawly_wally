# Scrawly Wally
# A Wall drawing robot

import math

class Scrawly():

    def move_xy(self, x:int, y:int):
        # Moves the gondola to the X & Y position
        pass

    def pen_up(self):
        # Moves the pen off the drawing surface
        pass

    def pen_down(self):
        # Places the pen on the drawing surface
        pass

# Configuration parameters
W = 900  # Width of the board in mm
H = 600  # Height of the board in mm
STEPS_PER_MM = 100  # Number of steps per millimeter for the stepper motors

# Initial position (bottom middle of the board)
X_0 = W / 2
Y_0 = H

# Function to calculate the length of the string from the motor to the gondola
def calculate_length(x, y, motor_x, motor_y):
    return math.sqrt((x - motor_x)**2 + (y - motor_y)**2)

# Function to move the gondola to an (X, Y) position
def move_to_position(x, y, current_x, current_y):
    # Motor positions
    motor1_x, motor1_y = 0, 0  # Top-left corner
    motor2_x, motor2_y = W, 0  # Top-right corner
    
    # Calculate current lengths
    current_length1 = calculate_length(current_x, current_y, motor1_x, motor1_y)
    current_length2 = calculate_length(current_x, current_y, motor2_x, motor2_y)
    
    # Calculate new lengths
    new_length1 = calculate_length(x, y, motor1_x, motor1_y)
    new_length2 = calculate_length(x, y, motor2_x, motor2_y)
    
    # Calculate change in length
    delta_length1 = new_length1 - current_length1
    delta_length2 = new_length2 - current_length2
    
    # Convert change in length to steps
    steps_motor1 = int(delta_length1 * STEPS_PER_MM)
    steps_motor2 = int(delta_length2 * STEPS_PER_MM)
    
    # Move the stepper motors
    move_stepper1(steps_motor1)
    move_stepper2(steps_motor2)
    
    # Update current position
    current_x = x
    current_y = y
    
    return current_x, current_y

# Function to raise or lower the pen
def pen_control(action):
    if action == 'up':
        control_servo('up')
    elif action == 'down':
        control_servo('down')

# Example usage
current_x = X_0
current_y = Y_0

# Move to (100, 200) and lower the pen
current_x, current_y = move_to_position(100, 200, current_x, current_y)
pen_control('down')

# Move to (150, 250) and raise the pen
current_x, current_y = move_to_position(150, 250, current_x, current_y)
pen_control('up')