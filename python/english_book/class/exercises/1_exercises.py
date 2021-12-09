class Investment:
    def __init__(self, principal, interest):
        self.principal = principal
        self.interest = interest
        self.value = 0

    def __str__(self):
        txt = 'Principal - ${}, Interest rate - {}%'.format(self.value, self.interest)
        return txt


    def value_after(self, n):
        self.value = self.principal * (1 + self.interest) ** n
        return self.value

x = Investment(500, 5)
x.value_after(3)
print(x)