def main():
    file = open("day6.txt", "r")

    set_of_chars = set()
    count = 0

    for line in file:
        line = line.strip("\n")
        if line != "":
            for char in line:
                if char not in set_of_chars:
                    set_of_chars.add(char)
        else:
            for key in set_of_chars:
                count += 1

            set_of_chars = set()

    for key in set_of_chars:
        count += 1

    return count

if __name__ == '__main__':
    print(main())