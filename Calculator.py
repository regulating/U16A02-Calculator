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

        self.build_ui()

    def build_ui(self):
        # to be added
        pass

# run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
