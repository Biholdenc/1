
def bread(func):
    def wrapper():
        print('pomidor')
        func()
        print('salt')
    return wrapper


@bread
def sandwich():
    print('vetchina')

sandwich()

