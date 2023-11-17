#Function - Compute the commission and next years target

def compute(sales):
  if sales > 100000.00:
    commission = sales * 0.10
  else:
    commission = sales * 0.05
  next_year_target = sales * 1.05
  return commission, next_year_target

#Main

last_name = input(f"What is the salesperson's last name? ")
sales = float(input(f"How much were sales? "))
commission, next_year_target = compute(sales)
print(f"The last name of the sale person is {last_name}")
print(f"The commission is ${commission:.2f}")
print(f"The target for next year is ${next_year_target:.2f}")
