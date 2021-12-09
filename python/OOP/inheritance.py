class BaseClass:
    name = 'Поле name'

    def say(self):
        print("Метод say()")


class NewClass(BaseClass):
    pass

obj = NewClass()
print(NewClass.name)
obj.say()

def hello(self):
    print('new method hello()')
    
BaseClass.say = hello

BaseClass.name = 'new value fild name'
print(NewClass.name)
obj.say()