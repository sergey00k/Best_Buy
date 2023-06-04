from abc import ABC, abstractmethod

class Promotion(ABC):
  
  def __init__(self, name):
    self.name = name

  @abstractmethod
  def apply_promotion(self, price):
    pass
  
  def remove_promotion(self):
    return None
  
class PercentDiscount(Promotion):
  
  def __init__(self, name, percent):
    self.name = name
    self.percent = float(percent)

  def apply_promotion(self, price, quantity):
    price = price * quantity
    result = price - (price * (self.percent / 100))
    return result
  
class SecondHalfPrice(Promotion):
  
  def apply_promotion(self, price, quantity):
    if quantity >= 2:
      result = ((quantity / 2) * (price * 0.5)) + ((quantity / 2) * price)
    return result
  
class ThirdOneFree(Promotion):
  
  def apply_promotion(self, price, quantity):
    if quantity >= 3:
      result = (quantity - (quantity / 3)) * price
      return result