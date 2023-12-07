#class

class Employee:
  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + "." + last + "@company.com"

  def fullname(self):
    return "{} {}".format(self.first, self.last)

  def bonus(self, rate):
    b = float(rate) * float(self.pay)
    return b

#main

emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Daniel", "Krynski", 60000)

print(emp_1.fullname())
print(emp_1.bonus(0.10))
print(emp_1.bonus(0.20))
print(emp_2.fullname())
print(emp_2.bonus(0.10))
print(emp_2.bonus(0.20))