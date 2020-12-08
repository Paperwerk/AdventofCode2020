def main():
    file = open("day6.txt", "r")

    dict = {}
    # number_of_lines = number of people
    number_of_lines = 0
    count = 0

    for line in file:
        line = line.strip("\n")
        if line != "":
            number_of_lines += 1
            for char in line:
                if char not in dict:
                    dict[char] = 1
                else:
                    dict[char] += 1
        else:
            for key in dict:
                # Since number_of_lines = number of people,
                # any key that has a value of number_of_lines is something that everyone answered yes to
                if dict[key] == number_of_lines:
                    count += 1

            number_of_lines = 0
            dict = {}

    # Need to repeat this off loop because off by one errors
    for key in dict:
        if dict[key] == number_of_lines:
            count += 1

    return (count)

if __name__ == '__main__':
    print(main())