# Black-Jack

## Objective of game
The objective of the game is to draw a hand of card which's value does not exceed 21 (21 and under), while having hand which's accumalitive value is greater than the dealer's. Another way of winning is if the dealer draws cards which's accumalative value exceeds 21.

### Value of cards
| Card              | Value              |
| -------------     |:-------------:     |
| 2 - 10            |As indicated on card|
| Face Cards(J,Q,K) |10                  |
| Ace Cards         |1 or 11 depending on which helps the player the most                |
#### Note: Suits of cards are not counted towards any counting



### Winning Cases
* By drawing a hand value that is higher than the dealer’s hand value
* By the dealer drawing a hand value that goes over 21.
* By drawing a hand value of 21 on your first two cards, when the dealer does not.

### Losing Cases
* Your hand value exceeds 21.
* The dealers hand has a greater value than yours at the end of the round

# Models
## Card
The `card` class is a model for a single card. It has the following attribute.

`value` - This is the value of the cards which's value is used to calculate the player or the dealer's score

`face_val` - The face value of the cards represented by a single letter. Eg 'Ace' -> 'A', 
   'King' -> 'K'

`face` - Dictionary storing value for face value of cards
``` python 
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
```


### Init Method
``` python
def __init__(self, face_val):
    self.value = self.face[face_val]
    self.face_val = face_val
```
 Set the value of the card to corrosponding face value

### String representation 
``` python
def __str__(self):
    return "The Face Value of card is {face_value} \n It is worth {value} points".format(face_value=self.face_val, value=self.value)
```
Returns the properties of the card as a string

## Deck
Representation of a single cards. Stores all attributes associated with a single card

### init method
```python 
def __init__(self):
        self.deck = []
        self.populateDeck()
        self.shuffleDeck()
```
### Population of cards
``` python
def populateDeck(self):
        for card in self.deck_cards:
            self.deck.append(Card(card))
```
### Shuffling Cards
``` python
def shuffleDeck(self):
        shuffle(self.deck)
```
After the deck is populated the elements in the list are shuffled, essentially shuffling the order of cards in the deck.

### String representation
``` python
def __str__(self):
        self.ret_deck = []
        for card in self.deck:
            self.ret_deck.append(card.face_val)
        return str(self.ret_deck)
```
Returns the the face value of all cards in the deck

Sample Output:
```
['9', 'A', '7', '3', 'Q', '7', '5', '9', '5', '7', 'J', '8', '2', '2', '8', '6', '6', '4', 'K', '3', 'Q', '9', 'K', '10', '10', '2', '10', 'A', '2', '4', 'K', 'Q', 'A', '10', '6', '5', 'A', 'Q', '6', '5', 'J', '4', 'J', 'J', '3', '4', '8', '9', '8', '3', 'K', '7']
```