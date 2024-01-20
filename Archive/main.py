import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from budget_calculator import BudgetCalculator
from income import IncomeTrackerGUI
from expense import MoneyTracker

class MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Buffy Money Manager")

        # Create styles
        self.create_styles()

        # Create UI elements
        self.create_widgets()

    def create_styles(self):
        self.style = ttk.Style()

        # Configure label style
        self.style.configure("Title.TLabel", font=("Comic Sans", 20, "bold"), foreground="purple")

        # Configure button style
        self.style.configure("Button.TButton", font=("Comic Sans", 14), foreground="black", background="brown")

    def create_widgets(self):
        # Title Label for Main Menu
        title_label = ttk.Label(self.root, text="Buffy Money Manager", style="Title.TLabel")
        title_label.pack(pady=20)

        # Initialize username_var 
        self.username_var = tk.StringVar()

        # Login Entry, Button, and 
        login_label = ttk.Label(self.root, text="Enter Username:")
        login_entry = ttk.Entry(self.root, textvariable=self.username_var)
        login_button = ttk.Button(self.root, text="Login", command=self.login, style="Button.TButton")

        login_label.pack(pady=5)
        login_entry.pack(pady=5)
        login_button.pack(pady=10)
     

        # Label to display the welcome message and balance
        self.welcome_label = ttk.Label(self.root, text="", style="Title.TLabel")
        self.welcome_label.pack(pady=10)

        # Buttons for Expense Tracker, Income Tracker, and Budget Calculator
        expense_button = ttk.Button(self.root, text="Expense Tracker", command=self.open_expense_tracker, style="Button.TButton")
        income_button = ttk.Button(self.root, text="Income Tracker", command=self.open_income_tracker, style="Button.TButton")
        budget_button = ttk.Button(self.root, text="Budget Calculator", command=self.open_budget_calculator, style="Button.TButton")

        expense_button.pack(pady=10)
        income_button.pack(pady=10)
        budget_button.pack(pady=10)

    def open_expense_tracker(self):
        # Instantiate the MoneyTracker class
        expense_tracker_page = MoneyTracker(tk.Toplevel(self.root))

    def open_income_tracker(self):
        # Instantiate the IncomeTrackerGUI class
        income_tracker_page = IncomeTrackerGUI(tk.Toplevel(self.root))

    def open_budget_calculator(self):
        # Instantiate the BudgetCalculator class
        budget_calculator_page = BudgetCalculator(tk.Toplevel(self.root))

    def login(self):
        # Get the entered username
        entered_username = self.username_var.get()

        # Update the welcome label
        self.welcome_label.config(text=f"Welcome {entered_username}! ")

def main():
    root = ThemedTk(theme="clearlooks")  # Use a theme of your choice
    app = MainMenu(root)
    root.mainloop()

if __name__ == "__main__":
    main()