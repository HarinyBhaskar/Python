# Step 1: Take input as a string
num_str = input("Enter a number string (e.g., '0123'): ")

# Step 2: Show the original input and type
print("Original value:", num_str, "| Type:", type(num_str))

# Step 3: Convert (cast) the string to an integer
cleaned_int = int(num_str)

# Step 4: Show the cleaned integer and its type
print("Cleaned value:", cleaned_int, "| Type:", type(cleaned_int))
