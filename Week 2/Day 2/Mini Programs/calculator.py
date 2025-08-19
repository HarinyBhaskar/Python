def calculator(*numbers, **operation):
 
    if not numbers:
        return "No numbers given!"

    if operation.get("task") == "add":
        return sum(numbers)
    elif operation.get("task") == "multiply":
        result = 1
        for n in numbers:
            result *= n
        return result
    elif operation.get("task") == "average":
        return sum(numbers) / len(numbers)
    else:
        return "Unknown task!"


# Example usage
print("Addition:", calculator(10, 20, 30, 40, task="add"))
print("Multiplication:", calculator(2, 3, 4, task="multiply"))
print("Average:", calculator(80, 90, 100, task="average"))
