def move(coordinates, direction, command):
    a=0
    if command == 'f':
        a=1
        coordinates = forward(coordinates,direction,a)
    elif command == 'b':
        a=-1
        coordinates = forward(coordinates,direction,a)
    elif command == 'l':
        direction = left(direction)
    elif command == 'r':
        direction = right(direction)
    elif command == 'u':
        a=1
        direction = up(direction, a)
    elif command == 'd':
        a=-1
        direction = up(direction, a)

def forward(coordinates, direction, a):
    if direction == 'N':
        coordinates[1]=coordinates[1]+a
    elif direction == 'S':
        coordinates[1]=coordinates[1]-a
    elif direction == 'E':
        coordinates[0]=coordinates[0]+a
    elif direction == 'W':
        coordinates[0]=coordinates[0]-a
    elif direction == 'U':
        coordinates[2]=coordinates[2]+a
    elif direction == 'D':
        coordinates[2]=coordinates[2]-a
    
    return coordinates

def left(direction):
    if direction == 'N':
        direction = "W"
    elif direction == 'S':
        direction = "E"
    elif direction == 'E':
        direction = "N"
    elif direction == 'W':
        direction = "S"

    return direction

def right(direction):
    if direction == 'N':
        direction = "E"
    elif direction == 'S':
        direction = "W"
    elif direction == 'E':
        direction = "S"
    elif direction == 'W':
        direction = "N"

    return direction

def up(direction, a):
    if(a==1):
        direction = "U"
    elif(a==-1):
        direction = "D"

    return direction



