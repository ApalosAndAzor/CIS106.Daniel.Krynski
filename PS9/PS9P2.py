#Function - Square footage and gallons needed

def compute(length, width, height):
  square_footage = (2 * length * width) + (2 * length * height) + (2 * width * height)
  gallons_needed = square_footage / 50
  return gallons_needed

#Main

prompt = input(f"Would you like to run the program? (Y/N):")

while prompt == "Y":
  length = float(input(f"What is the length of the room? "))
  width  = float(input(f"What is the width of the room? "))
  height = float(input(f"What is the height of the room? "))
  gallons_needed = compute(length, width, height)
  print(f"You need {gallons_needed} gallons to paint the room.")
  prompt = input(f"Would you like to run the program again? (Y/N):")
  