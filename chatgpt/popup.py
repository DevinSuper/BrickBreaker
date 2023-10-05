import tkinter as tk

# Function to open a new pop-up window
def open_popup_window():
    popup = tk.Toplevel(root)
    popup.title("Pop-up Window")

    label = tk.Label(popup, text="This is a pop-up window.")
    label.pack(padx=20, pady=10)

    close_button = tk.Button(popup, text="Close", command=popup.destroy)
    close_button.pack(pady=10)

    open_button.config(text="This window has been opened")

# Create the main window
root = tk.Tk()
root.title("Main Window")

# Create a button to open the pop-up window
open_button = tk.Button(root, text="Open Pop-up Window", command=open_popup_window)
open_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
