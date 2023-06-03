import store
import products
# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)

def start(store):
  print("\n1. List all products in store\n2. Show total amount in store\n3. Make an order\n4. Quit")
  choice = input("\nSelect option: ")
  if choice == "1":
    list_products(store)
  if choice == "2":
    show_total_amount(store)
  if choice == "3":
    make_order(store)
  if choice == "4":
    return print("Bye!")

def list_products(store):
  print("---------------\n")
  for product in store.products:
    print(product.name)
  print("\n---------------")
  return start(store)

def show_total_amount(store):
  print(store.get_total_quantity())
  return start(store)

def make_order(store):
  print("---------------\n")
  for product in store.get_all_products():
    print(product.show())
  print("\n---------------")
  total_price = 0
  shop_list = []
  quantity_track = {}
  while True:
    chosen_item = input("Enter a product to buy (leave blank to finish order): ")
    if len(chosen_item) < 1:
      break
    chosen_quantity = input("Enter amount needed: ")
    if len(chosen_quantity) < 1:
      print("Error: Please enter a quantity.")
      continue
    if int(chosen_quantity) < 1:
      print("Error: Quantity cannot be less than 1.")
      continue
    for product in store.get_all_products():
      if product.name == chosen_item:
        chosen_item = product
        quantity_track[chosen_item] = quantity_track.get(chosen_item, 0) + int(chosen_quantity)
        if quantity_track[chosen_item] > product.quantity:
          print(f"Error: Product sold out for {quantity_track[chosen_item] - product.quantity} previously chosen.")
          chosen_quantity = int(chosen_quantity) - (quantity_track[chosen_item] - product.quantity)
          product.deactivate()
        flag = False
        break
      else:
        if product == store.get_all_products()[-1]:
          print("Error: Product could not be found (please check spelling).")
          flag = True
    if flag:
      flag = False
      continue
    if int(chosen_quantity) > chosen_item.quantity:
      print("Error: Quantity chosen is too large.")
      continue
    paired = (chosen_item, int(chosen_quantity))
    shop_list.append(paired)
  if len(shop_list) >= 1:
    total_price = store.order(shop_list)
    print(f"\nTotal price: {total_price}")
  return start(store)
    
start(best_buy)