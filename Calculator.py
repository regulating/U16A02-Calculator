import tkinter as tk

# initalise main application window
class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        # placeholder for the gui
        self.build_ui()

        def build_ui(self):
            # to be added
            pass
    
    # run the app
    if __name__ == "__main__":
        root = tk.Tk()
        app = CalculatorApp(root)
        root.mainloop()
