principleAmount = int(input("What is the principle amount of the CD? "))
yearToMaturity = int(input("How many years to maturity of the CD? "))

if principleAmount > 100000 and yearToMaturity == 5:
  interestRate = 0.06
elif principleAmount >= 50000 and yearToMaturity == 10:
  interestRate = 0.05
elif principleAmount >= 50000 and yearToMaturity == 5:
  interestRate = 0.04
else:
  interestRate = 0.02

firstYearInterest = principleAmount * interestRate

print(f"The principle is {principleAmount}")
print(f"The interest rate is {interestRate}")
print(f"The interest amount for the first year is {firstYearInterest}")
