if __name__ == '__main__':
    file = open("day12.txt", "r")
    moves = []
    ship_x_coord = 0
    ship_y_coord = 0
    waypoint_x_coord = 10
    waypoint_y_coord = 1
    facing = 90

    for line in file:
        moves.append(line.strip("\n"))

    for individual_move in moves:

        action = individual_move[:1]
        value = int(individual_move[1:])

        if action == "F":
            ship_x_coord += waypoint_x_coord * value
            ship_y_coord += waypoint_y_coord * value

        elif action == "N":
            waypoint_y_coord += value

        elif action == "S":
            waypoint_y_coord -= value

        elif action == "E":
            waypoint_x_coord += value

        elif action == "W":
            waypoint_x_coord -= value

        # only "R" and "L" left
        else:
            # Dead Or Alive - You Spin Me Round (Like a Record) (Official Video)
            rotate = {'R': (1, -1), 'L': (-1, 1)}
            for i in range(value//90):
                waypoint_x_coord, waypoint_y_coord = \
                    waypoint_y_coord * rotate[action][0], waypoint_x_coord * rotate[action][1]

    print (abs(ship_x_coord) + abs(ship_y_coord))