import RPi.GPIO as GPIO
import time

class RobotDog:
    def __init__(self):
        # Define GPIO pins for motor control
        self.left_motor_forward_pin = 17
        self.left_motor_backward_pin = 18
        self.right_motor_forward_pin = 22
        self.right_motor_backward_pin = 23
        
        # Initialize GPIO settings
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.left_motor_forward_pin, GPIO.OUT)
        GPIO.setup(self.left_motor_backward_pin, GPIO.OUT)
        GPIO.setup(self.right_motor_forward_pin, GPIO.OUT)
        GPIO.setup(self.right_motor_backward_pin, GPIO.OUT)
        
    def move_forward(self):
        GPIO.output(self.left_motor_forward_pin, GPIO.HIGH)
        GPIO.output(self.right_motor_forward_pin, GPIO.HIGH)
        GPIO.output(self.left_motor_backward_pin, GPIO.LOW)
        GPIO.output(self.right_motor_backward_pin, GPIO.LOW)
        time.sleep(1)  # Adjust sleep duration for desired movement time
        self.stop()
        
    def move_backward(self):
        GPIO.output(self.left_motor_backward_pin, GPIO.HIGH)
        GPIO.output(self.right_motor_backward_pin, GPIO.HIGH)
        GPIO.output(self.left_motor_forward_pin, GPIO.LOW)
        GPIO.output(self.right_motor_forward_pin, GPIO.LOW)
        time.sleep(1)  # Adjust sleep duration for desired movement time
        self.stop()
        
    def turn_left(self):
        GPIO.output(self.left_motor_backward_pin, GPIO.HIGH)
        GPIO.output(self.right_motor_forward_pin, GPIO.HIGH)
        GPIO.output(self.left_motor_forward_pin, GPIO.LOW)
        GPIO.output(self.right_motor_backward_pin, GPIO.LOW)
        time.sleep(1)  # Adjust sleep duration for desired turning time
        self.stop()
        
    def turn_right(self):
        GPIO.output(self.left_motor_forward_pin, GPIO.HIGH)
        GPIO.output(self.right_motor_backward_pin, GPIO.HIGH)
        GPIO.output(self.left_motor_backward_pin, GPIO.LOW)
        GPIO.output(self.right_motor_forward_pin, GPIO.LOW)
        time.sleep(1)  # Adjust sleep duration for desired turning time
        self.stop()
        
    def stop(self):
        GPIO.output(self.left_motor_forward_pin, GPIO.LOW)
        GPIO.output(self.right_motor_forward_pin, GPIO.LOW)
        GPIO.output(self.left_motor_backward_pin, GPIO.LOW)
        GPIO.output(self.right_motor_backward_pin, GPIO.LOW)

def main():
    robot_dog = RobotDog()
    
    while True:
        command = input("Enter command (forward, backward, left, right, stop): ")
        
        if command == "forward":
            robot_dog.move_forward()
        elif command == "backward":
            robot_dog.move_backward()
        elif command == "left":
            robot_dog.turn_left()
        elif command == "right":
            robot_dog.turn_right()
        elif command == "stop":
            robot_dog.stop()
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()
