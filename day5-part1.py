import numpy


def main():
    def bisect(array: list):
        numpy_object = (numpy.array_split(array, 2))
        remove_numpy_object = list(list(i) for i in numpy_object)
        return remove_numpy_object

    def extract_int_from_two_chunks(two_chunks: [[], []]):
        for chunk in two_chunks:
            if len(chunk) > 0:
                return (chunk[0])

    result = []
    file = open("day5.txt", "r")
    for line in file:

        line = line.strip('\n')
        string = line[:-3]
        string2 = line[-3:]
        two_chunks = bisect(list(range(128)))

        for char in string:
            if char == "F":
                two_chunks = bisect(two_chunks[0])
            else:
                two_chunks = bisect(two_chunks[1])

        # two_chunks = [[44], []]
        row = extract_int_from_two_chunks(two_chunks)
        # row = 44

        two_chunks = bisect(list(range(8)))
        for char in string2:
            if char == "L":
                two_chunks = bisect(two_chunks[0])
            else:
                two_chunks = bisect(two_chunks[1])

        column = extract_int_from_two_chunks(two_chunks)

        result.append(row * 8 + column)

    return max(result)
if __name__ == '__main__':
    print(main())