class Store:
  import products
  def __init__(self, products):
    self.products = products

  def add_product(self, product):
    for item in product:
      self.products.append(item)
    
  def remove_product(self, product):
    if product in self.products:
      self.products.remove(product)
    else:
      print("Product was not found.")

  def get_total_quantity(self):
    self.total = 0
    for product in self.products:
      self.total += product.quantity
    return self.total

  def get_all_products(self):
    self.active_products = []
    for product in self.products:
      if product.active:
        self.active_products.append(product)
    return self.active_products

  def order(self, shopping_list):
    self.price = 0
    self.items = []
    for product in shopping_list:
      if product[0] not in self.products:
        raise ValueError("Product could not be found (please check spelling).\n")
      try:
        self.price = self.price + product[0].buy(product[1])
        return self.price
      except ValueError as e:
        print(f"\nError: {str(e)}")

def main():
  product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
              products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
              products.Product("Google Pixel 7", price=500, quantity=250),
              ]

  store = Store(product_list)
  products = store.get_all_products()
  print(store.get_total_quantity())
  print(store.order([(products[0], 1), (products[1], 2)]))

if __name__ == "__main__":
  main()