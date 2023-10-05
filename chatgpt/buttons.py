import tkinter as tk
import random

# Function to handle button 1 click
def button1_click():
    label.config(text="Button 1 Clicked!")

# Function to handle button 2 click
def button2_click():
    label.config(text="Button 2 Clicked!")

def button3_click():
    num = random.randint(1,5)
    label.config(text="The number is "+num)
    

def button4_click():
    label.config(text="Button 4 Clicked!")

# Create the main window
root = tk.Tk()
root.title("Two Buttons")

# Create a label
label = tk.Label(root, text="", padx=20, pady=10)
label.pack()

# Create the first button
button1 = tk.Button(root, text="Button 1", command=button1_click, bg="red", font=50)
button1.pack(pady=10)

# Create the second button
button2 = tk.Button(root, text="Button 2", command=button2_click, bg="green", font=50)
button2.pack(pady=10)

button3 = tk.Button(root, text="8 ball", command=button3_click, bg= "yellow", font=60)
button3.pack(pady=10)

button4 = tk.Button(root, text="Button 4", command=button4_click, bg="blue", font=50)
button4.pack(pady=10)
# Start the Tkinter event loop
root.mainloop()
