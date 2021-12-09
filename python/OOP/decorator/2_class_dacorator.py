def F(A):
    class Alpha(A):
        def hi(self):
            print('Класс Alpha!')
    return Alpha

def Q(A):
    class Bravo(A):
        def hi(self):
            print('Класс Bravo!')
    return Bravo

@F
class First:
    def hello(self):
        print('класс First')

@F
class Second:
    def hello(self):
        print('класс second')

@Q
@F
class Third:
    def hello(self):
        print('Класс Third!')

def show_obj(obj):
    print('класс экземпляра:', obj.__class__)
    obj.hi()
    obj.hello()

def show_class(A):
    print('имя класса:', A.__name__)
    print('Базовый класс:', A.__bases__)
    print('цепочка наследования:', A.__mro__)

one = First()
two = Second()
three = Third()
print('Экземпляры классов.')
for obj in [one, two, three]:
    show_obj(obj)

for A in [First, Second, Third]:
    show_class(A)
