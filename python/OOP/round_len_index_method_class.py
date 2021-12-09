class MyClass:
    def __init__(self, txt):
        self.name = txt

    def __str__(self):
        return self.name + 'asdfsa'

    def __len__(self):
        return len(self.name) * 100
    def __index__(self):
        p = self.name.count(' ') + 1
        return p
    def __round__(self):
        self.name = 'reset value'
        return self

txt = 'one, two, three, four, five.'

txt += '\n вышел зайчик погулять'

obj = MyClass(txt)

print(obj)

print(len(obj))
print(obj.__index__())
print(bin(obj))
print(oct(obj))
print(hex(obj))
print(round(obj))
print(obj)
