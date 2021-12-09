def f(a):

    return sum(map(int, list(a)))

def order_weight(strng):
    strng = sorted(strng.split())
    return ' '.join(sorted(strng, key=f))


print(order_weight('2000 11 11 10003 22 123 1234000 44444444 9999'))