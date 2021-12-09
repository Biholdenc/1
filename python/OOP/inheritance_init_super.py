class BaseClass:
    def __init__(self, num):
        self.id = num
    def get(self):
        print('id:', self.id)

    def show(self):
        print('field instance base class')
        self.get()

class NewClass(BaseClass):
    def __init__(self, num, txt):
        super().__init__(num)
        self.name = txt

    def get(self):
        super().get()
        print('Name:', self.name)

obj_base = BaseClass(1)
print('call method show() in instance obj_base:')

obj_base.show()
obj_new = NewClass(10, 'ten')
print('call method show() in instance obj_new:')
obj_new.show()
