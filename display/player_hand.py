import tkinter as tk

import game_logic.game_constants as gc

# Define paths
CARD_IMAGES_PATH = "display/images/cards"
BACKSIDE_IMAGE_PATH = f"{CARD_IMAGES_PATH}/backside.png"

def display_welcome_player_hand(player_hand_frame):
    """
    Display the welcome player hand.

    Args:
        player_hand_frame (tk.Frame): The frame to display the player hand. 
    """
    for i in range(gc.NB_TURNS):
        card_image = tk.PhotoImage(file=BACKSIDE_IMAGE_PATH)
        card_label = tk.Label(player_hand_frame, image=card_image)
        card_label.image = card_image
        card_label.grid(row=0, column=i, padx=3, pady=5)
