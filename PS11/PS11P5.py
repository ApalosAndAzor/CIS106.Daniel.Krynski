#Function - Display the array

def display(last_name_array, batting_average_array):
  q = len(last_name_array)
  print(f"In order:")
  for x in range (0, q, 1):
    print(last_name_array[x], batting_average_array[x])

#Function - Search the array
def seqsearch(last_name_array, sname):
  l = len(last_name_array)
  sindex = -1
  for y in range(0, l, 1):
    if last_name_array[y] == sname:
      sindex = y
  return sindex

#main
my_file = open("PS11P5.txt", "r")

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
  sname = input(f"Enter last name to search for: ")
  sindex = seqsearch(last_name_array, sname)
  if sindex == -1:
    print(sname, " is not in the array.")
  else:
    print(last_name_array[sindex], " has a batting average of ", batting_average_array[sindex])
  response = input(f"Would you like to run the search again? (Y/N):")
