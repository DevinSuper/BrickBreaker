import tkinter as tk

# Initialize a list to store click counts for each button
button_click_counts = [0, 0, 0]

# Function to handle button clicks
def button_click(button_index):
    # Increment the click count for the corresponding button
    button_click_counts[button_index] += 1
    # Update the button text to display the current click count
    button_labels[button_index].config(text=f"Button {button_index + 1}: {button_click_counts[button_index]}")

# Create the main window
root = tk.Tk()
root.title("Count Button Clicks")

# Create labels to display click counts
button_labels = []
for i in range(3):
    label = tk.Label(root, text=f"Button {i + 1}: 0", padx=20, pady=10)
    label.pack()
    button_labels.append(label)

# Create three buttons
buttons = []
for i in range(3):
    button = tk.Button(root, text=f"Button {i + 1}", command=lambda i=i: button_click(i))
    button.pack(pady=10)
    buttons.append(button)

# Start the Tkinter event loop
root.mainloop()
