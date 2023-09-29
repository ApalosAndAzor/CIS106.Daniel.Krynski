print("Waht is the brand name of the appliance?")
name = input()
print("How much did the appliance cost?")
cost = float(input())
if cost > 1000:
  warrantee = 0.10 * cost
else:
  warrantee = 0.05 * cost
total = cost + warrantee
print("The " + name + " appliance")
print("Has a warrantee cost of " + str(warrantee))
print("And a total cost of " + str(total))
