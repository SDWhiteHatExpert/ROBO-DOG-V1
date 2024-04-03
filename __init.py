class RobotDog:
    def __init__(self, name, color, breed):
        self.name = name
        self.color = color
        self.breed = breed
        self.energy = 100  # Initial energy level
        self.is_running = False
        self.is_barking = False

    def bark(self):
        self.is_barking = True
        print(f"{self.name} is barking!")

    def stop_barking(self):
        self.is_barking = False
        print(f"{self.name} stopped barking.")

    def run(self):
        if self.energy > 0:
            self.is_running = True
            self.energy -= 10  # Decrease energy when running
            print(f"{self.name} is running.")
        else:
            print(f"{self.name} is too tired to run.")

    def stop_running(self):
        self.is_running = False
        print(f"{self.name} stopped running.")

    def recharge(self):
        self.energy = 100
        print(f"{self.name} has been recharged.")

# Example usage:
my_robot_dog = RobotDog("Buddy", "Golden", "YEAH BUDDY , LIGHTWEIGHT")
print(f"My robot dog's name is {my_robot_dog.name}.")
print(f"It is a {my_robot_dog.color} {my_robot_dog.breed}.")
my_robot_dog.bark()
my_robot_dog.run()
my_robot_dog.stop_running()
my_robot_dog.recharge()
