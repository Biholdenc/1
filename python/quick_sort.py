import random

list = [12,45,78,321,4,6544,456,87,78]

def quick_sort(my_list):

    if len(my_list) < 2:
        return my_list
    pow = my_list[0]
    right = [i for i in my_list if i > pow]
    middle = [i for i in my_list if i == pow]
    left = [i for i in my_list if i < pow]

    return quick_sort(left) + middle + quick_sort(right)
print(quick_sort(list))