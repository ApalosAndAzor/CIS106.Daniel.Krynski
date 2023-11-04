#Function - Compute the assessed value

def compute(county, market_value):
  if county == "Cook":
    assessed_value_percent = 0.90
  elif county == "DuPage":
    assessed_value_percent = 0.80
  elif county == "McHenry":
    assessed_value_percent = 0.75
  elif county == "Kane":
    assessed_value_percent = 0.60
  else:
    assessed_value_percent = 0.70
  assessed_value = market_value * assessed_value_percent
  return assessed_value

#Main

all_market = 0.00
all_assessed = 0.00

prompt = input(f"Would you like to run the program? (Y/N):")

while prompt == "Y":
  county = input(f"What county is your property located? ")
  market_value  = float(input(f"What is the market value of your property? "))
  assessed_value = compute(county, market_value)
  all_market = all_market + market_value
  all_assessed = all_assessed + assessed_value
  print(f"Your property has a assessed value of ${assessed_value}.")
  prompt = input(f"Would you like to run the program again? (Y/N):")

print(f"The sum of all market value properties is ${all_market}")
print(f"The sum of all assessed value properties is ${all_assessed}")
