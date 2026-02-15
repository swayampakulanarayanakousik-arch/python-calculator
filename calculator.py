import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#2c3e50")
        
        self.expression = ""
        
        # Create display
        self.display = tk.Entry(
            root, 
            font=('Arial', 24), 
            justify='right', 
            bd=10,
            bg="#ecf0f1",
            fg="#2c3e50"
        )
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)
        
        # Button layout
        buttons = [
            ('C', 1, 0, '#e74c3c'), ('⌫', 1, 1, '#e74c3c'), ('/', 1, 2, '#f39c12'), ('*', 1, 3, '#f39c12'),
            ('7', 2, 0, '#3498db'), ('8', 2, 1, '#3498db'), ('9', 2, 2, '#3498db'), ('-', 2, 3, '#f39c12'),
            ('4', 3, 0, '#3498db'), ('5', 3, 1, '#3498db'), ('6', 3, 2, '#3498db'), ('+', 3, 3, '#f39c12'),
            ('1', 4, 0, '#3498db'), ('2', 4, 1, '#3498db'), ('3', 4, 2, '#3498db'), ('.', 4, 3, '#3498db'),
            ('0', 5, 0, '#3498db'), ('00', 5, 1, '#3498db'), ('=', 5, 2, '#27ae60')
        ]
        
        # Create buttons
        for (text, row, col, color) in buttons:
            if text == '=':
                btn = tk.Button(
                    root,
                    text=text,
                    font=('Arial', 18, 'bold'),
                    bg=color,
                    fg='white',
                    command=self.calculate,
                    relief=tk.RAISED,
                    bd=3
                )
                btn.grid(row=row, column=col, columnspan=2, sticky="nsew", padx=5, pady=5)
            else:
                btn = tk.Button(
                    root,
                    text=text,
                    font=('Arial', 18, 'bold'),
                    bg=color,
                    fg='white',
                    command=lambda t=text: self.on_button_click(t),
                    relief=tk.RAISED,
                    bd=3
                )
                btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
        
        # Configure grid weights for responsive design
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
    
    def on_button_click(self, char):
        if char == 'C':
            self.expression = ""
            self.display.delete(0, tk.END)
        elif char == '⌫':
            self.expression = self.expression[:-1]
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)
        else:
            self.expression += str(char)
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)
    
    def calculate(self):
        try:
            result = eval(self.expression)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
            self.expression = str(result)
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()