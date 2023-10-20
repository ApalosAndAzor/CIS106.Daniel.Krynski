accumulated_interest = 0.00

prompt = input(f"Would you like to a 5 year interest account? (Yes/No): ")

while prompt == "Yes":
  principle_amount = float(input(f"What is your starting principle amount? "))
  interest_rate = float(input(f"What is your interest rate? "))
  print(f"Year | Beginning Balance | Ending Balance")
  for year in range(1, 6, 1):
    annual_interest = principle_amount * interest_rate
    ending_balance = principle_amount + annual_interest
    print(f"{year:2} {principle_amount:12.2f} {ending_balance:19.2f}")
    accumulated_interest = accumulated_interest + annual_interest
    principle_amount = ending_balance
  print(f"Accumulated interest earned overall: {accumulated_interest:.2f}")
  prompt = input(f"Would you like to calculated another 5 year interest account? (Yes/No): ")
