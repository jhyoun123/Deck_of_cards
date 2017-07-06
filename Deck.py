import random

class Card(object):
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
class Deck(object):
    def __init__(self):
        self.deck = []
        self.addSuit('s').addSuit('h').addSuit('d').addSuit('c')

    def addSuit(self, suit):
        for i in range(1, 14):
            if (i == 1):
                self.deck.append(Card(suit, 'A'))
            elif (i == 11):
                self.deck.append(Card(suit, 'J'))
            elif (i == 12):
                self.deck.append(Card(suit, 'Q'))
            elif (i == 13):
                self.deck.append(Card(suit, 'K'))
            else: 
                self.deck.append(Card(suit, i))
        return self

    def displayDeck(self):
        for i in range(0, len(self.deck)):
            print "Suit: " + self.deck[i].suit + ", Value: " + str(self.deck[i].value)


    def add(self):
        rand = random.randint(0, 51)
        print self.deck[rand].suit, self.deck[rand].value
        return self

class Player(object): 
    def __init__(self, name):
        self.name = name
        self.hand = []
    def drawCard(self, deck):
        rand = random.randint(0, len(deck.deck) - 1)
        self.hand.append(deck.deck[rand])
        del deck.deck[rand]
        return self

    def discardCard(self, deck):
        card = self.hand.pop()
        deck.deck.append(card)
        return self

    def shuffleDeck(self, deck):
        for i in range(0, 100):
            self.drawCard(deck)
            self.discardCard(deck)

    def displayHand(self):
        for i in range(0, len(self.hand)):
            print "Suit: " + self.hand[i].suit + ", Value: " + str(self.hand[i].value)

deck1 = Deck()
player1 = Player("Ray")


# deck1.addSuit('s').addSuit('h').addSuit('d').addSuit('c')
# player1.drawCard(deck1).drawCard(deck1).drawCard(deck1).drawCard(deck1).drawCard(deck1)
print deck1.displayDeck()
# player1.displayHand()
# player1.discardCard(deck1).discardCard(deck1)
# player1.displayHand()
# print
# print deck1.displayDeck()
player1.shuffleDeck(deck1)
print deck1.displayDeck()
