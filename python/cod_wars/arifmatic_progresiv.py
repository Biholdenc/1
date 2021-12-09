def find_missing(sequence):
    first = sequence[1] - sequence[0]
    second = sequence[-1] - sequence[-2]
    if first > second:
        first = second
    if first < second or first == second:
        for i in range(-1, -len(sequence) - 1, -1):
            if sequence[i] - sequence[i - 1] == first:
                continue
            else:
                return sequence[i] - first




print(find_missing([1, 3, 4, 5, 6, 7, 8, 9]))