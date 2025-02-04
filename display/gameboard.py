import tkinter as tk

import game_logic.game_constants as gc

# Define paths
CARD_IMAGES_PATH = "display/images/cards"
BACKSIDE_IMAGE_PATH = f"{CARD_IMAGES_PATH}/backside.png"
EMPTY_CARD_IMAGE_PATH = f"{CARD_IMAGES_PATH}/empty_card.png"
LAST_CARD_IMAGE_PATH = f"{CARD_IMAGES_PATH}/last_card.png"

def display_welcome_gameboard(gameboard_frame):
    """
    Display the welcome gameboard.

    Args:
        gameboard_frame (tk.Frame): The frame to display the gameboard.
    """
    # Create labels for each row in the gameboard
    for row_number in range(gc.NB_ROWS):
        for i in range(gc.CARDS_PER_ROWS + 1):
            if i == 0:
                card_image = tk.PhotoImage(file=BACKSIDE_IMAGE_PATH)
            elif i <= gc.CARDS_PER_ROWS - 1:
                card_image = tk.PhotoImage(file=EMPTY_CARD_IMAGE_PATH)
            else:
                card_image = tk.PhotoImage(file=LAST_CARD_IMAGE_PATH)
            card_label = tk.Label(gameboard_frame, image=card_image)
            card_label.image = card_image  # Keep a reference to prevent garbage collection
            card_label.grid(row=row_number, column=i, padx=3, pady=5)
            
def display_gameboard(gameboard_frame, game):
    """
    Display the gameboard.

    Args:
        gameboard_frame (tk.Frame): The frame to display the gameboard.
        game (Game): The game to display.
    """
    # Clear the gameboard
    for widget in gameboard_frame.winfo_children():
        widget.destroy()
    
    # Create labels for each row in the gameboard
    for row_number in range(gc.NB_ROWS):
        for i in range(gc.CARDS_PER_ROWS + 1):
            if i < len(game.gameboard.rows[row_number]):
                card_image = tk.PhotoImage(file=f"{CARD_IMAGES_PATH}/{game.gameboard.rows[row_number][i].value}.png")
            elif i == gc.CARDS_PER_ROWS:
                card_image = tk.PhotoImage(file=LAST_CARD_IMAGE_PATH)
            else:
                card_image = tk.PhotoImage(file=EMPTY_CARD_IMAGE_PATH)
            card_label = tk.Label(gameboard_frame, image=card_image)
            card_label.image = card_image  # Keep a reference to prevent garbage collection
            card_label.grid(row=row_number, column=i, padx=3, pady=5)
            
    # Create labels for the row numbers
    for i in range(gc.NB_ROWS):
        row_number_label = tk.Label(gameboard_frame, text=str(i+1))
        row_number_label.grid(row=i, column=gc.CARDS_PER_ROWS + 1, padx=3, pady=5)
        
    # Create a separator between each row
    for i in range(gc.NB_ROWS):
        separator = tk.Frame(gameboard_frame, bg="black", height=2)
        separator.grid(row=i, column=0, columnspan=gc.CARDS_PER_ROWS + 2, sticky="ew")
