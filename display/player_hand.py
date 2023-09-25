import tkinter as tk
import game_logic.game_constants as gc

class Player_hand:
    def __init__(self, game, player_frame):
        """
        Create the player hand zone.
        """
        self.game = game
        self.player_frame = player_frame

    def display_hand(self):
        """
        Display the player hand.
        """
        self.clear_hand_zone()
        for card in self.game.players[0].hand:
            card_image = tk.PhotoImage(file="display/images/cards/"+str(card.value)+".png")
            card_label = tk.Label(self.player_frame, image=card_image)
            card_label.image = card_image
            card_label.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, anchor='w')

    def clear_hand_zone(self):
        """
        Destroy all the widgets in the player hand zone.
        """
        for widget in self.player_frame.winfo_children():
            widget.destroy()

    def get_card(self, event):
        """
        Play a card from the player's hand.

        Returns:
            card_value (int): The value of the card to play.
        """
        # Get the card value from the image name
        card_value = int(event.widget.image.cget("file").split("/")[-1].split(".")[0])
        # Play the card
        self.game.players[0].play_card(card_value)
        # Display the hand
        self.display_hand()
        # Display the rows
        self.game.gameboard.display_rows()
        # If the game is over
        if self.game.gameboard.is_game_over():
            # End the game
            self.game.end_game()
        # Else, the player has to play a card
        else:
            self.game.players[0].add_card_to_hand(self.game.deck)
            self.display_hand()
            self.game.gameboard.display_rows()
        return card_value
