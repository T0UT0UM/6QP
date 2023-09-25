import tkinter as tk
import game_logic.game_constants as gc

class Gameboard:
    def __init__(self, game, gameboard):
        """
        Create the gameboard.

        Args:
            game (Game): The game to launch.
            gameboard (tk.Frame): The window in which the gameboard is displayed.
        """
        self.game = game
        self.gameboard = gameboard

    def display_rows(self):
        """
        Display the rows on the gameboard.
        """
        self.clear_gameboard()
        for row in self.game.gameboard.rows:
            row_frame = tk.Frame(self.gameboard)
            row_frame.pack(side=tk.TOP, fill=tk.BOTH)
            for i in range(gc.CARDS_PER_ROWS + 1):

                if i < len(row):
                    card_image = tk.PhotoImage(file="display/images/cards/"+str(row[i].value)+".png")
                elif i == gc.CARDS_PER_ROWS:
                    card_image = tk.PhotoImage(file="display/images/cards/last_card.png")
                else:
                    card_image = tk.PhotoImage(file="display/images/cards/backside.png")

                card_label = tk.Label(row_frame, image=card_image)
                card_label.image = card_image
                card_label.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, anchor='w')

            tk.Label(row_frame, text=str(self.game.gameboard.rows.index(row)+1)).pack(side=tk.LEFT)
            tk.Frame(self.gameboard, bg="black", height=2).pack(expand=True, fill=tk.X, side=tk.TOP)


    def clear_gameboard(self):
        """
        Destroy all the widgets in the gameboard.
        """
        for widget in self.gameboard.winfo_children():
            widget.destroy()
