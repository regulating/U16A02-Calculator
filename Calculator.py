import tkinter as tk

# main app window
class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        # add display screen
        self.display = tk.Entry(self.root, font=("Arial", 20), bd=10, insertwidth=2, width=14, justify="right")
        self.display.grid(row=0, column=0, columnspan=4, pady=10)

        # add number buttons
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("0", 4, 1)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, font=("Arial", 18), padx=20, pady=20, command=lambda t=text: self.append_to_display(t))
            button.grid(row=row, column=col, sticky="nsew")

        # add operation buttons
        operations = [
            ("C", 1, 3), ("/", 2, 3), ("*", 3, 3),
            ("-", 4, 2), ("+", 4, 3), ("=", 4, 0)
        ]

        for (text, row, col) in operations:
            button = tk.Button(self.root, text=text, font=("Arial", 18), padx=20, pady=20, command=lambda t=text: self.handle_operation(t))
            button.grid(row=row, column=col, sticky="nsew")

    def append_to_display(self, value):
        # append the pressed button's value to the display
        self.display.insert(tk.END, value)

    def handle_operation(self, operator):
        if operator == "C":
            self.display.delete(0, tk.END)  # clear the display
        elif operator == "=":
            try:
                result = eval(self.display.get())  # eval the expression
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            self.append_to_display(operator)

# run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
