def remove_smallest(numbers):
    num = numbers[:]
    for i in range(len(num)):
        if num[i] == min(num):
            numbers.pop(i)
            break
    return num

print(remove_smallest([1, 2, 3, 4, 5]))