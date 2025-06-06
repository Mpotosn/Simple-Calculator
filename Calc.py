import tkinter as tk

# Function to evaluate the expression
def evaluate_expression():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to add characters to the entry
def add_to_expression(char):
    entry.insert(tk.END, char)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create an entry widget for displaying expressions and results
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief='groove')
entry.grid(row=0, column=0, columnspan=4)

# Create buttons for digits and operations
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, width=5, height=2, command=evaluate_expression)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, command=lambda t=text: add_to_expression(t))
    btn.grid(row=row, column=col)

# Start the Tkinter main loop
root.mainloop()




