import numpy as np
import game_constants as gc
from card import *

class Gameboard:
    def __init__(self, deck):
        """
        Initialize a gameboard with a deck.

        Args:
            deck (Deck): The deck from which to draw cards.
        """
        self.rows = [[], [], [], []]
        self.deck = deck

        #Initialize the gameboard with 4 cards
        for i in range(gc.NB_ROWS):
            self.rows[i].append(self.deck.draw())

    def add_card(self, card):
        """
        Add a card to the gameboard, the card is added to the row with the lowest value gap.

        Args:
            card (Card): The card to add to the gameboard.
        Returns:
            penalty (int): The number of penalty points the player gets for adding the card.
        """
        # Find the row with the lowest value gap
        gap = gc.NB_CARDS
        row = -1
        for i in range(gc.NB_ROWS):
            temp = card.value - self.rows[i][-1].value
            if 0 < temp < gap:
                gap = temp
                row = i

        # If the card valus is lower than every last card in the rows
        if row == -1:
            return -1

        # Add the card to the row
        penalty = 0
        if (len(self.rows[row]) < gc.CARDS_PER_ROWS):
            self.rows[row].append(card)
        else:
            for i in range(gc.CARDS_PER_ROWS):
                penalty += self.rows[row].pop().bullheads
            self.rows[row].append(card)
        return penalty

    def replace_row(self, row_number, card):
        """
        Replace a row with a new card.

        Args:
            row_number (int): The number of the row to replace.
            card (Card): The card to replace the row with.

        Returns:
            penalty (int): The number of penalty points the player gets for replacing the row.
        """
        penalty = 0
        for i in range(len(self.rows[row_number])):
            penalty += self.rows[row_number].pop().bullheads
        self.rows[row_number].append(card)
        return penalty


class Game:
    def __init__(self, players):
        """
        Initialize a game with a list of players.

        Args:
            players (list): The list of players.
        """
        self.players = players
        self.deck = Deck()
        self.gameboard = Gameboard(self.deck)

        # Initialize the players' hands
        for player in self.players:
            for i in range(gc.NB_TURNS):
                player.add_card_to_hand(self.deck)

    def play(self):
        """
        Play the game.
        """
        for player in self.players:
            pass