def increment_string(a):
    for i in range(len(a)):
        if a[i].isdigit():
            counter = 0
            old_len_string = len(a[i:])
            new_string = int(a[i:]) + 1
            for k in a[i:]:
                if k in '123456789':
                    break
                else:
                    counter += 1
            zero_counter = old_len_string - len(str(new_string))
            if counter == zero_counter:
                return a[:i] + counter * '0' + str(new_string)
            else:
                return a[:i] + (counter - 1) * '0' + str(new_string)
    return a + '1'




print(increment_string("foobar00099"))