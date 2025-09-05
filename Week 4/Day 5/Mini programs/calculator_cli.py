# calculator_cli.py
import argparse

def main():
    parser = argparse.ArgumentParser(description="Simple Calculator CLI")
    parser.add_argument("num1", type=float, help="First number")
    parser.add_argument("num2", type=float, help="Second number")
    parser.add_argument("operation", choices=["add", "sub", "mul", "div"], help="Operation to perform")
    
    args = parser.parse_args()
    
    if args.operation == "add":
        result = args.num1 + args.num2
    elif args.operation == "sub":
        result = args.num1 - args.num2
    elif args.operation == "mul":
        result = args.num1 * args.num2
    elif args.operation == "div":
        result = args.num1 / args.num2 if args.num2 != 0 else "Error: Division by zero"
    
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
