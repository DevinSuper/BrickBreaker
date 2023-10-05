import tkinter as tk
import mechanics


window  = tk.Tk()
window.title = "Mancala"

#2x6
buttons = [[4,4,4], [4,4,4], [4,4,4]]
for row in range(2): #Creates a row of three buttons and they get added to the buttons list
    for col in range(6):
        buttons[row][col] = tk.Button(window, text="", font=("Arial", 75))
        buttons[row][col].grid(row=row, column=col)





window.mainloop()