my_file = open("PS7P4.txt", 'r')

sum_extended_price = 0
count = 0

item = my_file.readline()
while item != "":
  quantity = my_file.readline()
  price = my_file.readline()
  extended_price = float(quantity) * float(price)
  count = count + 1
  sum_extended_price = sum_extended_price + extended_price
  print(f"Item: {item}")
  print(f"Quantity: {quantity}")
  print(f"Price: ${price}")
  print(f"Extended price: ${extended_price}")
  item = my_file.readline()
my_file.close()

average_order = float(sum_extended_price) / count

print(f"Sum of all the extended prices: ${sum_extended_price}")
print(f"Count of the number of orders: {count}")
print(f"Cost of average order: {average_order}")
