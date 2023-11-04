#Function - Compute the out the door price

def compute(msrp, make, model, electric):
  if make == "Honda" and model == "Accord":
    percent_off = 0.10
  elif make == "Toyota" and model == "Rav4":
    percent_off = 0.15
  elif electric == "Y":
    percent_off = 0.30
  else:
    percent_off = 0.05
  new_msrp = msrp - (percent_off * msrp)
  total = new_msrp + (new_msrp * 0.07)
  return total

#Main

sum_msrp = 0.00
sum_total = 0.00

prompt = input(f"Would you like to run the program? (Y/N):")

while prompt == "Y":
  make = input(f"What is the make of the automobile? ")
  model  = input(f"What is the model of the automobile? ")
  electric = input(f"Is the automobile electric? (Y/N) ")
  msrp = float(input(f"What is the sticker price of the automobile? "))
  total = compute(msrp, make, model, electric)
  sum_msrp = sum_msrp + msrp
  sum_total = sum_total + total
  print(f"The total of your automobile is ${total}.")
  prompt = input(f"Would you like to run the program again? (Y/N):")

print(f"The sum of all msrp is ${sum_msrp}")
print(f"The sum of all sale price is ${sum_total}")
