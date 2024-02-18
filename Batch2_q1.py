''' Write a program in Python that reads data values as product name and price. For this, it asks user to 
enter such data pairs until user says 'n'/no. Store these data in a dictionary whose keys are the product 
names and whose values are the prices. When the user is done entering products and prices, allow them 
to enter a product name and print the corresponding price or a message if the product is not in the data. 
Also, allow the user to enter price range and print out all the products whose price is within that range. 
Take at least 8 such data.'''

def get_product_data():
  product_data = {}

  while True:
    product_name = input("Enter product name or 'n' to stop : ").lower()

    if product_name == 'n':
      break
    
    try:
      price = float(input(f"Enter the price for {product_name} : "))
      product_data[product_name]=price
    except ValueError:
      print("Invalid proce.Please enter a valid numeric value.")

  return product_data

def get_product_price(product_data,product_name):
  if product_name in product_data:
    print("Product price : ",product_data[product_name])
  else:
    print("Product not found.")

def get_product_range(product_data,min_price,max_price):
  products_range ={}

  for name,price in product_data.items():
    if min_price <= price <= max_price :
      products_range[name] =price
  return products_range

# Get the product data
product_data = get_product_data()
print(product_data)

min = float(input("Minimum price : "))
max = float(input("Maximum price : "))
print(get_product_range(product_data,min,max))
