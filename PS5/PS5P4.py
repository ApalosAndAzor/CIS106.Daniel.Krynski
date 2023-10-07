number_of_concert_tickets = int(input("How many tickets are you buying? "))

if number_of_concert_tickets >= 25:
  price_per_ticket = 50
elif number_of_concert_tickets >= 10:
  price_per_ticket = 60
elif number_of_concert_tickets >= 5:
  price_per_ticket = 70
else:
  price_per_ticket = 75

total_cost = number_of_concert_tickets * price_per_ticket

print(f"The number of concert tickets is {number_of_concert_tickets}")
print(f"The price per ticket is {price_per_ticket}")
print(f"The total cost is {total_cost}")
