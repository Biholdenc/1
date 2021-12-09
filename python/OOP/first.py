class My:

    def set(self, n):
        print('Пробую что то сделать.')
        self.numbers = n
        
    def get(self):
        print('вроде получилось вывести или нет', self.numbers)

test = My()

test.set(8)
test.get()
