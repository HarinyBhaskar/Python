password = input("Enter a password: ")

if len(password) < 8:
    print("Weak: Less than 8 characters.")
elif password.isalpha() or password.isdigit():
    print("Weak: Use a mix of letters and numbers.")
elif password.isalnum():
    print("Medium: Add special characters for strength.")
else:
    print("Strong password!")

