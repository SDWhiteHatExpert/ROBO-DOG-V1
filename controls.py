class RobotDog:
    def __init__(self):
        self.position = [0, 0]  # Initial position
        self.direction = "forward"  # Initial direction

    def move_forward(self):
        self.position[0] += 1
        return "Moving forward"

    def move_backward(self):
        self.position[0] -= 1
        return "Moving backward"

    def turn_left(self):
        self.direction = "left"
        return "Turning left"

    def turn_right(self):
        self.direction = "right"
        return "Turning right"

    def stop(self):
        return "Stopping"

def main():
    dog = RobotDog()

    while True:
        action = input("Enter action (forward, backward, left, right, stop): ")

        if action == "forward":
            print(dog.move_forward())
        elif action == "backward":
            print(dog.move_backward())
        elif action == "left":
            print(dog.turn_left())
        elif action == "right":
            print(dog.turn_right())
        elif action == "stop":
            print(dog.stop())
            break
        else:
            print("Invalid action")

if __name__ == "__main__":
    main()
