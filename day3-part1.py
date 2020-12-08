import math


def main():

    file = open("day3.txt", "r")
    x = 0
    result = 0

    for line in file:
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
        x = x + 3

    return result

if __name__ == '__main__':
    print(main())