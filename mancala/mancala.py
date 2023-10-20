import mechanics
import tkinter as tk
from tkinter import PhotoImage

#generate board
game = mechanics.Board()
game.getPlayers()
# Window Creation
window  = tk.Tk()
window.title = "Mancala"
window.configure(bg="Grey")

# Load the image using the file path
bg_image = PhotoImage(file= r"C:\Users\dgard\Downloads\luhcalm.png")

#callback function for when button is pressed
def click(player, column):
    print("l")
    if player != game.turn: #if button isn't pressed on the right turn
        return #do nothing
    game.move(column) #refer to the button that got pressed
    update_board()

def update_board():
    for row in range(2): #Creates a row of three buttons and they get added to the buttons list
        for col in range(6):
            buttons[row][col].config(text=str(game.board[row][col]))
    lside.config(text=game.players[0].score)
    rside.config(text=game.players[1].score)
    pass
# Create a label to display the image
background_label = tk.Label(window, image=bg_image)
background_label.place(x=10, y=0)

#Creation of the 2x6 grid
buttonposx = 375
buttonposy = 100
i = 0
buttons = [[4,4,4,4,4,4], [4,4,4,4,4,4]]
for row in range(2): #Creates a row of three buttons and they get added to the buttons list
    if i == 1:
        buttonposy += 290
        buttonposx = 375
    for col in range(6):
        buttons[row][col] = tk.Button(window, text="", font=("Algerian", 70), height= 2, width= 2, padx=2, pady=2, command=lambda player = i-1, col=col: click(bool(player), col))
        buttons[row][col].place(x=buttonposx, y=buttonposy)
        buttons[row][col].config(text="4")
        buttonposx+=130
    i+=1
#Creation of the two side buttons (Score Pits)
lside = tk.Button(window, text="0", font=("Algerian", 75), height= 4, width= 2)
lside.place(x=242, y=125)
rside = tk.Button(window, text="0", font=("Algerian", 75), height= 4, width= 2)
rside.place(x=1152, y=125)


#board.getPlayers()
#player1name = board.players[0].name
#player2name = board.players[1].name
#name1 = tk.Label(window, text= "Player 1: " + player1name, font=("Algerian", 20))
#name1.place(x= 30, y = 30)
#name2 = tk.Label(window, text= "Player 2: " + player2name, font=("Algerian", 20))
#name2.place(x= 30, y = 75)

#board.move()



window.mainloop()