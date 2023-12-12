#super class

class Car:
  def __init__(self, make, model, sticker):
    self.make = make
    self.model = model
    self.sticker = sticker

  def discount(self):
    b = 0.90 * float(self.sticker)
    return b

#sub class

class Sport(Car):
  def sport_wheels(self):
    a = 1000.00
    return a
  def sport_engine(self):
    b = 3000.00
    return b
  def sport_interior(self):
    c = 2000.00
    return c
  def price_with_options(self):
    d = float(self.sticker) + self.sport_wheels() + self.sport_engine() + self.sport_interior()
    return d

#main

car_1 = Sport("Honda", "Civic", 23950)
car_2 = Sport("Toyota", "Camry", 26420)

print(car_1.make)
print(car_1.model)
print(car_1.sticker)
print(car_1.discount())
print(car_1.price_with_options())
print(car_2.make)
print(car_2.model)
print(car_2.sticker)
print(car_2.discount())
print(car_2.price_with_options())