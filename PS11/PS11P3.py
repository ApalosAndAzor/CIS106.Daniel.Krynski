#function
def display_high_low(last_name_array, score_array):
  l = len(last_name_array)
  high_variable = 0
  low_variable = 999
  for y in range (0, l, 1):
    if int(score_array[y]) > int(high_variable):
      high_index = y
      high_variable = score_array[y]
    if int(score_array[y]) < int(low_variable):
      low_index = y
      low_variable = score_array[y]
  print("The highest score is: ", last_name_array[high_index], score_array[high_index])
  print("The lowest score is: ", last_name_array[low_index], score_array[low_index])

#main
my_file = open("PS11P3.txt", "r")

last_name_array = []
score_array = []

last_name = my_file.readline()

while last_name != "":
  last_name_array.append(str(last_name).rstrip("\n"))
  score = int(my_file.readline())
  score_array.append(score)
  last_name = my_file.readline()
my_file.close()

display_high_low(last_name_array, score_array)
