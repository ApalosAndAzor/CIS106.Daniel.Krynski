print("Enter the Item, it will be A or B")
item = input()
print("Enter the quantity of the item")
quantity = int(input())
if item == "A":
  unitPrice = 10.00
else:
  unitPrice = 20.00
extendedPrice = quantity * unitPrice
print("Item " + item)
print("Has a unit price of " + str(unitPrice))
print("And a extended price of " + str(extendedPrice))
