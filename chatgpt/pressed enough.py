import tkinter as tk

# Function to open a new pop-up window
def open_popup_window():
    popup = tk.Toplevel(root)
    popup.title("Pop-up Window")

    label = tk.Label(popup, text="This is a pop-up window.")
    label.pack(padx=20, pady=10)

    close_button = tk.Button(popup, text="Close", command=popup.destroy)
    close_button.pack(pady=10)

# Function to handle button clicks
def button_click():
    global click_count, click_count2
    click_count += 1
    if click_count >= 2 and click_count2 >=2:  # Open pop-up after 5 clicks
        click_count = 0
        click_count2 = 0
        open_popup_window()

def button_click2():
    global click_count2, click_count
    click_count2 += 1
    if click_count2 >= 2 and click_count >=2:  # Open pop-up after 5 clicks
        click_count2 = 0
        click_count = 0
        open_popup_window()


# Create the main window
root = tk.Tk()
root.title("Button Click Counter")

# Create a button to click
click_count = 0
click_button = tk.Button(root, text="Click Me", command=button_click)
click_button.pack(pady=20)

click_count2 = 0
click_button2 = tk.Button(root, text="Click Me2", command=button_click2)
click_button2.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
