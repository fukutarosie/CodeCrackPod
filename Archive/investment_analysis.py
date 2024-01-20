import tkinter as tk
from tkinter import ttk

class InvestmentAnalyzer:
    def __init__(self, root):
        self.root = root
        self.root.title("Investment Analyzer")

        # Create variables
        self.total_budget_var = tk.DoubleVar()
        self.risk_level_var = tk.StringVar()

        # Create styles
        self.create_styles()

        # Create UI elements
        self.create_widgets()

    def create_styles(self):
        self.style = ttk.Style()

        # Configure label style
        self.style.configure("Label.TLabel", font=("Comic Sans", 12), foreground="black")

        # Configure entry style
        self.style.configure("Entry.TEntry", font=("Comic Sans", 12), foreground="black")

        # Configure button style
        self.style.configure("Button.TButton", font=("Comic Sans", 12), foreground="black", background="blue")

        # Configure radio button style
        self.style.configure("TRadiobutton", font=("Comic Sans", 12), foreground="black")
    
    def create_widgets(self):
        # Entry for Total Savings and Investment Budget
        total_budget_label = ttk.Label(self.root, text="Enter Total Savings and Investment Budget ($):", style="Label.TLabel")
        total_budget_entry = ttk.Entry(self.root, textvariable=self.total_budget_var, style="Entry.TEntry")

        # Label for Risk Level
        risk_level_label = ttk.Label(self.root, text="Choose Your Risk Level:", style="Label.TLabel")

        # Radio buttons for Risk Level
        low_risk_radio = ttk.Radiobutton(self.root, text="Low Risk", variable=self.risk_level_var, value="Low Risk")
        moderate_risk_radio = ttk.Radiobutton(self.root, text="Moderate Risk", variable=self.risk_level_var, value="Moderate Risk")
        high_risk_radio = ttk.Radiobutton(self.root, text="High Risk", variable=self.risk_level_var, value="High Risk")

        # Button to Analyze Investments
        analyze_button = ttk.Button(self.root, text="Analyze Investments", command=self.analyze_investments, style="Button.TButton")

        # Pack UI elements
        total_budget_label.pack(pady=5)
        total_budget_entry.pack(pady=5)
        risk_level_label.pack(pady=10)
        low_risk_radio.pack(pady=5)
        moderate_risk_radio.pack(pady=5)
        high_risk_radio.pack(pady=5)
        analyze_button.pack(pady=10)

    def analyze_investments(self):
        total_budget = self.total_budget_var.get()
        risk_level = self.risk_level_var.get()

        if total_budget and risk_level:
            # Create a new window for displaying investment analysis
            analysis_window = tk.Toplevel(self.root)
            analysis_window.title("Investment Analysis")

            # Create labels to display investment analysis
            analysis_label = ttk.Label(analysis_window, text="Investment Analysis:", style="Label.TLabel")

            if risk_level == "Low Risk":
                # Less Risk Allocation
                mutual_funds_allocation = 0.3 * total_budget
                government_bond_allocation = 0.3 * total_budget
                savings_account_allocation = 0.25 * total_budget
                stocks_allocation = 0.15 * total_budget

                # Display the allocation
                analysis_text = f"Allocations for Low Risk:\n" \
                                f"Mutual Funds & Funds: ${mutual_funds_allocation:.2f}\n" \
                                f"Government Bond: ${government_bond_allocation:.2f}\n" \
                                f"Savings Account/Cash: ${savings_account_allocation:.2f}\n" \
                                f"Stocks: ${stocks_allocation:.2f}"

            elif risk_level == "Moderate Risk":
                # Moderate Risk Allocation
                mutual_funds_allocation = 0.25 * total_budget
                corporate_bonds_allocation = 0.2 * total_budget
                stocks_allocation = 0.25 * total_budget
                government_bond_allocation = 0.15 * total_budget
                savings_account_allocation = 0.15 * total_budget

                # Display the allocation
                analysis_text = f"Allocations for Moderate Risk:\n" \
                                f"Mutual Funds & Funds: ${mutual_funds_allocation:.2f}\n" \
                                f"Corporate Bonds: ${corporate_bonds_allocation:.2f}\n" \
                                f"Stocks: ${stocks_allocation:.2f}\n" \
                                f"Government Bond: ${government_bond_allocation:.2f}\n" \
                                f"Savings Account/Cash: ${savings_account_allocation:.2f}"

            elif risk_level == "High Risk":
                # High Risk Allocation
                cryptocurrency_allocation = 0.2 * total_budget
                mini_bonds_allocation = 0.2 * total_budget
                stocks_allocation = 0.25 * total_budget
                cash_allocation = 0.15 * total_budget
                mutual_funds_allocation = 0.1 * total_budget
                corporate_bonds_allocation = 0.1 * total_budget

                # Display the allocation
                analysis_text = f"Allocations for High Risk:\n" \
                                f"Cryptocurrency: ${cryptocurrency_allocation:.2f}\n" \
                                f"Mini-Bonds: ${mini_bonds_allocation:.2f}\n" \
                                f"Stocks: ${stocks_allocation:.2f}\n" \
                                f"Cash/Savings Account: ${cash_allocation:.2f}\n" \
                                f"Mutual Funds & Funds: ${mutual_funds_allocation:.2f}\n" \
                                f"Corporate Bonds: ${corporate_bonds_allocation:.2f}"

            else:
                analysis_text = "Invalid risk level."

            # Display the analysis
            analysis_label.pack(pady=10)
            ttk.Label(analysis_window, text=analysis_text, style="Label.TLabel").pack(pady=10)

def main():
    root = tk.Tk()
    app = InvestmentAnalyzer(root)
    root.mainloop()

if __name__ == "__main__":
    main()
