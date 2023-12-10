class Car:
  def __init__(self, make, model, sticker_price):
      self.make = make
      self.model = model
      self.sticker_price = sticker_price
      self.discount_price = 0.9 * sticker_price

  def options(self):
      return self.discount_price

class Sport(Car):
  def __init__(self, make, model, sticker_price):
      super().__init__(make, model, sticker_price)
      self.sport_wheels = 0
      self.sport_engine = 0
      self.sport_interior = 0

  def swheels(self):
      self.sport_wheels = 1000.00

  def sengine(self):
      self.sport_engine = 3000.00

  def sinterior(self):
      self.sport_interior = 2000.00

  def pricewoptions(self):
      total_price = self.sport_wheels + self.sport_engine + self.sport_interior + self.sticker_price
      return total_price



car=Sport ("Bmw", "M5", 90000)
car.swheels()
car.sengine()
car.sinterior()

print (car.pricewoptions())