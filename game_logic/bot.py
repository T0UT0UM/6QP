from game_logic.card import Card

class Bot:
    def __init__(self, name, difficulty):
        """
        Initialize a player with a name and an empty hand.

        Args:
            name (str): The name of the player.
        """
        self.name = name
        self.difficulty = difficulty
        self.hand = []
        self.penalty_points = 0

    def add_card_to_hand(self, card : Card):
        """
        Add a card to the player's hand.

        Args:
            card (Card): The card to add to the player's hand.
        """
        self.hand.append(card)
        self.hand.sort(key=lambda card: card.value)

    def play_card(self, card_value : int):
        """
        Play a card from the player's hand.

        Args:
            card_value (int): The value of the card to play.

        Returns:
            Card: The card that was played.
        """
        for i in range(len(self.hand)):
            if self.hand[i].value == card_value:
                return self.hand.pop(i)

    def choose_card(self):
        return self.hand[0].value

    def choose_row(self):
        return 1

    def __str__(self):
        """
        Return a string representation of the player's hand.
        """
        return f"{self.name}: {', '.join(str(card) for card in self.hand)}"
