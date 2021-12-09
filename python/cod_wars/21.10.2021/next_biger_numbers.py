def next_bigger(num1):

    num = list(str(num1))

    for i in range(len(num)):
        if len(num) == i + 1:
            if num != []:
                numbers = ''.join(num)
                numbers = int(numbers)
                if numbers < num1:
                    return -1
                return num1
            return None
        num[-1 - i], num[-1 - i - 1] = num[-1 - i - 1], num[-1 - i]
        numbers = ''.join(num)
        numbers = int(numbers)
        if num1 < numbers:
            return numbers



print(next_bigger(1))