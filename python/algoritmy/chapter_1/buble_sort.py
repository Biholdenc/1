my_list = [5,7,8,4,3,47,7,9,87,7,97,45,1,47,8,]

for i in range(0, len(my_list)):
        for j in range(0, len(my_list) - i - 1):

            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp


print(my_list)