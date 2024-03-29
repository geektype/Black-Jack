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

class Player:
    """Representation of a basic player in Black Jack """

    def __init__(self, deck):
        self.hand = []
        self.deck = deck
        self.points = 0
    
    def hit(self):
        self.card = self.deck.drawCard()
        self.hand.append(self.card)
        self.updateScore()
        
    def updateScore(self):
        hand = self.showHandVal()
        if 'A' in hand:
            while 'A' in hand:
                int_array = []
                ace_array = []
                for card in hand:
                    if card == 'A':
                        ace_array.append(card)
                    else:
                        int_array.append(card)
                
                ace_count = len(ace_array)
                int_sum = abs(sum(int_array)-21)
                
                if int_sum > ((ace_count-1)+10):
                    hand[hand.index('A')] = 11

                else:
                    hand[hand.index('A')] = 1
        self.points = sum(hand)
            
    def showHand(self):
        ret_hand = []
        for card in self.hand:
            ret_hand.append(card.face_val)
        return ret_hand
    def showHandVal(self):
        ret_hand = []
        for card in self.hand:
            if card.face_val == 'A':
                ret_hand.append('A')
            else:
                ret_hand.append(card.value)
        return ret_hand
    
    def value_of_ace(self):
        if self.points + 11 > 21:
            return 1
        else:
            return 11
    
    def __str__(self):
        return """
            Player Hand: {hand} \n
            Player Points: {points}
                """.format(hand=self.showHand(), points=self.points)
deck = Deck()
p = Player(deck)

print(p)
p.hit()
p.hit()
p.hit()
print(p)




