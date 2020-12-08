import math
def main(x_input, y_input):

    file = open("day3.txt", "r")
    x = 0
    y = 0
    result = 0

    for line in file:

        if y % y_input == 0:
            line = line.strip("\n")
            initial_length = len(line)
            try:
                if line[x] == "#":
                    result += 1
            except IndexError:
                line = line * math.ceil((x / initial_length))
                try:
                    if line[x] == "#":
                        result += 1
                except IndexError:
                    line = line + line
                    if line[x] == "#":
                        result += 1
            x = x + x_input
        y = y + 1

    return result

if __name__ == '__main__':
    print(main(1, 1) * main(3, 1) * main(5, 1) * main(7, 1) * main(1, 2))