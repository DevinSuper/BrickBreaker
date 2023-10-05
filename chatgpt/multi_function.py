import tkinter as tk

# Function 1
def function_1():
    print("Function 1 executed")

# Function 2
def function_2():
    print("Function 2 executed")

def function_3():
    print("Function 3 executed")

# Function to run both functions
def run_both_functions():
    function_1()
    function_2()
    function_3()

# Create the main window
root = tk.Tk()
root.title("Button Running Two Functions")

# Create a button that runs both functions
run_button = tk.Button(root, text="Run Functions", command=run_both_functions)
run_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
