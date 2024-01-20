import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from datetime import datetime

class IncomeTrackerGUI:
    all_transactions = []  # Class variable to store all transactions

    def __init__(self, root):
        self.root = root
        self.root.title("Income Tracker")

        # Create variables
        self.source_var = tk.StringVar()
        self.amount_var = tk.DoubleVar()
        self.transactions = []

        # Create styles
        self.create_styles()

        # Create UI elements
        self.create_widgets()

    def create_styles(self):
        self.style = ttk.Style()

        # Configure label style
        self.style.configure("Label.TLabel", font=("Comic Sans", 12), foreground="white")

        # Configure entry style
        self.style.configure("Entry.TEntry", font=("Comic Sans", 12), foreground="white")

        # Configure button style
        self.style.configure("Button.TButton", font=("Comic Sans", 12), foreground="white", background="black")

        # Configure treeview style
        self.style.configure("Treeview.Treeview", font=("Comic Sans", 12), foreground="black", background="lightyellow")

    def create_widgets(self):
        # Label and Entry for Income Source
        source_label = ttk.Label(self.root, text="Income Source:", style="Label.TLabel")
        source_entry = ttk.Entry(self.root, textvariable=self.source_var, style="Entry.TEntry")

        # Label and Entry for Income Amount
        amount_label = ttk.Label(self.root, text="Income Amount ($):", style="Label.TLabel")
        amount_entry = ttk.Entry(self.root, textvariable=self.amount_var, validate="key", validatecommand=(self.root.register(self.validate_amount), "%P"), style="Entry.TEntry")

        # Button to Record Income
        record_button = ttk.Button(self.root, text="Record Income", command=self.record_income, style="Button.TButton")

        # Button to Save Transactions
        save_button = ttk.Button(self.root, text="Save", command=self.save_transactions, style="Button.TButton")

        # Button to Reset Entries
        reset_button = ttk.Button(self.root, text="Reset", command=self.reset_entries, style="Button.TButton")

        # Treeview for displaying income transactions
        columns = ("Timestamp", "Source", "Amount")
        self.treeview = ttk.Treeview(self.root, columns=columns, show="headings", style="Treeview.Treeview")
        for col in columns:
            self.treeview.heading(col, text=col)
        self.treeview.column("Timestamp", width=150)

        # Pack UI elements
        source_label.pack(pady=5)
        source_entry.pack(pady=5)
        amount_label.pack(pady=5)
        amount_entry.pack(pady=5)
        record_button.pack(pady=10)
        save_button.pack(pady=5)
        reset_button.pack(pady=5)
        self.treeview.pack(pady=20)

    def validate_amount(self, new_value):
        try:
            if new_value:
                float(new_value)
            return True
        except ValueError:
            return False

    def record_income(self):
        source = self.source_var.get()
        amount = self.amount_var.get()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if source and amount:
            self.transactions.append((timestamp, source, amount))
            self.update_treeview()

            # Clear entry fields after recording income
            self.source_var.set("")
            self.amount_var.set(0.0)

    def update_treeview(self):
        # Clear existing items
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        # Insert updated transactions
        for transaction in self.transactions:
            self.treeview.insert("", "end", values=transaction)

    def save_transactions(self):
        # Save the transactions to the class variable (all_transactions)
        self.all_transactions.extend(self.transactions)

        # Here you can implement the logic to save transactions to a file or database
        # For demonstration purposes, let's print the saved transactions to the console
        print("All Transactions:", self.all_transactions)

    def reset_entries(self):
        # Clear entry fields and transactions
        self.source_var.set("")
        self.amount_var.set(0.0)
        self.transactions = []
        self.update_treeview()

def main():
    root = ThemedTk(theme="equilux")  # Use a theme of your choice
    app = IncomeTrackerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
