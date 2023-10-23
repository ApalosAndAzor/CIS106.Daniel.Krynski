#function - to compute batting average
def average(number_of_hits, at_bats):
  batting_average = number_of_hits / at_bats
  return batting_average

# main
number_of_players = 0.0

prompt = input(f"Would you like to run the program? (Y/N):")

while prompt == "Y":
  player_last_name = input(f"What is the players last name? ")
  number_of_hits = int(input(f"How many hits? "))
  at_bats = int(input(f"How many at bats?" ))
  batting_average = average(number_of_hits, at_bats)
  print(f"{player_last_name}, their batting average is {batting_average}")
  number_of_players = number_of_players + 1
  prompt = input(f"Would you like to run the program again? (Y/N):")

print(f"The number of players entered is {number_of_players}")
