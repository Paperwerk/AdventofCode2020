if __name__ == '__main__':
    file = open("day12.txt", "r")
    moves = []
    x_coord = 0
    y_coord = 0
    # only valid values 0, 90, 180, 270
    # initially facing east = 90
    facing = 90

    for line in file:
        moves.append(line.strip("\n"))

    for individual_move in moves:

        action = individual_move[:1]
        value = int(individual_move[1:])

        # so that it can only be valid values of 0, 90, 180, 270
        while facing >= 360:
            facing -= 360
        while facing < 0:
            facing += 360

        if action == "F":
            if facing == 90:
                x_coord += value
            elif facing == 180:
                y_coord -= value
            elif facing == 270:
                x_coord -= value
            elif facing == 0:
                y_coord += value
            else:
                print ("bug found")

        elif action == "N":
            y_coord += value

        elif action == "S":
            y_coord -= value

        elif action == "E":
            x_coord += value

        elif action == "W":
            x_coord -= value

        elif action == "L":
            facing -= value

        else:
            # else "R"
            facing += value

    print (abs(x_coord) + abs(y_coord))