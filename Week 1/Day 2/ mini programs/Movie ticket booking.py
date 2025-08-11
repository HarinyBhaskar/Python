price = 12.5  # price per ticket
tickets = input("Enter number of tickets: ")
tickets = int(tickets)
discount = input("Enter discount %: ")
discount = float(discount)
total = price * tickets
discount_amount = (discount / 100) * total
final_price = total - discount_amount
print("Total price before discount:", total)
print("Final price after discount: $", final_price)
