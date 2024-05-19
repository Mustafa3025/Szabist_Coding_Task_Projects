"""


This module contains code from

Think Python: an Introduction to Software Design

Allen B. Downey


"""


from Card import *


class PokerHand(Hand):

    

    def suit_hist(self):

        """build a histogram of the suits that appear in the hand"""

        self.suits = {}

        for card in self.cards:

            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1


    def has_flush(self):

        """return True if the hand has a flush, False otherwise"""

        self.suit_hist()

        for val in self.suits.values():

            if val >= 5:

                return True

        return False
    
    def has_pairs(self):
        self.rank = {}
        
        for card in self.cards:
            self.rank[card.rank] = self.ranks.get(card.rank, 0) + 1
        for val in self.ranks.values():
            if val == 2:
                return True
        return False

    def has_two_pairs(self):
        pairs = 0
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1
        for val in self.ranks.values():
            if val == 2:
                pairs += 1
        return pairs == 2

    def classify(self):
        if self.has_flush():
            self.label = "Flush"
        elif self.has_two_pairs():
            self.label = "Two Pairs"
        elif self.has_pairs():
            self.label = "Pairs"
        else:
            self.label = "None"


if __name__ == '__main__':

    deck = Deck()
    deck.shuffle()


    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print(hand)
        print(hand.has_flush())
        print()




