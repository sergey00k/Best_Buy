import store
import products
# setup initial stock of inventory
# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250),
                 products.NonStocked("Windows License", price=125),
                 products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
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
  while True:
    flag = False
    chosen_item = input("Enter a product to buy (leave blank to finish order): ")
    if len(chosen_item) < 1:
      break
    for product in store.get_all_products():
      if product.name == chosen_item:
        chosen_item = product
        if isinstance(product, products.NonStocked):
          try:
            total_price += chosen_item.buy()
            flag = True
            break
          except ValueError as e:
            print("Error: ", str(e))
            continue
    if flag:
      continue
    chosen_quantity = input("Enter amount needed: ")
    paired = (chosen_item, chosen_quantity)
    shop_list = [paired]
    try:
      price = store.order(shop_list)
      if price == None:
        continue
      else:
        total_price += price
    except ValueError as e:
      print("\nError: ", str(e))
  print(f"\nTotal price: {total_price}")
  return start(store)
    
start(best_buy)