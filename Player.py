from Deck import Deck

class Player:
    def __init__(self):
        self.hand = []

    def drawCard(self, deck):
        self.hand.append(deck.drawCard())

    def returnCard(self, deck, value, suite):
        suites = ["Spade", "Club", "Diamond", "Heart"]
        cardNum = range(1, 14)
        index = -1

        if value in cardNum:
            if suite in suites:
                for i in range(len(self.hand)):
                    if self.hand[i].getValue() == value and self.hand[i].getSuite().upper() == suite.upper():
                        index = i
                if index == -1:
                    print("Card not found in hand!")
                else:
                    self.hand[index].printCard()
                    print("The card has been returned to the deck!")
                    deck.returnCard(self.hand.pop(index))
            else:
                print("Incorrect suite!")
        else:
            print("Value out of bounds!")

    def showHand(self):
        for card in self.hand:
            card.printCard()

if __name__ == "__main__":
    p1 = Player()
    deck = Deck()
    #deck.shuffleDeck()
    #deck.printDeck()
    p1.drawCard(deck)
    p1.drawCard(deck)
    p1.drawCard(deck)
    p1.showHand()
    print("")
    p1.returnCard(deck, 13, "Diamond")
    print("")
    p1.showHand()
    print("")
    deck.printTopCard()

