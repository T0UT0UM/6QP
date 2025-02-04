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

def display_player_hand(player_hand_frame, player):
    """
    Display the player hand.

    Args:
        player_hand_frame (tk.Frame): The frame to display the player hand.
        player (Player): The player to display.
    """
    # Clear the player hand
    for widget in player_hand_frame.winfo_children():
        widget.destroy()
    
    # Create labels for each card in the player hand
    for i in range(len(player.hand)):
        card_image = tk.PhotoImage(file=f"{CARD_IMAGES_PATH}/{player.hand[i].value}.png")
        card_label = tk.Label(player_hand_frame, image=card_image)
        card_label.image = card_image
        card_label.grid(row=0, column=i, padx=3, pady=5)
        
def choose_card(toolbar_frame, player):
    """
    Choose a card from the player hand.

    Returns:
        card_value (int): The value of the chosen card.
    """
    for widget in toolbar_frame.winfo_children():
        widget.destroy()
    
    tk.Label(toolbar_frame, text="Choose a card:").pack(side=tk.LEFT)
    card_value = tk.Entry(toolbar_frame)
    card_value.pack(side=tk.LEFT)
    card_value.focus_set()
    def on_click():
        nonlocal card_value
        card_value = card_value.get()
        print(card_value)
        return card_value
    tk.Button(toolbar_frame, text="OK", command=on_click).pack(side=tk.LEFT)
    

def choose_row(toolbar_frame):
    """
    Choose a row to replace.

    Returns:
        row_number (int): The number of the row to replace.
    """
    for widget in toolbar_frame.winfo_children():
        widget.destroy()
    
    tk.Label(toolbar_frame, text="Choose a row:").pack(side=tk.LEFT)
    row_number = tk.Entry(toolbar_frame)
    row_number.pack(side=tk.LEFT)
    row_number.focus_set()
    def on_click():
        nonlocal row_number
        row_number = row_number.get()
        print(row_number)
        return row_number
    tk.Button(toolbar_frame, text="OK", command=on_click).pack(side=tk.LEFT)
