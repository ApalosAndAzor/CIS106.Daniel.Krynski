#Function - Compute the ticket price

def compute(miles_chicago):
  if miles_chicago >= 30:
    ticket_price = 12
  elif miles_chicago >= 20:
    ticket_price = 10
  elif miles_chicago >= 10:
    ticket_price = 8
  else:
    ticket_price = 5
  return ticket_price

#Main

sum_tickets = 0.00

prompt = input(f"Would you like to run the program? (Y/N):")

while prompt == "Y":
  last_name = input(f"What is your last name? ")
  miles_chicago  = int(input(f"How many miles from downtown Chicago? "))
  ticket_price = compute(miles_chicago)
  sum_tickets = sum_tickets + ticket_price
  print(f"{last_name}, the ticket price is ${ticket_price}.")
  prompt = input(f"Would you like to run the program again? (Y/N):")

print(f"The sum of all tickets is ${sum_tickets}")
