my_file = open("PS7P5.txt", "r")

sum_tuition = 0.0
count = 0

last_name = str(my_file.readline().rstrip('\n'))

while last_name != "":
  district_code = str(my_file.readline().rstrip('\n'))
  number_credits = float(my_file.readline())
  
  if district_code == "I":
    cost_credit = 250.00
  else:
    cost_credit = 500.00
  
  compute_tuition = number_credits * cost_credit
  count = count + 1
  sum_tuition = sum_tuition + compute_tuition
  
  print(f"Last name: {last_name}")
  print(f"Credits taken: {number_credits}")
  print(f"Tuition owed: ${compute_tuition}")
  print(f"")
  
  last_name = str(my_file.readline().rstrip('\n'))

my_file.close()

print(f"Sum of all tuition owed: ${sum_tuition}")
print(f"Number of student: {count}")
