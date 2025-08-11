print(" Online Shopping Cart ")

# String data type for customer name
customer_name = input("Enter your name: ")

# Float for prices
item1_price = float(input("Enter price of item 1: ₹ "))
item2_price = float(input("Enter price of item 2: ₹ "))

# Int for quantities
item1_qty = int(input("Quantity of item 1: "))
item2_qty = int(input("Quantity of item 2: "))

# Bool for delivery option
delivery_needed = input("Do you need delivery? (yes/no): ").lower() == "yes"

# Calculations
subtotal = (item1_price * item1_qty) + (item2_price * item2_qty)
delivery_fee = 50.0 if delivery_needed else 0.0
total = subtotal + delivery_fee

# Output
print("\nCustomer:", customer_name)
print("Subtotal: ₹", subtotal)
print("Delivery Fee: ₹", delivery_fee)
print("Total: ₹", total)
