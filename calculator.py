import tkinter as tk

# Initialize the main application window
root = tk.Tk()
root.title("My Calculator")
root.geometry("400x500")

# --- MILESTONE 3: THE BRAIN (The missing function!) ---
def button_click(value):
    """Handles what happens when a button is clicked."""
    if value == "C":
        # Clear the display completely
        display.delete(0, tk.END)
    elif value == "=":
        # Calculate the result
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(tk.END, str(result))
        except:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    else:
        # For numbers and operators, add them to the screen
        display.insert(tk.END, value)


# --- MILESTONE 2: THE DISPLAY ---
display = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief="groove", justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# --- MILESTONE 1: THE BUTTONS ---
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+']
]

# Use loops to dynamically create and place the buttons
for row_index, row_list in enumerate(buttons):
    for col_index, button_text in enumerate(row_list):
        btn = tk.Button(root, text=button_text, font=("Arial", 18), width=5, height=2,
                        command=lambda text=button_text: button_click(text))
        btn.grid(row=row_index + 1, column=col_index, padx=5, pady=5)

# Start the main event loop
root.mainloop()
