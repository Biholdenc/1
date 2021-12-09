s = [1, 2, 3].__iter__()
print(s.__next__())
print(s.__next__())
print(s.__next__())

try:
    print(s.__next__())
except Exception as err:
    print(err.__class__)