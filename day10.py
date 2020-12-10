def day10_part2(devices):
    jolt_dict = {}

    # So now we have a dict of all the possible {joltages:number_of_combinations}
    for i in range(max(devices)):
        jolt_dict[i] = 0

    # Base case, only one way to add the device
    # The twist is that we pop (i.e. start from the highest jolt device)
    charger = devices.pop()
    jolt_dict[charger] = 1

    # Since we are starting from the highest jolt device, we reverse the dict
    for i in reversed(devices):
        # Just rip this off from https://leetcode.com/problems/climbing-stairs/
        jolt_dict[i] = jolt_dict[i+1] + jolt_dict[i+2] + jolt_dict[i+3]

    return jolt_dict[0]


def day10_part1(devices):

    devices.sort()

    jolt = 0
    count_one_jolt = 0
    count_two_jolts = 0
    count_three_jolts = 0
    # "your device's built-in adapter is always 3 higher than the highest adapter"
    while jolt < max(devices)+3:
        if jolt + 1 in devices:
            jolt += 1
            count_one_jolt += 1
        elif jolt + 2 in devices:
            jolt += 2
            count_two_jolts += 1
        else:
            jolt += 3
            count_three_jolts += 1

    return (count_one_jolt * count_three_jolts)


if __name__ == '__main__':
    file = open("day10.txt", "r")
    devices = []

    for line in file:
        devices.append(int(line.strip("\n")))

    print (day10_part1(devices))
    # "your device's built-in adapter is always 3 higher than the highest adapter"
    devices.append(max(devices)+3)
    devices.insert(0, 0)
    print (day10_part2(devices))
