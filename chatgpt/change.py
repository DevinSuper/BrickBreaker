import tkinter as tk

# Function to swap button text
def swap_text():
    text1 = button1.cget("text")
    text2 = button2.cget("text")
    text3 = button3.cget("text")
    
    button1.config(text=text3)
    button2.config(text=text1)
    button3.config(text=text2)

def reset():
    button1.config(text="Button 1")
    button2.config(text="Button 2")
    button3.config(text="Button 3")

# Create the main window
root = tk.Tk()
root.title("Swap Button Text")

# Create the first button
button1 = tk.Button(root, text="Button 1", command=swap_text)
button1.pack(pady=10)

# Create the second button
button2 = tk.Button(root, text="Button 2", command=swap_text)
button2.pack(pady=10)

button3 = tk.Button(root, text="Button 3", command=swap_text)
button3.pack(pady=10)

button4 = tk.Button(root, text="Reset", command=reset)
button4.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
