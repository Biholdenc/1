def josephus_survivor(n,k):
    my_list = [i for i in range(1, n + 1)]
    counter = 1
    i = 0
    while len(my_list) != 1:
        if counter == k:
            my_list.pop(i)
            counter = 1
        elif i + 1 == len(my_list):
            i = 0
            counter += 1
        elif i == len(my_list):
            i = 0
            i += 1
            counter += 1

        else:
            i += 1
            counter += 1
    return my_list[0]



def josephus_survivor(n, k):
    s = 0
    for i in range(1, n + 1):
        s = (s + k) % i
    return s + 1

print(josephus_survivor(7, 5))



print(josephus_survivor(2,1))