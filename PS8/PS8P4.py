#function - job code - compute - pay rate
def compute(job_code):
  if job_code == "L":
    pay_rate = 25.00
  elif job_code == "A":
    pay_rate = 30.00
  else:
    pay_rate = 50.00
  return pay_rate

#main

total_gross_pay = 0.00

prompt = input(f"Would you like to run the program? (Y/N):")

while prompt == "Y":
  last_name = input(f"What is your last name? ")
  job_code = input(f"What is your job code? (L/A/J) ")
  hours_worked  = int(input(f"What is your hours worked? "))
  pay_rate = compute(job_code)
  if hours_worked >= 40:
    gross_pay = (pay_rate * 40) + ((hours_worked - 40) * (pay_rate * 1.5))
  else:
    gross_pay = hours_worked * pay_rate
  total_gross_pay = total_gross_pay + gross_pay
  print(f"{last_name} your gross pay is ${gross_pay}")
  prompt = input(f"Would you like to run the program again? (Y/N):")

print(f"This is the total gross pay for all employees: ${total_gross_pay}")
