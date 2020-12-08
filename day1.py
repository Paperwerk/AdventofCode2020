def main():
    file = open("day1.txt", "r")
    numbers = []
    for line in file:
        numbers.append(int(line.strip('\n')))

    for i in numbers:
        for i2 in numbers:
            for i3 in numbers:
                if i + i2 + i3 == 2020:
                    return (i * i2 * i3)

    return 0


if __name__ == '__main__':
    print(main())