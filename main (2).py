class Employee:
  def __init__(self, first, last, pay, bonus=0):
      self.first = first
      self.last = last
      self.email = f'{first}.{last}@email.com'
      self.pay = pay
      self.bonus = bonus


  def calculate_bonus(self, bonus_rate):
      return self.pay * bonus_rate

  def fullname(self):
      return '{} {}'.format(self.first, self.last)

class Manager(Employee): 
  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.email = f'{first}.{last}@email.com'
    self.pay = pay


  def calculate_bonus(self):
    return self.pay * .4 

mang1=Manager ("Aman", "Jones" , 4)
print (mang1.calculate_bonus ()) 
