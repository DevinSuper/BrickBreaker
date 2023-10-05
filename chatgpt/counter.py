import tkinter as tk

# Variables to store button click counts
button1_count = 0
button2_count = 0

# Function to handle button 1 click

def reset():
    global button2_count, button1_count
    button2_count = 0
    button1_count = 0
    button1_count_label.config(text=f"Button 1 Clicked: {button1_count}")
    button2_count_label.config(text=f"Button 2 Clicked: {button2_count}")

def button1_click():
    global button1_count
    button1_count += 1
    button1_count_label.config(text=f"Button 1 Clicked: {button1_count}")

# Function to handle button 2 click
def button2_click():
    global button2_count
    button2_count += 1
    button2_count_label.config(text=f"Button 2 Clicked: {button2_count}")

# Create the main window
root = tk.Tk()
root.title("Button Click Counter")

# Create labels to display click counts
button1_count_label = tk.Label(root, text="Button 1 Clicked: 0", padx=20, pady=10)
button1_count_label.pack()

button2_count_label = tk.Label(root, text="Button 2 Clicked: 0", padx=20, pady=10)
button2_count_label.pack()

# Create the first button
button1 = tk.Button(root, text="Button 1", command=button1_click)
button1.pack(pady=10)

# Create the second button
button2 = tk.Button(root, text="Button 2", command=button2_click)
button2.pack(pady=10)

reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.pack(pady=10)

button1 = tk.Button(root, text="Button 1.1", command=button1_click)
button1.pack(pady=10)
# Start the Tkinter event loop
root.mainloop()
