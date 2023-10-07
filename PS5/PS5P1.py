quantity = int(input("How many widgets are you buying?"))

if quantity >= 10000:
  price = 10.00
elif quantity >= 5000:
  price = 20.00
else:
  price = 30.00

extended = quantity * price
tax = extended * 0.07
total = tax + extended

print(f"The extended price is {extended:.2f}")
print(f"The tax amount is {tax:.2f}")
print(f"The total is {total:.2f}")
