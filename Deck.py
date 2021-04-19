from Card import Card
import random

class Deck:
    def __init__(self):
        self.suites = ["Spade", "Club", "Diamond", "Heart"]
        self.cardNum = range(1, 14)
        self.deck = []
        self.buildDeck()

    def buildDeck(self):
        for value in self.cardNum:
            for suite in self.suites:
                self.deck.append(Card(value, suite, True))

    def shuffleDeck(self):
        for i in range(len(self.deck)):
            r = random.randint(0, i)
            self.deck[i], self.deck[r] = self.deck[r], self.deck[i]

    def hideAllCards(self):
        for card in self.deck:
            card.hideCard()

    def showAllCards(self):
        for card in self.deck:
            card.showCard()

    def drawCard(self):
        return self.deck.pop()

    def returnCard(self, card):
        self.deck.append(card)

    def printTopCard(self):
        if len(self.deck) > 0:
            self.deck[-1].printCard()
        else:
            print("Deck is empty!")

    def printDeck(self):
        for card in self.deck:
            card.printCard()
