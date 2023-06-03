class Product:

  def __init__(self, name, price, quantity):
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
    if int(quantity) < 1:
      raise ValueError("Quantity cannot be below 1.")
    self.quantity = self.quantity - int(quantity)
    if self.quantity == 0:
      self.deactivate()
    total = self.price * int(quantity)
    return total

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