def robot_dog_joystick(direction):
    if direction == "forward":
        return "Moving forward"
    elif direction == "backward":
        return "Moving backward"
    elif direction == "left":
        return "Turning left"
    elif direction == "right":
        return "Turning right"
    else:
        return "Invalid direction"

# Example usage:
direction_input = input("Enter direction (forward, backward, left, right): ")
print(robot_dog_joystick(direction_input))

print(robot_dog_joystick("forward"))
print(robot_dog_joystick("backward"))
print(robot_dog_joystick("left"))
print(robot_dog_joystick("right"))

