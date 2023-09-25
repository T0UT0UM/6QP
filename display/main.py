import tkinter as tk
import sys
sys.path.append('../game_logic')

class Menu:
    def __init__(self):
        """
        Create the welcome window.
        """
        self.window = tk.Tk()
        self.window.title("6 Qui Prend!")
        self.window.geometry("800x600")

        self.toolbar = tk.Frame(self.window, width = 200, bg="#f0f0f0")

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
        self.toolbar.pack(fill=tk.Y, side=tk.LEFT)

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
        pass

    def player_conf(self):
        """
        Player configuration window.
        """
        self.clear_toolbar()
        # Create a back button
        
        # Create widgets on the toolbar that allows:
            # - Enter a bot name
            # - Select a difficulty : easy, medium, hard (radio button)
            # - Add a bot
            # - Delete a bot
        # List of bots (number and name)

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
                  command=lambda: self.add_bot(bot_name.get(), difficulty.get()),
                  width=10,
                  bg='#f0f0f0',
                  activebackground='#bdbdbd').pack(anchor='w', padx=20, pady=3)
        tk.Button(self.toolbar,
                  text="Delete",
                  command=lambda: self.delete_bot(bot_name.get()),
                  width=10,
                  bg='#f0f0f0',
                  activebackground='#bdbdbd').pack(anchor='w',ipadx=10, padx=20, pady=3)

        # List of bots
        tk.Label(self.toolbar, text="List of bots").pack(fill='x', ipady=10, pady=3)
        
        
        

    def rules(self):
        pass

