def pig_it(text):
    new_list = [i if i in '!?' else i[1:] + i[0] + 'ay' for i in text.split()]
    return ' '.join(new_list)


print(pig_it('O tempora o mores ?'))