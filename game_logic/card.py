import random

class Card:
    def __init__(self, value):
        """
        Initialize a card with a numeric value and the number of bullheads it contains.
        
        Args:
            value (int): The numeric value of the card.
            bullheads (int): The number of bullheads on the card.
        """
        assert 1 <= value <= 104, "Card value must be between 1 and 105"
        self.value = value

        if (value % 55 == 0):
            self.bullheads = 7

        elif(value % 11 == 0):
            self.bullheads = 5

        elif (value % 10 == 0):
            self.bullheads = 3

        elif (value % 10 == 5):
                self.bullheads = 2
        else:
            self.bullheads = 1

    def __str__(self):
        """
        Return a string representation of the card, e.g., "7 (1*)".
        """
        return f" |{self.value:3d}(*{self.bullheads}*)| "

 

class Deck:
    def __init__(self):
        """
        Initialize a deck of cards with values ranging from 1 to 104.
        """
        self.cards = [Card(value) for value in range(1, 105)]
        random.shuffle(self.cards)

    def draw(self):
        """
        Draw one card from the deck.

        Returns:
            list: The drawn card.
        """
        assert len(self.cards) > 0, "Cannot draw from an empty deck"
        return self.cards.pop()
