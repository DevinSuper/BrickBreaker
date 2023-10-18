import mechanics
import tkinter as tk
from tkinter import PhotoImage
#from tkinter import simpledialog


# Game Window Creation
window  = tk.Tk()
window.title = "Mancala"
window.configure(bg="Grey")

# Load the image using the file path
bg_image = PhotoImage(file= r"C:\Users\d3v1n\Downloads\mancalaimg.png")

# Create a label to display the image
background_label = tk.Label(window, image=bg_image)
background_label.place(x=10, y=0)

click = 0
def buttonclick():
    click = 1

#Creation of the 2x6 grid
buttonnum = 1
buttonposx = 375
buttonposy = 100

i = 0
buttons = [[4,4,4,4,4,4], [4,4,4,4,4,4]]
for row in range(2): #Creates two rows of six buttons and they get added to the buttons list
    if i == 1:
        buttonposy += 290
        buttonposx = 375
    for col in range(6):
        buttons[row][col] = tk.Button(window, text=str(buttonnum), font=("Algerian", 70), height= 2, width= 2, padx=2, pady=2, command=buttonclick)
        buttons[row][col].place(x=buttonposx, y=buttonposy)
        buttons[row][col].config(text="4")
        buttonposx+=130
        buttonnum+=1
    i+=1
#Creation of the two side buttons (Score Pits)
lside = tk.Button(window, text="0", font=("Algerian", 75), height= 4, width= 2)
lside.place(x=242, y=125)
rside = tk.Button(window, text="0", font=("Algerian", 75), height= 4, width= 2)
rside.place(x=1152, y=125)

#Name Input (Input is in the terminal)
board = mechanics.Board()
board.getPlayers()
player1name = board.players[0].name
player2name = board.players[1].name
name1 = tk.Label(window, text= "Player 1: " + player1name, font=("Algerian", 20))
name1.place(x= 30, y = 45)
name2 = tk.Label(window, text= "Player 2: " + player2name, font=("Algerian", 20))
name2.place(x= 30, y = 90)

if(click==1):
    for i in range(int(buttons[row][col].cget('text'))):
        newnum = int(buttons[row][col].cget('text'))+ 1
        buttons[row][col-1].config(text= str(newnum))
    click==0

#players = mechanics.Player()


window.mainloop()





















#p1 = ""
#def input_name():
 #   playname = simpledialog.askstring("Name", input("Enter Player 1"))
  #  p1=playname
   # return p1

#namebutton = tk.Button(window, text="Input Names", font=("Algerian", 15), command=input_name)
#namebutton.place(x=30, y=15)