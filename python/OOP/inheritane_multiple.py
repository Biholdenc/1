class Alpha:
    def hi():
        print('class Alpha')

class Bravo:
    def hi():
        print('class Bravo')

class Charlie:
    def hi():
        print('class Charlie')

class Delta(Alpha):
    pass

class Echo(Delta):
    pass

class Foxtrot(Bravo, Alpha):
    pass
class Test(Charlie):
    pass
class Golf(Foxtrot):
    pass

class Hotel(Charlie, Golf,  Test):
    pass

Echo.hi()
Golf.hi()
Hotel.hi()
print(Hotel.__mro__)