import csv
from datetime import datetime

def get_income():
    while True:
        try:
            income = float(input("Enter your monthly income: "))
            break
        except ValueError:
            print("Please enter a valid number.")
    return income

def record_expenses():
    expenses = []
    while True:
        expense_type = input("Enter type of expense (e.g. food, rent, etc.):\n--- ")
        while True:
            try:
                amount = float(input("Enter the expense amount: "))
                break
            except ValueError:
                print("Please enter a valid number.")
        expense = {
            "name": expense_type,
            "amount": amount
        }
        expenses.append(expense)
        while True:
            keep_adding = input("Add another? Yes/No ").strip().lower()
            if keep_adding == "no":
                return expenses
            elif keep_adding == "yes":
                break
            else:
                print("Please enter 'yes' or 'no'.")

def calculate_expenses(money, expenses_list):
    print("----Expenses----")
    for expense in expenses_list:
        print(f"{expense['name']} - ${expense['amount']:.2f}")
        money -= expense["amount"]
    print(f"Remaining money: ${money:.2f}")
    return money

def save_to_csv(income, money, expenses_list):
    with open("expenses.csv", mode="w", newline="") as file:
        month = datetime.now().strftime("%Y-%m")
        writer = csv.DictWriter(file, fieldnames=["month", "name", "amount"])
        writer.writeheader()
        for expense in expenses_list:
            writer.writerow({"month": month, "name": expense["name"], "amount": expense["amount"]})
        writer.writerow({"month": month, "name": "Income", "amount": income})
        writer.writerow({"month": month, "name": "Remaining", "amount": money})

def main():
    available_money = get_income()
    my_expenses = record_expenses()
    remaining = calculate_expenses(available_money, my_expenses)
    save_to_csv(available_money, remaining, my_expenses)

if __name__ == "__main__":
    main()