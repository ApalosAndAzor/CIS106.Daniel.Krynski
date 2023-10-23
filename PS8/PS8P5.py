#function - district code - compute - cost per hour
def compute(credit_hours, district_code):
  if district_code == "I":
    credit_charge = 250.00
  else:
    credit_charge = 500.00
  tuition = credit_charge * credit_hours
  return tuition

#main

total_all_tuition = 0.00

prompt = input(f"Would you like to run the program? (Y/N):")

while prompt == "Y":
  last_name = input(f"What is your last name? ")
  credit_hours  = int(input(f"How many credit hours are you taking? "))
  district_code = input(f"What is your district code? (I/O) ")
  tuition = compute(credit_hours, district_code)
  print(f"{last_name} your tuition owed is ${tuition}")
  total_all_tuition = total_all_tuition + tuition
  prompt = input(f"Would you like to run the program again? (Y/N):")

print(f"This is the total tuition cost for all students: ${total_all_tuition}")
