class A:
    def __init__(self, n):
        self.nums = [0 for i in range(n)]

    def __str__(self):
        txt = '||'
        for i in self.nums:
            txt += str(i) + '||'

        return txt

obj = A(5)

print(obj)
print(A.__qualname__)