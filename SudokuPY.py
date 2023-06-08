import tkinter as tk
from tkinter import messagebox

# Hardcoded sudoku puzzle
grid = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

class Sudoku:
    def __init__(self, root):
        self.board = grid
        self.gui = [[None for _ in range(9)] for _ in range(9)]
        self.root = root

        # Create 9 frames for 9 3x3 squares
        frames = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                frames[i][j] = tk.Frame(root, borderwidth=3, relief="groove")
                frames[i][j].grid(row=i, column=j)

        # Create 9x9 grid of Entry widgets
        for i in range(9):
            for j in range(9):
                self.gui[i][j] = tk.Entry(frames[i//3][j//3], width=2, font=('Arial', 24), justify='center')
                if self.board[i][j] != 0:
                    self.gui[i][j].insert(0, str(self.board[i][j]))
                    self.gui[i][j]['state'] = 'disabled'
                self.gui[i][j].grid(row=i%3, column=j%3)

        submit_button = tk.Button(root, text="Submit", command=self.submit)
        submit_button.grid(row=3, column=0, columnspan=3)

    def submit(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    if self.gui[i][j].get() == "":
                        messagebox.showerror("Error", "Empty fields detected. Please fill all fields with numbers between 1 and 9.")
                        return
                    try:
                        input_val = int(self.gui[i][j].get())
                    except ValueError:
                        messagebox.showerror("Error", "You must enter a number between 1 and 9.")
                        return
                    if not 1 <= input_val <= 9 or not self.valid_move(self.board, i, j, input_val):
                        messagebox.showerror("Error", "Invalid Sudoku puzzle.")
                        return
                    self.board[i][j] = input_val
        messagebox.showinfo("Sudoku", "Congratulations! You solved the puzzle.")

    @staticmethod
    def valid_move(board, row, col, num):
        for x in range(9):
            if board[row][x] == num:
                return False

        for x in range(9):
            if board[x][col] == num:
                return False

        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if board[i+start_row][j+start_col] == num:
                    return False
        return True


root = tk.Tk()
sudoku_game = Sudoku(root)
root.mainloop()
