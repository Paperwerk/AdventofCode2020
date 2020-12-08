from operator import xor


def main():

    file = open("day2.txt", "r")
    result = 0

    for line in file:
        line = line.strip('\n')
        colon_index = line.find(":")
        dash_index = line.find("-")
        letter_to_find = line[colon_index-1]

        first_position = int(line[:dash_index])
        second_position = int(''.join(i for i in line[dash_index:colon_index] if i.isdigit()))

        try:
            if xor(line[colon_index+2:][first_position-1] == letter_to_find,
                   line[colon_index+2:][second_position-1] == letter_to_find):
                result += 1
        except IndexError:
            pass

    return result


if __name__ == '__main__':
    print(main())