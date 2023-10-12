import tkinter as tk
import mechanics


window  = tk.Tk()
window.title = "Mancala"
window.configure(bg= "Black")
#background = tk.PhotoImage(file= "manalaimg.jpg")

#2x6
buttonposx = 375
buttonposy = 100
i = 0
buttons = [[4,4,4,4,4,4], [4,4,4,4,4,4]]
for row in range(2): #Creates a row of three buttons and they get added to the buttons list
    if i == 1:
        buttonposy += 290
        buttonposx = 375
    for col in range(6):
        buttons[row][col] = tk.Button(window, text="", font=("Algerian", 70), height= 2, width= 2, padx=2, pady=2)
        buttons[row][col].place(x=buttonposx, y=buttonposy)
        buttons[row][col].config(text="4")
        buttonposx+=130
    i+=1

lside = tk.Button(window, text="0", font=("Algerian", 75), height= 4, width= 2)
lside.place(x=242, y=125)
rside = tk.Button(window, text="0", font=("Algerian", 75), height= 4, width= 2)
rside.place(x=1152, y=125)





window.mainloop()