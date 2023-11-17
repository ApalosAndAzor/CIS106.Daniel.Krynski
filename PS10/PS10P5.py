#Function - Compute the total and tax, plus make them global

def compute(quantity_item, unit_price):
  global total
  total = quantity_item * unit_price
  global tax
  tax = total * 0.07
  return total, tax

#Main

quantity_item = int(input(f"What is the quantity of the item? "))
unit_price = float(input(f"What is the unit price of the item? "))
total, tax = compute(quantity_item, unit_price)
print(f"The total price is ${total:.2f}")
print(f"The tax is ${tax:.2f}")
