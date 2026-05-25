income = float(input("Enter your monthly income: "))
expenses = input("Enter your expenses (space-separated): ")
expense_list = expenses.split()
total_expense = 0
for expense in expense_list:
    total_expense += float(expense)
remaining_budget = income - total_expense
print("Remaining budget: $%.2f" % remaining_budget)