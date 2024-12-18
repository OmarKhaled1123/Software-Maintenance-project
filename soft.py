import tkinter as tk
from tkinter import messagebox


class Ai_ProjectGUI:
    def __init__(self):
        # Initialize
        self.root = tk.Tk()
        self.root.title("omar gi")
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.game_mode = None
        
        pvp_button = tk.Button(self.root, text='Player vs Player2', command=lambda: self.set_game_mode('PvP'))
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

    # Handle button click events
    def on_button_click(self, row, col):
        if self.board[row][col] == ' ':
            # Update the game board and button text
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)


            if self.check_winner():
                self.show_winner_message()
                self.reset_game()
            elif self.is_board_full():
                self.show_draw_message()
                self.reset_game()
            else:
                self.switch_player()

            # If playing against the computer, make the computer move
            if self.game_mode == 'PvC' and self.current_player == 'O':
                self.make_computer_move()

    # Switch the current player
    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    
    def make_computer_move(self):
        row, col = self.get_best_move()
        self.on_button_click(row, col) #update game board

    # Minimax algorithm for determining the best move
    def minimax(self, depth, maximizing_player):
        if self.check_winner():
            return -1 if maximizing_player else 1
        elif self.is_board_full():
            return 0

        if maximizing_player:
            max_eval = float('-inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = 'O'
                        eval = self.minimax(depth + 1, False)
                        self.board[i][j] = ' '
                        max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = 'X'
                        eval = self.minimax(depth + 1, True)
                        self.board[i][j] = ' '
                        min_eval = min(min_eval, eval)
            return min_eval

    # Determine the best move for the computer using the minimax algorithm
    def get_best_move(self):  #built in method
        best_val = float('-inf')
        best_move = (-1, -1)

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'O'
                    move_val = self.minimax(0, False)                    #simulation,initial depth is O
                    self.board[i][j] = ' '

                    if move_val > best_val:
                        best_move = (i, j)
                        best_val = move_val

        return best_move



    # Check if there is a winner
    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False

    def is_board_full(self):
        return all(cell != ' ' for row in self.board for cell in row)


    def show_winner_message(self):
        winner = 'Player X' if self.current_player == 'X' else 'Player O'
        messagebox.showinfo("Game Over", f"{winner} wins!")


    def show_draw_message(self):
        messagebox.showinfo("Game Over", "It's a draw!")

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ' '
                self.buttons[i][j].config(text='')
        self.current_player = 'X'
        self.game_mode = None

    # Run the Tkinter main loop
    def run(self):
        self.root.mainloop()

# Entry point for the program
if __name__ == "__main__":
    # Create an instance of the TicTacToeGUI class and run the game
    game = Ai_ProjectGUI()
    game.run()
