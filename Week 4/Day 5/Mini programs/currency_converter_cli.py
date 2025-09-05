# currency_converter_cli.py
import argparse

RATES = {
    "USD": 1,
    "INR": 83.0,
    "EUR": 0.92,
    "GBP": 0.78,
}

def main():
    parser = argparse.ArgumentParser(description="Currency Converter CLI")
    parser.add_argument("amount", type=float, help="Amount to convert")
    parser.add_argument("from_currency", choices=RATES.keys(), help="Currency to convert from")
    parser.add_argument("to_currency", choices=RATES.keys(), help="Currency to convert to")
    args = parser.parse_args()

    usd_amount = args.amount / RATES[args.from_currency]
    converted = usd_amount * RATES[args.to_currency]

    print(f"{args.amount} {args.from_currency} = {converted:.2f} {args.to_currency}")

if __name__ == "__main__":
    main()
