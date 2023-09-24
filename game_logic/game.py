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
        """
        # Find the row with the lowest value gap
        gap = 104
        
        


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
            for i in range(gc.NB_TOURS):
                player.add_card_to_hand(self.deck)

    def play(self):
        """
        Play the game.
        """
        for player in self.players:
            pass