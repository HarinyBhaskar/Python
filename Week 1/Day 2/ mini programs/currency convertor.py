usd = input("Enter amount in USD: ")
usd = float(usd)
rate = 83.5  # 1 USD = 83.5 INR
inr = usd * rate
print("USD entered:", usd)
print("Exchange rate: 1 USD =", rate, "INR")
print("Converted amount in INR:", inr)
