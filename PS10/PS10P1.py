#Function - Compute the discount amount and price

def compute(quantity, price, discount_rate):
  discounted_price = price - (price * discount_rate)
  discount_amount = quantity * discounted_price
  return discounted_price, discount_amount

#Main

quantity = int(input(f"What is the quanitity? "))
price = float(input(f"What is the price? "))
discount_rate = float(input(f"What is the discount rate? "))
discount_amount, discounted_price = compute(quantity, price, discount_rate)
print(f"The quantity is {quantity}")
print(f"The full price is ${price:.2f}")
print(f"The discount amount is ${discount_amount:.2f}")
print(f"The discounted price is ${discounted_price:.2f}")
