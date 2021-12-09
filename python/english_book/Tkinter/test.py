from math import pow

def minor(m1):
    if len(m1) == 1:
        return m1[0][0]
    first = 1
    second = 1
    for i in range(len(m1)):
        for j in range(len(m1[i])):
            if j == i:
                first *= m1[i][j]
            elif i == len(m1) - 1 - j:
                second *= m1[i][j]
    return first - second
def det(matrix):
    all_number = []
    if len(matrix) <= 2:
        return minor(matrix)
    numbers_in_matrix = matrix[:]
    for k in range(len(numbers_in_matrix)):
        num = numbers_in_matrix[0][k]
        my_list = []


        for i in range(len(matrix)):

            new = []
            for j in range(len(matrix[i])):
                if i != 0 and j != k:
                    new.append(matrix[i][j])
            if new != []:
                my_list.append(new)
        all_number.append((num * pow(-1, k)) * minor(my_list))
    return sum(all_number)


print(det([[2,5,3], [1,-2,-1], [1, 3, 4]]))
