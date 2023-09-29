print("How many items do you have?")
quantity = int(input())
if quantity >= 1000:
  price = 3.00
else:
  price = 5.00
extendedPrice = quantity * price
tax = 0.07 * extendedPrice
total = extendedPrice + tax
print("Here is the quantity: " + str(quantity))
print("The unit price: " + str(price))
print("The extended price: " + str(extendedPrice))
print("The tax: " + str(tax))
print("And the total: " + str(total))
