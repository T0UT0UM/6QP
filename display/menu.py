import tkinter as tk
from tkinter import messagebox

# Import game logic
from game_logic.card import Card, Deck
from game_logic.player import Player
from game_logic.bot import Bot
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
    
    # Game configuration
    players = []
    

    def show_main_menu(event=None):
        # Clear the window
        welcome_label.destroy()
        window.unbind("<Key>")
        
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
        if len(players) < 1:
            messagebox.showerror("Error", "You must have at least one player to start the game.")
            return
        
        for widget in toolbar_frame.winfo_children():
            widget.destroy()
        
        # Initialize the game
        game = Game(players, toolbar_frame, gameboard_frame, player_hand_frame)
        game.play()

    def configure_players():
        # Clear the toolbar frame
        for widget in toolbar_frame.winfo_children():
            widget.destroy()

        # Create configuration buttons
        tk.Button(toolbar_frame,
                  text="Back",
                  command=show_main_menu,
                  anchor='w',
                  bg='#f0f0f0',
                  activebackground='#bdbdbd').pack(fill=tk.X, ipady=10, pady=3)
        
        tk.Label(toolbar_frame, text="Player name:").pack(anchor='w', padx=20, pady=3)
        player_name_entry = tk.Entry(toolbar_frame)
        player_name_entry.pack(anchor='w', padx=30, pady=3)
        tk.Label(toolbar_frame, text="Player type:").pack(anchor='w', padx=20, pady=3)
        player_type_var = tk.StringVar()
        player_type_var.set("human")
        tk.Radiobutton(toolbar_frame, text="Human", variable=player_type_var, value="human").pack(anchor='w', padx=30, pady=3)
        tk.Radiobutton(toolbar_frame, text="Bot", variable=player_type_var, value="bot").pack(anchor='w', padx=30, pady=3)
        tk.Label(toolbar_frame, text="Bot difficulty:").pack(anchor='w', padx=20, pady=3)
        bot_difficulty_var = tk.StringVar()
        bot_difficulty_var.set("easy")
        tk.Radiobutton(toolbar_frame, text="Easy", variable=bot_difficulty_var, value="easy").pack(anchor='w', padx=30, pady=3)
        tk.Radiobutton(toolbar_frame, text="Medium", variable=bot_difficulty_var, value="medium").pack(anchor='w', padx=30, pady=3)
        tk.Radiobutton(toolbar_frame, text="Hard", variable=bot_difficulty_var, value="hard").pack(anchor='w', padx=30, pady=3)
        tk.Button(toolbar_frame,
                  text="Add",
                  command=lambda: add_player(player_name_entry.get(), player_type_var.get(), bot_difficulty_var.get()),
                  width=10,
                  bg='#f0f0f0',
                  activebackground='#bdbdbd').pack(anchor='w', padx=20, pady=3)
        tk.Button(toolbar_frame,
                  text="Delete",
                  command=lambda: delete_player(player_name_entry.get()),
                  width=10,
                  bg='#f0f0f0',
                  activebackground='#bdbdbd').pack(anchor='w', padx=20, pady=3)
        
        # Display the list of players
        show_player_list()
        
        
    def add_player(player_name, player_type, bot_difficulty):
        if player_type == "human":
            players.append(Player(player_name))
        elif player_type == "bot":
            players.append(Bot(player_name, bot_difficulty))
        configure_players()

    def delete_player(player_name):
        for i in range(len(players)):
            if players[i].name == player_name:
                players.pop(i)
                break
        configure_players()
        
        
    def show_player_list():
        tk.Label(toolbar_frame, text="List of players (" + str(len(players)) + ")").pack(fill='x', ipady=10, pady=3)
        player_box = tk.Listbox(toolbar_frame, height=5)
        player_box.pack(fill='x', ipady=10, pady=3)
        for player in players:
            if isinstance(player, Bot):
                player_box.insert(tk.END, player.name + " (" + player.difficulty + ")")
            else:
                player_box.insert(tk.END, player.name)
        

        
    def show_rules():
        # Display rules of the game
        messagebox.showinfo("Rules", "Rules of the game (to be implemented)")

    # Bind key press event to show_main_menu function
    window.bind("<Key>", show_main_menu)

    # Run the Tkinter main loop
    window.mainloop()
