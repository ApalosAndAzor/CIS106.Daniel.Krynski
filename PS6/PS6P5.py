sum_discount_amount = 0

prompt = input(f"Would you like to run the program? (Yes/No)")

while prompt == "Yes":
  quantity_item = int(input(f"How many items? "))
  price_item = float(input(f"What is the price of the items? "))
  extended_price = quantity_item * price_item
  if extended_price > 1000.00:
    discount = 0.25
  else:
    discount = 0.10
  discount_amount = extended_price * discount
  total = extended_price - discount_amount
  print(f"The extended price is {extended_price:.2f}")
  print(f"The discount amount is {discount_amount:.2f}")
  print(f"The total is {total:.2f}")
  sum_discount_amount = sum_discount_amount + discount_amount
  print(f"The current sum of all discount amounts is {sum_discount_amount:.2f}")
  prompt = input(f"Would you like to run the program again? (Yes/No)")
