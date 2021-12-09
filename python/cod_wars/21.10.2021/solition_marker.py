def solution(string, marker):
    import codecs
    my_string = repr(string)
    new_string = ''
    a = '\\'

    i = 0
    while True:
        if my_string[i] in marker:
            new_string = new_string.strip()

            while my_string[i] != a:
                if i == len(my_string) - 1:
                    return codecs.decode(new_string[1:], 'unicode_escape')

                i += 1
        else:
            if i == len(my_string) - 1:
                return codecs.decode(new_string[1:], 'unicode_escape')
            new_string += my_string[i]
            i += 1











print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))