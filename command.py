from craft_control import move

coordinates = [0, 0, 0]
direction = input("Enter initial direction of space craft: ")
commands = input("Enter command string (f, b, l, r, u, d): ")

for command in commands:
    coordinates, direction = move(coordinates, direction, command)

print("Finl Position: ", coordinates)
print("Final Direction: ", direction)