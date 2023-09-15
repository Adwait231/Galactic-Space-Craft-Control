from craft_control import move

coordinates = [0, 0, 0]
direction = input("Enter initial direction of space craft: ")
command = input("Enter command(f, b, l, r, u, d): ")

coordinates, direction = move(coordinates, direction, command)

print("Finl Position: ", coordinates)
print("Final Direction: ", direction)