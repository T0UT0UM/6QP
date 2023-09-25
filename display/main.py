import tkinter as tk

from game_logic.player import Player
from display.gameboard import Gameboard
from display.player_hand import Player_hand

class Menu:
    def __init__(self, game):
        """
        Create the welcome window.

        Args:
            game (Game): The game to launch.
        """
        self.game = game
        
        self.window = tk.Tk()
        self.window.title("6 Qui Prend!")
        self.window.geometry("800x600")

        self.gameboard_frame = tk.Frame(self.window, bg="white")
        self.player_frame = tk.Frame(self.window, bg="white")
        self.toolbar = tk.Frame(self.window, bg="#f0f0f0")

        self.gameboard = Gameboard(self.game, self.gameboard_frame)
        self.player_hand = Player_hand(self.game, self.player_frame)

        welcome = tk.PhotoImage(file="display/images/welcome.png")
        self.welcome_label = tk.Label(self.window, image=welcome)
        self.welcome_label.pack()

        self.window.bind("<Key>", lambda event: self.menu())

        self.window.mainloop()

    def menu(self):
        """
        Create the menu window.
        """
        # Destroy the welcome window
        self.welcome_label.destroy()
        self.clear_toolbar()
        self.window.unbind("<Key>")
        self.toolbar.pack(fill=tk.Y, side=tk.LEFT, expand=False)
        self.gameboard_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.player_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Play button
        tk.Button(self.toolbar,
                  text="Play",
                  command=self.play,
                  anchor='w',
                  bg='#ff6666',
                  activebackground='#c44343').pack(fill='x', ipady=10, pady=3)

        # Configuration player button
        tk.Button(self.toolbar,
                  text="Player configuration",
                  command=self.player_conf,
                  anchor='w',
                  bg='#f0f0f0',
                  activebackground='#bdbdbd').pack(fill='x', ipady=10, pady=3)

        # Rules button
        tk.Button(self.toolbar,
                  text="Rules",
                  command=self.rules,
                  anchor='w',
                  bg='#f0f0f0',
                  activebackground='#bdbdbd').pack(fill='x', ipady=10, pady=3)

        # Quit button
        tk.Button(self.toolbar,
                  text="Quit",
                  command=self.window.quit,
                  anchor='w',
                  bg='#f0f0f0',
                  activebackground='#bdbdbd').pack(fill='x', ipady=10, pady=3)

    def clear_toolbar(self):
        """
        Destroy all the widgets in the toolbar.
        """
        for widget in self.toolbar.winfo_children():
            widget.destroy()

    def play(self):
        #self.game.play()
        self.gameboard.display_rows()
        self.game.init_player(self.game.players[0])
        self.player_hand.display_hand()

    def player_conf(self):
        """
        Player configuration window.
        """

        def add_bot(bot_name, difficulty):
            self.game.players.append(Player(bot_name, difficulty))
            self.player_conf()

        def delete_bot(bot_name):
            for i in range(len(self.game.players)):
                if self.game.players[i].name == bot_name:
                    self.game.players.pop(i)
                    break
            self.player_conf()

        def show_player_list():
            tk.Label(self.toolbar, text="List of players").pack(fill='x', ipady=10, pady=3)
            players = tk.Listbox(self.toolbar, height=5)
            players.pack(fill='x', ipady=10, pady=3)
            for player in self.game.players:
                if player.difficulty != None:
                    players.insert(tk.END, player.name+" ("+player.difficulty+")")
                else:
                    players.insert(tk.END, player.name)

        self.clear_toolbar()

        # Back button
        tk.Button(self.toolbar,
                    text="Back",
                    command=self.menu,
                    anchor='w',
                    bg='#f0f0f0',
                    activebackground='#bdbdbd').pack(fill='x', ipady=10, pady=3)

        # Bot configuration
        tk.Label(self.toolbar, text="Bot name").pack(anchor='w', padx=20, pady=3)
        bot_name = tk.Entry(self.toolbar)
        bot_name.pack(anchor='w', padx=30, pady=3)
        tk.Label(self.toolbar, text="Difficulty").pack(anchor='w', padx=20, pady=3)
        difficulty = tk.StringVar()
        tk.Radiobutton(self.toolbar, text="Easy", variable=difficulty, value="Easy").pack(anchor='w', padx=30, pady=3)
        tk.Radiobutton(self.toolbar, text="Medium", variable=difficulty, value="Medium").pack(anchor='w', padx=30, pady=3)
        tk.Radiobutton(self.toolbar, text="Hard", variable=difficulty, value="Hard").pack(anchor='w', padx=30, pady=3)
        tk.Button(self.toolbar,
                    text="Add",
                    command=lambda: add_bot(bot_name.get(), difficulty.get()),
                    width=10,
                    bg='#f0f0f0',
                    activebackground='#bdbdbd').pack(anchor='w', padx=20, pady=3)
        tk.Button(self.toolbar,
                    text="Delete",
                    command=lambda: delete_bot(bot_name.get()),
                    width=10,
                    bg='#f0f0f0',
                    activebackground='#bdbdbd').pack(anchor='w',ipadx=10, padx=20, pady=3)

        show_player_list()


    def rules(self):
        pass

