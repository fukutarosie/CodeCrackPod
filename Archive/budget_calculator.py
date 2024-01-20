import tkinter as tk
from tkinter import ttk
from subprocess import run

class BudgetCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Budget Calculator")

        # Create variables
        self.income_var = tk.DoubleVar()
        self.necessities_var = tk.DoubleVar()
        self.tertiary_needs_var = tk.DoubleVar()
        self.savings_var = tk.DoubleVar()

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

    def create_widgets(self):
        # Disclaimer
        disclaimer_label = tk.Label(self.root, text="DISCLAIMER: THE FOLLOWING CALCULATOR IS JUST GENERALIZATION AND PRONE TO BIAS, AND INTENDED TO BE USED AS A REFERENCE.\nIT IS ADVISED THAT USERS HAVE TO BUDGET AND INVEST ACCORDING TO THEIR NEEDS AND PRIORITIES", font=("Arial", 15), foreground="red")
        disclaimer_label.pack(pady=10)

        # Label and Entry for Income
        income_label = ttk.Label(self.root, text="Enter Your Monthly Income ($):", style="Label.TLabel")
        income_entry = ttk.Entry(self.root, textvariable=self.income_var, style="Entry.TEntry")

        # Button to Calculate Budget
        calculate_button = ttk.Button(self.root, text="Calculate Budget", command=self.calculate_budget, style="Button.TButton")

        # Labels to display budget allocations
        necessities_label = ttk.Label(self.root, text="Necessities:", style="Label.TLabel")
        tertiary_needs_label = ttk.Label(self.root, text="Tertiary Needs:", style="Label.TLabel")
        savings_label = ttk.Label(self.root, text="Savings and Investments:", style="Label.TLabel")

        # Entry widgets to display calculated values
        necessities_entry = ttk.Entry(self.root, textvariable=self.necessities_var, state="readonly", style="Entry.TEntry")
        tertiary_needs_entry = ttk.Entry(self.root, textvariable=self.tertiary_needs_var, state="readonly", style="Entry.TEntry")
        savings_entry = ttk.Entry(self.root, textvariable=self.savings_var, state="readonly", style="Entry.TEntry")

        # Pack UI elements
        disclaimer_label.pack(pady=10)
        income_label.pack(pady=5)
        income_entry.pack(pady=5)
        calculate_button.pack(pady=10)
        necessities_label.pack(pady=5)
        necessities_entry.pack(pady=5)
        tertiary_needs_label.pack(pady=5)
        tertiary_needs_entry.pack(pady=5)
        savings_label.pack(pady=5)
        savings_entry.pack(pady=5)

        # Button to open Necessities Analysis
        necessities_analysis_button = ttk.Button(self.root, text="Give Further Analysis for Necessities", command=self.open_necessities_analysis, style="Button.TButton")
        necessities_analysis_button.pack(pady=10)

        # Button to open Investment Analysis
        investment_analysis_button = ttk.Button(self.root, text="Give Further Analysis for Savings and Investments", command=self.open_investment_analysis, style="Button.TButton")
        investment_analysis_button.pack(pady=10)

    def calculate_budget(self):
        income = self.income_var.get()

        if income:
            if income < 5000:
                # Budget allocation for income < $5000 (70-20-10)
                necessities_percentage = 0.7
                tertiary_needs_percentage = 0.2
                savings_percentage = 0.1
            else:
                # Budget allocation for income >= $5000 (50-30-20)
                necessities_percentage = 0.5
                tertiary_needs_percentage = 0.3
                savings_percentage = 0.2

            necessities = necessities_percentage * income
            tertiary_needs = tertiary_needs_percentage * income
            savings = savings_percentage * income

            self.necessities_var.set(necessities)
            self.tertiary_needs_var.set(tertiary_needs)
            self.savings_var.set(savings)

    def open_necessities_analysis(self):
        self.necessities_analysis_window = tk.Toplevel(self.root)
        app = NecessitiesCalculator(self.necessities_analysis_window)

    def open_investment_analysis(self):
        self.investment_analysis_window = tk.Toplevel(self.root)
        app = InvestmentAnalyzer(self.investment_analysis_window)

class NecessitiesCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Necessities Calculator")

        # Create variables
        self.necessities_var = tk.DoubleVar()
        self.total_necessities_var = tk.DoubleVar()
        self.housing_var = tk.DoubleVar()
        self.electricities_var = tk.DoubleVar()
        self.food_var = tk.DoubleVar()
        self.mobile_data_var = tk.DoubleVar()
        self.transport_var = tk.DoubleVar()
        self.insurance_var = tk.DoubleVar()
        self.housing_amenities_var = tk.DoubleVar()

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

    def create_widgets(self):
        # Entry for Total Necessities Amount
        total_necessities_label = ttk.Label(self.root, text="Enter Total Necessities Amount ($):", style="Label.TLabel")
        total_necessities_entry = ttk.Entry(self.root, textvariable=self.total_necessities_var, style="Entry.TEntry")

        # Button to Calculate Necessities
        calculate_button = ttk.Button(self.root, text="Calculate Necessities", command=self.calculate_necessities, style="Button.TButton")

        # Labels and Entry widgets for Necessities
        housing_label = ttk.Label(self.root, text="Housing:")
        electricities_label = ttk.Label(self.root, text="Electricities:")
        food_label = ttk.Label(self.root, text="Food and Drink:")
        mobile_data_label = ttk.Label(self.root, text="Mobile Data:")
        transport_label = ttk.Label(self.root, text="Transport:")
        insurance_label = ttk.Label(self.root, text="Insurance:")
        housing_amenities_label = ttk.Label(self.root, text="Housing Amenities:")

        housing_entry = ttk.Entry(self.root, textvariable=self.housing_var, state="readonly")
        electricities_entry = ttk.Entry(self.root, textvariable=self.electricities_var, state="readonly")
        food_entry = ttk.Entry(self.root, textvariable=self.food_var, state="readonly")
        mobile_data_entry = ttk.Entry(self.root, textvariable=self.mobile_data_var, state="readonly")
        transport_entry = ttk.Entry(self.root, textvariable=self.transport_var, state="readonly")
        insurance_entry = ttk.Entry(self.root, textvariable=self.insurance_var, state="readonly")
        housing_amenities_entry = ttk.Entry(self.root, textvariable=self.housing_amenities_var, state="readonly")

        # Pack UI elements
        total_necessities_label.pack(pady=5)
        total_necessities_entry.pack(pady=5)
        calculate_button.pack(pady=10)
        housing_label.pack(pady=5)
        housing_entry.pack(pady=5)
        electricities_label.pack(pady=5)
        electricities_entry.pack(pady=5)
        food_label.pack(pady=5)
        food_entry.pack(pady=5)
        mobile_data_label.pack(pady=5)
        mobile_data_entry.pack(pady=5)
        transport_label.pack(pady=5)
        transport_entry.pack(pady=5)
        insurance_label.pack(pady=5)
        insurance_entry.pack(pady=5)
        housing_amenities_label.pack(pady=5)
        housing_amenities_entry.pack(pady=5)

    def calculate_necessities(self):
        total_necessities = self.total_necessities_var.get()

        # Calculate necessities allocations based on user input
        self.housing_var.set(0.6 * total_necessities)
        self.electricities_var.set(0.1 * total_necessities)
        self.food_var.set(0.15 * total_necessities)
        self.mobile_data_var.set(0.05 * total_necessities)
        self.transport_var.set(0.025 * total_necessities)
        self.insurance_var.set(0.05 * total_necessities)
        self.housing_amenities_var.set(0.025 * total_necessities)

        # Update total necessities value
        self.necessities_var.set(total_necessities)

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
    app = BudgetCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
