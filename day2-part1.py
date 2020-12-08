def main():

    file = open("day2.txt", "r")
    result = 0

    for line in file:
        line = line.strip('\n')
        colon_index = line.find(":")
        dash_index = line.find("-")
        letter_to_find = line[colon_index-1]
        count = 0

        minimum = int(line[:dash_index])
        maximum = int(''.join(i for i in line[dash_index:colon_index] if i.isdigit()))

        for letter in line[colon_index:]:
            if letter == letter_to_find:
                count += 1

        if minimum <= count <= maximum:
            result += 1

    return result

if __name__ == '__main__':
    print(main())