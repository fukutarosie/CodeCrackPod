import tkinter as tk
from tkinter import ttk

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

def main():
    root = tk.Tk()
    app = NecessitiesCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()