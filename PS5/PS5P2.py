partNumber = int(input("What is the part number?"))
quantity = int(input("How much of the part do you need?"))

if partNumber == 10 or partNumber == 55:
  unitCost = 1.00
elif partNumber == 99:
  unitCost = 2.00
elif partNumber == 80 or partNumber == 70:
  unitCost = 3.00
else:
  unitCost = 5.00

totalCost = quantity * unitCost

print(f"The part number is {partNumber}")
print(f"The cost per unit is {unitCost}")
print(f"The total cost is {totalCost}")
