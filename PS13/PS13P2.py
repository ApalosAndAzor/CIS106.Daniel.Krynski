#class

class Student:
  def __init__(self, first, last, code):
    self.first = first
    self.last = last
    self.code = code

  def tuition(self, credits):
    if self.code == "I":
      charge = 250.00
    else:
      charge = 500.00
    t = float(credits) * float(charge)
    return t

#main

emp_1 = Student("Corey", "Schafer", "O")
emp_2 = Student("Daniel", "Krynski", "I")

print(emp_1.first)
print(emp_1.last)
print(emp_1.tuition(5))
print(emp_2.first)
print(emp_2.last)
print(emp_2.tuition(5))
