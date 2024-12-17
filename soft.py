import tkinter as tk
from tkinter import messagebox


class Ai_ProjectGUI:
    def __init__(self):
        # Initialize
        self.root = tk.Tk()
        self.root.title("Ai_Project")
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.game_mode = None
        
        pvp_button = tk.Button(self.root, text='Player vs Player', command=lambda: self.set_game_mode('PvP'))
        pvp_button.grid(row=3, column=0)
        pvc_button = tk.Button(self.root, text='Player vs Computer', command=lambda: self.set_game_mode('PvC'))
        pvc_button.grid(row=3, column=1)

        # Initialize the game board buttons
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text='', font=('normal', 20), width=8, height=4,
                            command=lambda row=i, col=j: self.on_button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    # Set the game mode based on user selection
    def set_game_mode(self, mode):
        self.game_mode = mode
