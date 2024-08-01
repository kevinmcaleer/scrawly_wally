from gpiozero import OutputDevice
from time import sleep

SPEED = 0.005 # Delay between steps

# Define the GPIO pins for the stepper motor
coil_a_1_pin = 14  # IN1
coil_a_2_pin = 15  # IN2
coil_b_1_pin = 18  # IN3
coil_b_2_pin = 23  # IN4

# Initialize the pins
coil_a_1 = OutputDevice(coil_a_1_pin)
coil_a_2 = OutputDevice(coil_a_2_pin)
coil_b_1 = OutputDevice(coil_b_1_pin)
coil_b_2 = OutputDevice(coil_b_2_pin)

# Define the step sequence for the 28BYJ-48 stepper motor
step_sequence = [
    (1, 0, 0, 0),
    (1, 1, 0, 0),
    (0, 1, 0, 0),
    (0, 1, 1, 0),
    (0, 0, 1, 0),
    (0, 0, 1, 1),
    (0, 0, 0, 1),
    (1, 0, 0, 1)
]

def set_step(w1, w2, w3, w4):
    coil_a_1.value = w1
    coil_a_2.value = w2
    coil_b_1.value = w3
    coil_b_2.value = w4

def stepper_test(delay, steps, direction=1):
    if direction == -1:  # Reverse direction
        step_sequence.reverse()
    for _ in range(steps):
        for step in step_sequence:
            set_step(*step)
            sleep(delay)
    if direction == -1:  # Restore original sequence
        step_sequence.reverse()

def main():
    try:
        while True:
            print("Rotating forward...")
            stepper_test(SPEED, 512, direction=1)  # Rotate forward 512 steps
            sleep(1)
            print("Rotating backward...")
            stepper_test(SPEED, 512, direction=-1)  # Rotate backward 512 steps
            sleep(1)
    except KeyboardInterrupt:
        print("Test stopped by user")
        # Clean up by setting all pins to low
        set_step(0, 0, 0, 0)

if __name__ == "__main__":
    main()
