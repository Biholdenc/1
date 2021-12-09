import random
from random import shuffle

class StandartDeck:
    def __init__(self):
        self.names = {'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
        self.suit = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = []

        for key in self.suit:
            for value in range(6, 15):
                self.cards.append(dict([(key, value)]))

    def t(self):
        pass

class FirstPlayer(StandartDeck):
    def __init__(self):
        StandartDeck.__init__(self)

        self.my_cards = []
    def f(self):
        pass

x = StandartDeck()
y = FirstPlayer()
random.shuffle(x.cards)
print(x.cards)
print(y.cards)
