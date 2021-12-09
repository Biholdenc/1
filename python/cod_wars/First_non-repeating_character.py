def first_non_repeating_letter(string):
    my_dict_counter = {}
    for key in string:
        my_dict_counter[key.lower()] = my_dict_counter.get(key.lower(), 0) + 1
    for key, value in my_dict_counter.items():
        if value == 1:
            for i in string:
                if i.lower() == key:
                    return i
    return ''


print(first_non_repeating_letter(''))