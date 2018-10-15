# P4HW1-Budget Analysis
# 26 Sept 2018
# CTI-110
# Kayla Ward
# Enter budgeting amount. 
# Enter each expense for the for the month using a while loop.
# Keep a running total and when loop is finished, tell the user if they were
# under or over budget.

user_budget = float(input("Please enter how much you've budgeted for the month: "))
more_expenses = "y"
total_expenses = 0

while more_expenses =="y":
    user_expenses = float(input("Enter an expense: "))
    total_expenses += user_expenses
    more_expenses = input("Do you have more expenses?: Type y " + \
                          "for yes, any key for no: ")
print()
if total_expenses > user_budget:
    print('You were over your budget of',"$" + format(user_budget, ",.2f"), \
          'by $', format(totla_expenses - user_budget, ",.2f"))
elif user_budget > total_expenses:
    print('You were under your budget of',"$" + format(user_budget, ",.2f", \
        'by $', format(user_budget -total_expenses, ",.2f"))
else:
    print('You used exactly you budget of',"$" + format(user_budget, ",.2f"), '.')
