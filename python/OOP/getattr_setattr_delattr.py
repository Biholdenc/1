class MyClass:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __setattr__(self, attr, val):
        if attr == 'name':
            self.__dict__[attr] = val
        else:
            print("Операцыя не разрешина")

    def __getattr__(self, attr):
        return 'такого поля нет!'

    def __delattr__(self, attr):
        print('удалять поля запрещено!')

obj = MyClass('исходное значение')
print(obj)
obj.name = 'новое значение'
print(obj)
obj.number = 100
print(obj.number)
del obj.name
print(obj)
