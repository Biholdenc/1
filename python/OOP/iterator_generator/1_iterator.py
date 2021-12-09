s = iter([1, 2, 3])
print(next(s))
print(next(s))
print(next(s))
try:
    print(next(s))
except Exception as err:
    print(err.__class__)