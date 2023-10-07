last_name = input("What is your last name? ")
salary = float(input("What is your slary? "))
job_level = int(input("What is your job level? "))

if job_level >= 10:
  bonus_rate = 0.25
elif job_level >= 5:
  bonus_rate = 0.20
else:
  bonus_rate = 0.10

bonus = salary * bonus_rate

print(f"{last_name} your bonus is {bonus}")
