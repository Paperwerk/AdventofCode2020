def day8_part1(instructions: list):
    accmulator = 0
    index = 0

    state = [0]*len(instructions)

    while index < len(instructions) and state[index] == 0:
        if "nop" in instructions[index]:
            state[index] += 1
            index += 1
        elif "acc" in instructions[index]:
            accmulator += int(instructions[index][4:])
            state[index] += 1
            index += 1
        else:
            # jmp
            state[index] += 1
            index += int(instructions[index][4:])

    try:
        state[index] == 0
    # IndexError = index went beyond end of file = No Cycle
    except IndexError:
        message = "No Cycle detected"
    else:
        message = "Cycle detected"

    # example: ('Cycle detected', 'accumulator = 1832')
    return message, "accumulator = " + str(accmulator)


def day8_part2(instructions: list):
    index = 0

    while index < len(instructions):
        if instructions[index][:3] == "nop":
            instructions[index] = "jmp" + instructions[index][3:]
        elif instructions[index][:3] == "jmp":
            instructions[index] = "nop" + instructions[index][3:]

        message = (day8_part1(instructions))
        # message = ('Cycle detected', 'accumulator = 1832')
        if message[0] == "No Cycle detected":
            return message[1]

        if instructions[index][:3] == "nop":
            instructions[index] = "jmp" + instructions[index][3:]
        elif instructions[index][:3] == "jmp":
            instructions[index] = "nop" + instructions[index][3:]

        index += 1


if __name__ == '__main__':

    file = open("day8.txt", "r")
    instructions = []
    for line in file:
        instructions.append(line.strip("\n"))

    print(day8_part1(instructions))
    print(day8_part2(instructions))
