from random import shuffle
class Card:
    """Representation of a single cards. Stores all attributes associated with a single card"""
    face = {'A':1,
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9,
            '10':10,
            'J':10,
            'Q':10,
            'K':10}
    def __init__(self, face_val):
        self.value = self.face[face_val]
        self.face_val = face_val
    
    def __str__(self):
        return "The Face Value of card is {face_value} \n It is worth {value} points".format(face_value=self.face_val, value=self.value)


class Deck:
    """Representation of a deck hoding in total 52 cards in random order without suits"""
    
    deck_cards = ['A','2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
                  'A','2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
                  'A','2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',
                  'A','2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K',]

    def __init__(self):
        self.deck = []
        self.populateDeck()
        self.shuffleDeck()

    def populateDeck(self):
        for card in self.deck_cards:
            self.deck.append(Card(card))
    
    def shuffleDeck(self):
        shuffle(self.deck)
    
    def drawCard(self):
        return self.deck.pop()

    def __str__(self):
        self.ret_deck = []
        for card in self.deck:
            self.ret_deck.append(card.face_val)
        return str(self.ret_deck)
        

deck = Deck()
print(deck)



         