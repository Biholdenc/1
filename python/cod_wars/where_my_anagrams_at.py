def anagrams(word, words):
    first = list(filter(lambda x: sorted(x) == sorted(word), words))

    return first




print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))