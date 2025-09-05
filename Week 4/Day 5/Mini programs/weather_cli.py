import argparse
import random

def main():
    parser = argparse.ArgumentParser(description="Simple Weather CLI")
    parser.add_argument("city", type=str, help="Enter city name")
    parser.add_argument("--unit", choices=["C", "F"], default="C", help="Temperature unit (C/F)")
    
    args = parser.parse_args()

    # Fake random temperature
    temp = random.randint(20, 35) if args.unit == "C" else random.randint(60, 95)
    print(f"Weather in {args.city}: {temp}°{args.unit}, Sunny ☀️")

if __name__ == "__main__":
    main()
