class Card:
    def __init__(self, value, suite, visible):
        self.value = value
        self.suite = suite
        self.visible = visible

    def getValue(self):
        if self.visible:
            return self.value

    def getSuite(self):
        if self.visible:
            return self.suite

    def printCard(self):
        if self.visible:
            value = self.value
            if value == 1:
                value = "Ace"
            elif value > 10:
                picture = ["Jack", "Queen", "King"]
                value = picture[value-11]

            print("{} of {}".format(value, self.suite))
        else:
            print("Card is hidden!")

    def hideCard(self):
        self.visible = False

    def unhideCard(self):
        self.visible = True
