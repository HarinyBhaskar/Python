principal = input("Enter principal amount: ")
principal = float(principal)
rate = input("Enter rate of interest (%): ")
rate = float(rate)
time = input("Enter time in years: ")
time = int(time)
interest = (principal * rate * time) / 100
total_amount = principal + interest
print("Simple interest is:", interest)
print("Total amount after", time, "years is:", total_amount)
