number_of_employees = 0
sum_of_gross_pay = 0

prompt = input(f"Would you like to figure out your gross pay? (Yes/No) ")

while prompt == "Yes":
  number_of_employees = number_of_employees + 1
  last_name = input(f"What is your last name? ")
  hours_worked = float(input(f"How many hours did you work? "))
  rate_of_pay = float(input(f"What is your hourly rate? "))
  if hours_worked >= 40:
    gross_pay = (rate_of_pay * 40) + ((hours_worked - 40) * (rate_of_pay * 1.5))
  else:
    gross_pay = hours_worked * rate_of_pay
  sum_of_gross_pay = sum_of_gross_pay + gross_pay
  print(f"{last_name} your gross pay is {gross_pay}")
  prompt = input(f"Would you like to add more data? (Yes/No) ")

average_pay = sum_of_gross_pay / number_of_employees

print(f"This is the sum of gross pay for every employee: {sum_of_gross_pay}")
print(f"This is how many employees entered data: {number_of_employees}")
print(f"This is the average pay of all the gross pay: {average_pay:.2f}")
