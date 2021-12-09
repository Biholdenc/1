class Alpha:
    def hello():
        pass

    class Bravo:
        pass

class Charlie(Alpha):
    pass

class Delta(Charlie):
    pass

obj = Alpha()

print('fields __class__')
print('instance obj:', obj.__class__)
print('class Alpha:', Alpha.__class__)
print('class Alpha.Bravo:', Alpha.Bravo.__class__)
print('class Charlie:', Charlie.__class__)

print('\n fields __bases__ and __mro__')
print('class Delta, fields __bases__:', Delta.__bases__)
print('class Delta, fields __mro__:', Delta.__mro__)
print('class Alpha, fields __bases__:', Alpha.__bases__)
print('class Alpha, fields __mro__:', Alpha.__mro__)

print('\n fields __doc__')
print('class description Alpha:', Alpha.__doc__)
Delta.__doc__ = 'class Delta inheriten class Charlie'
print('class description Delta:', Delta.__doc__)

print('\n fields __module__')
print('module class Alpha:', Alpha.__module__)

print('\n fields __dict__')
print('attribute class Alpha:', Alpha.__dict__)
print('attribute class Delta:', Delta.__dict__)

print('\n fields __name__ and __qualname__')
print('class Alpha, fields __name__:', Alpha.__name__)
print('class Alpha, field __qualname__:', Alpha.__qualname__)
print('class Alpha.Bravo, fields __name__:', Alpha.Bravo.__name__)
print('class Alpha.Bravo, fields __qualname__:', Alpha.Bravo.__qualname__)
print('class Delta, fields __name__:', Delta.__name__)
print('class Delta, fields __qualname__:', Delta.__qualname__)

