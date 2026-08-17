import tkinter as tk
from tkinter import messagebox

current_player = "X"
board = [""] * 9

def check_winner():
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for condition in win_conditions:
        a, b, c = condition
        if board[a] == board[b] == board[c] != "":
            return True
    return False

def button_click(index):
    global current_player

    if board[index] == "":
        board[index] = current_player
        buttons[index].config(text=current_player)

        if check_winner():
            messagebox.showinfo("Winner", f"Player {current_player} wins!")
            reset_game()
            return

        if "" not in board:
            messagebox.showinfo("Draw", "It's a draw!")
            reset_game()
            return

        current_player = "O" if current_player == "X" else "X"

def reset_game():
    global board, current_player

    board = [""] * 9
    current_player = "X"

    for button in buttons:
        button.config(text="")

root = tk.Tk()
root.title("Tic Tac Toe")

buttons = []

for i in range(9):
    btn = tk.Button(
        root,
        text="",
        font=("Arial", 20),
        width=5,
        height=2,
        command=lambda i=i: button_click(i)
    )
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

reset_btn = tk.Button(root, text="Reset", command=reset_game)
reset_btn.grid(row=3, column=0, columnspan=3)

root.mainloop()