class Product:

  def __init__(self, name, price, quantity):
    if type(price) is not int or type(name) is not str or type(quantity) is not int:
      raise ValueError("Invalid input type when creating new product.\n")
    if price <= 0 or quantity <= 0:
      raise ValueError("Price and quantity must be greater than 0.\n")
    if len(name) <= 0:
      raise ValueError("Name must not be empty.\n")
    self.price = float(price)
    self.name = str(name)
    self.quantity = int(quantity)
    self.active = True

  def get_quantity(self):
    return float(self.quantity)

  def set_quantity(self, quantity):
    self.quantity = int(quantity)
    if self.quantity == 0:
      self.deactivate()

  def is_active(self):
    return self.active

  def activate(self):
    self.active = True

  def deactivate(self):
    self.active = False

  def show(self):
    return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

  def buy(self, quantity):
    if len(str(quantity)) < 1:
      raise ValueError("Please enter a quantity.\n")
    if int(quantity) < 1:
      raise ValueError("Quantity cannot be below 1.\n")
    if int(quantity) > self.quantity:
      raise ValueError(f"Chosen quantity exceeds amount available in stock. ({self.quantity} available)\n")
    self.quantity = self.quantity - int(quantity)
    if self.quantity == 0:
      self.deactivate()
    total = self.price * int(quantity)
    return total
  
class NonStocked(Product):

    def __init__(self, name, price):
        self.price = float(price)
        self.name = str(name)
        self.quantity = 0
        self.active = True

    def buy(self):
      total = self.price
      return total
    
    def show(self):
      return f"{self.name}, Price: {self.price}"
    
class LimitedProduct(Product):
  
  def __init__(self, name, price, quantity, maximum):
    super().__init__(name, price, quantity)
    self.maximum = maximum

  def buy(self, quantity):
    if int(quantity) > self.maximum:
      raise ValueError(f"This product has a maximum of {self.maximum} units per person. (chose {quantity})\n")
    return super().buy(quantity)

  def show(self):
    return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Maximum: {self.maximum}"

def main():
  bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
  mac = Product("MacBook Air M2", price=1450, quantity=100)

  print(bose.buy(50))
  print(mac.buy(100))
  print(mac.is_active())

  bose.show()
  mac.show()

  bose.set_quantity(1000)
  bose.show()

if __name__ == "__main__":
  main()