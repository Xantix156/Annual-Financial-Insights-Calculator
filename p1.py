def analyze_finances(expenses, monthly_salary):
    # Initialize total expenses and a dictionary to store category-wise totals
    total_spent = 0
    total_expenses_by_category = {}

    # Loop through each category in the expenses dictionary
    for category, expense_list in expenses.items():
        # Calculate the total expenses for the current category
        total_expense_in_category = sum(expense_list)
        # Add the category total to the overall total
        total_spent += total_expense_in_category
        # Store the total for the current category in the dictionary
        total_expenses_by_category[category] = total_expense_in_category

    # Calculate annual income from the monthly salary
    annual_income = monthly_salary * 12
    # Calculate annual savings as the difference between income and total expenses
    annual_savings = annual_income - total_spent
    # Calculate the average monthly expenses
    average_monthly_expenses = total_spent / 12

    # Print the calculated financial details
    print("Annual Income:", round(annual_income, 2))
    print("Total Annual Expenses:", round(total_spent, 2))
    print("Annual Savings:", round(annual_savings, 2))
    print("Average Monthly Expenses:", round(average_monthly_expenses, 2))

    # Print the percentage breakdown of expenses by category
    print("Percentage of Expenses by Category:")
    for category, total_expense in total_expenses_by_category.items():
        # Calculate the percentage of total expenses for each category
        percentage = (total_expense / total_spent) * 100
        print(category, f"{round(percentage, 2)}%")

# Input data: monthly expenses by category
expenses = {
    "Food": [120, 150, 110, 140, 160, 130, 145, 155, 125, 135, 115, 125],
    "Transport": [50, 55, 60, 45, 65, 55, 60, 50, 40, 45, 55, 50],
    "Entertainment": [80, 75, 90, 85, 70, 80, 95, 65, 60, 75, 85, 90],
    "Health": [100, 95, 110, 120, 105, 90, 115, 105, 110, 100, 95, 105]
}

# User input
monthly_salary = float(input("Enter your monthly salary: "))

# Function call to analyze financial data
analyze_finances(expenses, monthly_salary)