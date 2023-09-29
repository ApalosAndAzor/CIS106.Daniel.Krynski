print("What is your last name?")
last_name = input()
print("How many dependents do you have?")
number_of_dependents = int(input())
print("What is your gross income?")
gross_income = float(input())
adjusted_gross_income = gross_income - number_of_dependents * 12000
if adjusted_gross_income > 50000:
  income_tax_rate = 0.20
else:
  income_tax_rate = 0.10
income_tax = adjusted_gross_income * income_tax_rate
if income_tax < 0:
  income_tax = 100
print(last_name + " your gross income is " + str(gross_income))
print("You have " + str(number_of_dependents) + " number of dependents")
print("Your adjusted gross income is " + str(adjusted_gross_income))
print("And your income tax is " + str(income_tax))
