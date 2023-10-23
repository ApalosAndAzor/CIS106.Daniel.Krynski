#function - compute miles per gallon
def compute(miles_travelled, gallons_used):
  miles_per_gallon = miles_travelled / gallons_used
  return miles_per_gallon

#main
number_of_trips = 0

prompt = input(f"Would you like to run the program? (Y/N):")

while prompt == "Y":
  destination_city = input(f"What is the destination city? ")
  miles_travelled = float(input(f"How many miles have you travelled? "))
  gallons_used = float(input(f"How many gallons have you used? "))
  miles_per_gallon = compute(miles_travelled, gallons_used)
  number_of_trips = number_of_trips + 1
  print(f"Your end point is {destination_city}")
  print(f"You travelled {miles_travelled} miles")
  print(f"Your MPG is {miles_per_gallon}")
  prompt = input(f"Would you like to run the program again? (Y/N):")

print(f"The number of trips entered is {number_of_trips}")
