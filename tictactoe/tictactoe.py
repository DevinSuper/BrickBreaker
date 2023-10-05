import tkinter as tk


def board_check(row, col) -> str:
    hor = horiz_check(row) # we define them here so we don't have to double call them
    vert = col_Check(col)
    left_diag = ldiag()
    right_diag = rdiag()
    if hor != None:
        return hor
    elif vert != None:
        return vert
    elif left_diag != None:
        return left_diag
    elif right_diag != None:
        return right_diag
    return ""
            

def horiz_check(row) -> str:
    i=1
    repeated = True
    while(i< len(grid[row]) and repeated): 
        if grid[row][i-1].cget("text")  != grid[row][i].cget("text")  or grid[row][i-1].cget("text")  == "" :
            # compare current index with previous
            repeated = False
            return None
        i+=1 
    return grid[row][0].cget("text") 

def col_Check(col) -> str:
    i=1
    repeated = True
    while(i< len(grid[row]) and repeated): #assuming length of column == length of row
        if grid[i-1][col].cget("text") != grid[i][col].cget("text")  or grid[i-1][col].cget("text")  == "" :
            # compare current index with previous
            repeated = False
            return None
        i+=1 
    return grid[0][col].cget("text")

def rdiag() -> str:
    length = len(grid[row])-1
    repeated = True
    for i in range(length):
        target = grid[length-(i+1)][i+1]
        base = grid[length-i][i]
        if target.cget("text") != base.cget("text") or base.cget("text") == "":
            repeated = False
            return None
    return target.cget("text")
        
     # we know that's top left

def ldiag() -> str:
    i = 1
    repeated = True
    while(i< len(grid[row]) and repeated): #iterating tl diagonal
        if grid[i-1][i-1].cget("text") != grid[i][i].cget("text")  or grid[i-1][i-1].cget("text")  == "" :
            repeated = False
            return None
        i+=1
    return grid[0][0].cget("text")


def button_click(row,col):
    button = grid[row][col]
    if button.cget("text") == "":
        sample = "X"
    elif button.cget("text") == "X":
        sample = "O"
    else:
        sample = ""

    button.config(text = sample)
    if board_check(row, col) == "X":
        label.config(text="Player 1 wins")
    elif board_check(row, col) == "O":
        label.config(text="Player 2 wins")
# Create the main window
root = tk.Tk()
root.title("Tictactoe")

# Create a 3x3 grid of buttons

grid = []
for row in range(3):
    r = []
    for col in range(3):
        button = tk.Button(root, text=f"", command=lambda row=row, col=col: button_click(row, col))
        r.append(button)
        button.grid(row=row, column=col, padx=10, pady=10)
    grid.append(r)

label = tk.Label(root, text="", padx=20, pady=10)
label.grid(row=3, column=1)
# Start the Tkinter event loop
root.mainloop()
