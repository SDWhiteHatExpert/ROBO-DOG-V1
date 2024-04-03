# main function of ROBO DOG

def main():
    robot_dog = RobotDog()
    
    print("Robot Dog Control Panel")
    print("=======================")
    print("Commands:")
    print("1. Forward")
    print("2. Backward")
    print("3. Turn Left")
    print("4. Turn Right")
    print("5. Stop")
    print("6. Exit")
    
    while True:
        command = input("Enter command number: ")
        
        if command == "1":
            robot_dog.move_forward()
        elif command == "2":
            robot_dog.move_backward()
        elif command == "3":
            robot_dog.turn_left()
        elif command == "4":
            robot_dog.turn_right()
        elif command == "5":
            robot_dog.stop()
        elif command == "6":
            print("Exiting control panel.")
            break
        else:
            print("Invalid command number. Please try again.")
        
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
        
        # Initialize ChatGPT
        openai.api_key = 'YOUR_OPENAI_API_KEY'
        
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

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=100
    )
    return response.choices[0].text.strip()

def main():
    robot_dog = RobotDog()
    
    print("Robot Dog Control Panel")
    print("=======================")
    print("Commands:")
    print("1. Forward")
    print("2. Backward")
    print("3. Turn Left")
    print("4. Turn Right")
    print("5. Stop")
    print("6. Chat with Robot Dog")
    print("7. Exit")
    
    while True:
        command = input("Enter command number: ")
        
        if command == "1":
            robot_dog.move_forward()
        elif command == "2":
            robot_dog.move_backward()
        elif command == "3":
            robot_dog.turn_left()
        elif command == "4":
            robot_dog.turn_right()
        elif command == "5":
            robot_dog.stop()
        elif command == "6":
            user_input = input("You: ")
            response = chat_with_gpt("Human: " + user_input + "\nRobot:")
            print("Robot:", response)
        elif command == "7":
            print("Exiting control panel.")
            break
        else:
            print("Invalid command number. Please try again.")

if __name__ == "__main__":
    main()
