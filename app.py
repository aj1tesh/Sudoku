import tkinter as tk
from tkinter import messagebox
import random

def is_safe(board, row, col, num):
    # Check if placing 'num' at board[row][col] is safe
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False
    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
                
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_safe(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        else:
                            board[row][col] = 0
                return False
    return True

def generate_sudoku():
    board = [[0]*9 for _ in range(9)]
    solve_sudoku(board)
    hide_count = 40
    
    cells_to_hide = random.sample(range(81), hide_count)
    for idx in cells_to_hide:
        row, col = idx // 9, idx % 9
        board[row][col] = 0
    
    return board

def solve():
    board = []
    for i in range(9):
        row = []
        for j in range(9):
            value = cells[i][j].get()
            if value == "":
                row.append(0)
            else:
                row.append(int(value))
        board.append(row)
    
    if solve_sudoku(board):
        for i in range(9):
            for j in range(9):
                current_value = cells[i][j].get()
                new_value = str(board[i][j])
                if current_value == "":
                    cells[i][j].delete(0, tk.END)
                    cells[i][j].insert(0, new_value)
                    cells[i][j].config(fg="red")  # Set solved numbers to red
    else:
        messagebox.showerror("No Solution", "No solution exists for the given Sudoku.")

def generate_and_load():
    board = generate_sudoku()
    for i in range(9):
        for j in range(9):
            cells[i][j].delete(0, tk.END)
            if board[i][j] != 0:
                cells[i][j].insert(0, str(board[i][j]))
                cells[i][j].config(fg="black")  # Set pre-generated numbers to black

root = tk.Tk()
root.title("Sudoku Solver")

window_width = 600
window_height = 600

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_position = int((screen_width / 2) - (window_width / 2))
y_position = int((screen_height / 2) - (window_height / 2))

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
entry_style = {"width": 2, "font": ('Arial', 24), "justify": 'center'}

cells = []
for i in range(9):
    row = []
    for j in range(9):
        cell = tk.Entry(root, **entry_style)
        cell.grid(row=i, column=j, padx=1, pady=1)
        if (i // 3) % 2 == 0 and (j // 3) % 2 == 0:
            cell.config(highlightthickness=2, highlightbackground="black")
        elif (i // 3) % 2 == 1 and (j // 3) % 2 == 1:
            cell.config(highlightthickness=2, highlightbackground="black")
        row.append(cell)
    cells.append(row)

button_style = {"padx": 10, "pady": 5, "width": 12, "font": ('Arial', 12)}

solve_button = tk.Button(root, text="Solve Sudoku", command=solve, **button_style)
solve_button.grid(row=9, column=0, columnspan=3, pady=(10, 20), sticky="ew")

generate_button = tk.Button(root, text="Generate Sudoku", command=generate_and_load, **button_style)
generate_button.grid(row=9, column=3, columnspan=3, pady=(10, 20), sticky="ew")

root.mainloop()
