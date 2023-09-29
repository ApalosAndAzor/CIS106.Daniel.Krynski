print("How many books do you need to order?")
books = int(input())
print("How much does each book cost?")
cost = float(input())
order = books * cost
if order > 50.00:
  ship = 0.00
else:
  ship = 25.00
print("The order total is " + str(order))
print("And the shipping charge is " + str(ship))
