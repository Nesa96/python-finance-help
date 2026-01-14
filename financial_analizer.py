import csv
from collections import defaultdict

class FinanceAnalysis:
    """
    A class to process financial records from a CSV file.
    Coming from info of Income, Fixed, and Variable expenses.
    """
    def __init__(self, file_path):
        self.file_path = file_path
        # Using defaultdict to avoid KeyErrors when initializing
        self.metrics = defaultdict(float)
        self.total_expenses = 0
        self.savings = 0

    def process_data(self):
        """Reads the CSV and aggregates values by Category."""
        try:
            with open(self.file_path, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    category = row['Category']
                    amount = float(row['Amount'])
                    
                    self.metrics[category] += amount
                    
            self.total_expenses = self.metrics['Fixed'] + self.metrics['Variable']
            self.savings = self.metrics['Income'] - self.total_expenses
        except FileNotFoundError:
            print(f"Error: The file '{self.file_path}' was not found.")
        except KeyError as e:
            print(f"Error: Missing column in CSV: {e}")

    def update_data(self, category, amount):
        self.metrics[category] += amount         
        self.total_expenses = self.metrics['Fixed'] + self.metrics['Variable']
        self.savings = self.metrics['Income'] - self.total_expenses

    def print_report(self):
        """Calculated financial summary """
        header = "{:^10} | {:^10} | {:^10} | {:^10}".format("INCOME", "FIXED", "VARIABLE", "SAVINGS")
        print("\n" + header)
        print("-" * len(header))
        
        print("{:^10.2f} | {:^10.2f} | {:^10.2f} | {:^10.2f}".format(self.metrics['Income'], self.metrics['Fixed'], self.metrics['Variable'], self.savings))
        print("-" * len(header) + "\n")

    def add_new_row(self):
        """Appends a new record to the CSV file."""
        print("\n--- Write the new values you want to add ---")
        category = input("Category (Income, Fixed, Variable): ")
        amount = input("Amount: ")
        description = input("Description: ")

        with open(self.file_path, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([category, amount, description])
        print("Record added successfully!")
        self.update_data(category, float(amount))

    def goal_savings_plan(self):
        """Calculates extra savings needed for a specific goal."""
        print("We are assuming you can have the same savings as the month in the CSV readed")
        print("\n--- Savings Goal Calculator ---")
        item_price = float(input("How much does the item cost? "))
        months_to_save = int(input("In how many months do you want to buy it? "))

        savings_each_month = item_price / months_to_save
        extra_needed = max(0, savings_each_month - self.savings)

        print(f"\nResults:")
        print("- Your las month savings: {:.2f}".format(self.savings))
        print()
        
        if extra_needed > 0:
            print("You need and extra saving of {:.2f} each month".format(extra_needed))
        else:
            print("With your current savings, you can buy this item on that time.")


def main_menu(file_path):
    analyzer = FinanceAnalysis(file_path)
    analyzer.process_data()
    
    while True:
        print("\n===== FINANCE MANAGER MENU =====")
        print("1. Print CSV Report")
        print("2. Add New row to CSV")
        print("3. Savings Goal Calculator")
        print("4. Exit")
        
        choice = input("\nChoose an option (1-4): ")
        if choice == '1':
            analyzer.print_report()
        elif choice == '2':
            analyzer.add_new_row()
        elif choice == '3':
            analyzer.goal_savings_plan()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    your_file_path = "./expenses_data_january.csv"
    main_menu(your_file_path)

