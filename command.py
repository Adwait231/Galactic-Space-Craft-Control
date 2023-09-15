from craft_control import move

coordinates = [0, 0, 0]
direction = input("Enter initial direction of space craft: ")

def execute(coordinates, direction, commands):

    for command in commands:
        coordinates, direction = move(coordinates, direction, command)

    print("Finl Position: ", coordinates)
    print("Final Direction: ", direction)

    return coordinates,direction


while True:
    x = int(input("Enter 0 to exit or 1 to continue: "))
    if(x==0):
        break
    else:   
        commands = input("Enter command string (f, b, l, r, u, d): ")
        coordinates,direction = execute(coordinates, direction, commands)