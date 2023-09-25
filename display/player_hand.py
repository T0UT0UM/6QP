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

    def get_card(self):
        """
        Play a card from the player's hand.

        Returns:
            card_value (int): The value of the card to play.
        """
        # ask the player to click with the cursor on one of its card
        # return the value of the card
        card_value = 0

        def on_click(event):
            global card_value
            card_value = int(event.widget.image.cget("file").split("/")[-1].split(".")[0])
            print(card_value)

        self.player_frame.bind("<Button-1>", on_click)
        # wait for the player to click on a card
        while card_value == 0:
            self.player_frame.update()
        self.player_frame.unbind("<Button-1>")
        return card_value

    def on_click(self, event):
        global card_value
        card_value = int(event.widget.image.cget("file").split("/")[-1].split(".")[0])
        print(card_value)
