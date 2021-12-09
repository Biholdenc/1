class Converter:
    def __init__(self, number, unit):
        self.number = number
        self.unit = unit
        self.list_unit = {'meters': 1,
                          'centimeters': 0.01,
                          'kilometers': 1000}
    def meters(self):
        a = self.list_unit[self.unit]
        return a * self.number
    def centimeters(self):
        a = self.list_unit[self.unit]
        return a * self.number

    def kilometers(self):
        a = self.list_unit[self.unit]
        return a * self.number


c = Converter(9,'centimeters')

print(c.kilometers())