import tkinter as tk
from tkinter import messagebox

# Import game logic
from game_logic.card import Card, Deck
from game_logic.player import Player
from game_logic.game import Game
import game_logic.game_constants as gc

# Import display
from display.gameboard import *
from display.player_hand import *


# Define paths
CARD_IMAGES_PATH = "display/images/cards"
WELCOME_IMAGE_PATH = "display/images/welcome.png"

def Menu():

    # Initialize main application window
    window = tk.Tk()
    window.title("6 qui prend!")
    window.resizable(False, False)
    window_dim = (170 + 86*max(gc.NB_TURNS, gc.CARDS_PER_ROWS + 1), 130*gc.NB_ROWS + 130)
    window.geometry(f"{window_dim[0]}x{window_dim[1]}")
    
    # Elements of the main window
    toolbar_frame = tk.Frame(window, bg="#f0f0f0")
    gameboard_frame = tk.Frame(window, bg="white")
    player_hand_frame = tk.Frame(window, bg="lightgrey")

    # Load welcome image
    welcome_photo = tk.PhotoImage(file=WELCOME_IMAGE_PATH)
    welcome_label = tk.Label(window, image=welcome_photo)
    welcome_label.pack(expand=True)

    def show_main_menu(event=None):
        # Clear the window
        welcome_label.destroy()
        
        # Clear the toolbar frame
        for widget in toolbar_frame.winfo_children():
            widget.destroy()

        # Toolbar section
        toolbar_frame.place(relheight=1, width=170, rely=0, relx=0)

        # Gameboard section
        gameboard_dim = (86*gc.CARDS_PER_ROWS, 130*gc.NB_ROWS)
        gameboard_frame.place(x=170, rely=0, height=gameboard_dim[1], relwidth=1)

        # Player hand section
        player_hand_frame.place(x=170, y=gameboard_dim[1], relheight=1, relwidth=1)

        # Create toolbar buttons
        play_button = tk.Button(toolbar_frame,
                                text="Play",
                                command=play_game,
                                anchor='w',
                                bg='#ff6666',
                                activebackground='#c44343')
        config_button = tk.Button(toolbar_frame,
                                  text="Player Configuration",
                                  command=configure_players,
                                  anchor='w',
                                  bg='#f0f0f0',
                                  activebackground='#bdbdbd')
        rules_button = tk.Button(toolbar_frame,
                                 text="Rules",
                                 command=show_rules,
                                 anchor='w',
                                 bg='#f0f0f0',
                                 activebackground='#bdbdbd')
        quit_button = tk.Button(toolbar_frame,
                                text="Quit",
                                command=window.quit,
                                anchor='w',
                                bg='#f0f0f0',
                                activebackground='#bdbdbd')

        # Place buttons in the toolbar frame
        play_button.pack(fill=tk.X, ipady=10, pady=3)
        config_button.pack(fill=tk.X, ipady=10, pady=3)
        rules_button.pack(fill=tk.X, ipady=10, pady=3)
        quit_button.pack(fill=tk.X, ipady=10, pady=3)
        
        # Display the gameboard
        display_welcome_gameboard(gameboard_frame)
        
        # Display the player hand
        display_welcome_player_hand(player_hand_frame)
        

    def play_game():
        # Start the game
        messagebox.showinfo("Play Game", "Game screen (to be implemented)")


    def configure_players():
        # Clear the toolbar frame
        for widget in toolbar_frame.winfo_children():
            widget.destroy()

        # Create configuration buttons
        add_button = tk.Button(toolbar_frame,
                               text="Add",
                               command=add_player,
                               anchor='w',
                               bg='#f0f0f0',
                               activebackground='#bdbdbd')
        delete_button = tk.Button(toolbar_frame,
                                  text="Delete",
                                  command=delete_player,
                                  anchor='w',
                                  bg='#f0f0f0',
                                  activebackground='#bdbdbd')
        back_button = tk.Button(toolbar_frame,
                                text="Back",
                                command=show_main_menu,
                                anchor='w',
                                bg='#f0f0f0',
                                activebackground='#bdbdbd')

        # Place buttons in the toolbar frame
        add_button.pack(fill=tk.X, ipady=10, pady=3)
        delete_button.pack(fill=tk.X, ipady=10, pady=3)
        back_button.pack(fill=tk.X, ipady=10, pady=3)
        
    def add_player():
        # Add player functionality (to be implemented)
        messagebox.showinfo("Add Player", "Add player functionality (to be implemented)")

    def delete_player():
        # Delete player functionality (to be implemented)
        messagebox.showinfo("Delete Player", "Delete player functionality (to be implemented)")

        
    def show_rules():
        # Display rules of the game
        messagebox.showinfo("Rules", "Rules of the game (to be implemented)")

    # Bind key press event to show_main_menu function
    window.bind("<Key>", show_main_menu)

    # Run the Tkinter main loop
    window.mainloop()
