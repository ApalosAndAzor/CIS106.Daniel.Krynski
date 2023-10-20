my_file = open("PS7P3.txt" , "r")

total_bonus = 0

last_name = my_file.readline()
while last_name != "":
  salary = my_file.readline()
  print()
  print(f"Employee last name: {last_name}")
  print(f"Employee Salary: $ {salary}")
  if float(salary) > 100000.00:
    bonus = float(salary) * 0.20
  elif float(salary) > 50000.00:
    bonus = float(salary) * 0.15
  else:
    bonus = float(salary) * 0.10
  print(f"Employee Bonus: $ {bonus}")
  total_bonus = total_bonus + bonus
  last_name = my_file.readline()
my_file.close()
print(f"Sum of all bonuses: $ {total_bonus}")
