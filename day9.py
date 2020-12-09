def day9_part1(numbers):
    index = 25
    while index < len(numbers):
        subarray = numbers[index - 25:index]
        found_pairs = False
        for i in subarray:
            for i2 in subarray:
                if i + i2 == numbers[index]:
                    found_pairs = True
        if not found_pairs:
            print ("Part A solution: " + str(numbers[index]))
            return (numbers[index])
        index += 1
    return "Part A: No weakness found"


def day9_part2(array, target):
    length = len(array)
    for i in range(length):
        current_sum = array[i]
        i2 = i + 1
        while i2 <= length:
            if current_sum == target:
                return "Part B solution: " + str(max(array[i:i2]) + min(array[i:i2]))
            elif i2 == length or current_sum > target:
                break
            current_sum = current_sum + array[i2]
            i2 += 1
    return "Part B: No subarray found"

if __name__ == '__main__':
    file = open("day9.txt", "r")
    numbers = []

    for line in file:
        numbers.append(int(line.strip("\n")))

    weakness = (day9_part1(numbers))
    print(day9_part2(numbers, weakness))
