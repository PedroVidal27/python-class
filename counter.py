import tkinter as tk

class CounterApp:
    def __init__(self, root):
        self.counter = 0

        self.label = tk.Label(root, text=f"Contador: {self.counter}", font=("Arial", 20))
        self.label.pack(pady=10)

        self.increment_button = tk.Button(root, text="Aumentar", command=self.increment, font=("Arial", 15))
        self.increment_button.pack(side=tk.LEFT, padx=20)

        self.decrement_button = tk.Button(root, text="Diminuir", command=self.decrement, font=("Arial", 15))
        self.decrement_button.pack(side=tk.RIGHT, padx=20)

    def increment(self):
        self.counter += 1
        self.label.config(text=f"Contador: {self.counter}")

    def decrement(self):
        self.counter -= 1
        self.label.config(text=f"Contador: {self.counter}")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Contador")
    app = CounterApp(root)
    root.mainloop()
