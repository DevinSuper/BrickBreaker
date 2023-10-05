import tkinter as tk

# Function to handle button clicks
def button_click(row, col):
    print(f"Button ({row}, {col}) clicked")

# Create the main window
root = tk.Tk()
root.title("2x3 Grid of Buttons")

# Create a 2x3 grid of buttons
for row in range(3):
    for col in range(3):
        button = tk.Button(root, text=f"Button ({row+1}, {col+1})", command=lambda row=row, col=col: button_click(row, col))
        button.grid(row=row, column=col, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
