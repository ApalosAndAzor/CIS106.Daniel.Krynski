#Function
def compute(month, sales):
  if month == "Jan" or month == "Feb" or month == "Mar":
    forecast_percent = 0.10
  elif month == "Apr" or month == "May" or month == "Jun":
    forecast_percent = 0.15
  elif month == "Jul" or month == "Aug" or month == "Sep":
    forecast_percent = 0.20
  else:
    forecast_percent = 0.25
  next_month_sale = sales * (1 + forecast_percent)
  return next_month_sale

#Main

prompt = input(f"Would you like to run the program? (Y/N):")

while prompt == "Y":
  last_name = input(f"What is your last name? ")
  month  = input(f"Which month is it? (Jan, Feb, Mar, etc...) ")
  sales = float(input(f"How much were sales? "))
  next_month_sale = compute(month, sales)
  print(f"{last_name} your forecast for next months sales is ${next_month_sale}")
  prompt = input(f"Would you like to run the program again? (Y/N):")