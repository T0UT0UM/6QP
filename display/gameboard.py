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
