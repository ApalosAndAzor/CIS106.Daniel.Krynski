#Function - Display the array

def display(last_name_array, batting_average_array):
  q = len(last_name_array)
  print(f"In order:")
  for x in range (0, q, 1):
    print(last_name_array[x], batting_average_array[x])

#Function - Search the array
def seqsearch(last_name_array, batting_average_array, search_name):
  l = len(last_name_array)
  for y in range(0, l, 1):
    if last_name_array[y] == search_name:
      sindex = y
  print(last_name_array[sindex], "has a batting average of", batting_average_array[sindex])

#main
my_file = open("PS11P4.txt", "r")

last_name_array = []
batting_average_array = []

last_name = my_file.readline()

while last_name != "":
  last_name_array.append(str(last_name).rstrip("\n"))
  batting_average = float(my_file.readline())
  batting_average_array.append(batting_average)
  last_name = my_file.readline()
my_file.close()

display(last_name_array, batting_average_array)

response = input(f"Would you like to search for a last name and batting average? (Y/N):")

while response == "Y":
  search_name = input(f"Enter last name to search for: ")
  seqsearch(last_name_array, batting_average_array, search_name)
  response = input(f"Would you like to run the search again? (Y/N):")
