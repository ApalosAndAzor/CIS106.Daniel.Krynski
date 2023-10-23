# function - compute the total
def total(quantity, price):
  compute_total = quantity * price
  if compute_total > 10000.00:
    discount = compute_total * 0.10
  else:
    discount = 0
  grand_total = compute_total - discount
  return grand_total

# main
sum_extended_price = 0.0

prompt = input(f"Would you like to run the program? (Y/N):")

while prompt == "Y":
  quantity = int(input(f"How many units? "))
  price = float(input(f"What is the price of each unit? "))
  grand_total = total(quantity, price)
  sum_extended_price = sum_extended_price + grand_total
  print(f"The quantity is {quantity}")
  print(f"The price is {price}")
  print(f"The total is {grand_total}")
  prompt = input(f"Would you like to run the program again? (Y/N):")

print(f"The sum of all the totals is {sum_extended_price}")
