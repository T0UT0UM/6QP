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
            card_label.card_value = card.value
            card_label.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, anchor='w')

    def clear_hand_zone(self):
        """
        Destroy all the widgets in the player hand zone.
        """
        for widget in self.player_frame.winfo_children():
            widget.destroy()

    def get_card(self):
        """
        Ask the player to click on a card from their deck and return the card value.
        """
        card_value = None
        def on_click(event):
            nonlocal card_value
            card_value = event.widget.card_value
            print(card_value)
            event.widget.master.quit()
        for widget in self.player_frame.winfo_children():
            widget.bind("<Button-1>", on_click)
        self.player_frame.update()
        return card_value

    def choose_row(self):
        """
        Choose a row to replace.

        Returns:
            row_number (int): The number of the row to replace.
        """
        pass
