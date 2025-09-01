import logging
from collections import Counter, defaultdict
from itertools import chain

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    # Products purchased across two days
    day1 = ["apple", "banana", "apple", "orange", "banana"]
    day2 = ["apple", "apple", "grape", "banana"]

    # Merge sales data
    all_sales = list(chain(day1, day2))
    logging.info(f"All sales merged: {all_sales}")

    # Count most sold products
    sales_count = Counter(all_sales)
    logging.info(f"Top selling items: {sales_count.most_common(2)}")

    # Restocking check
    stock = defaultdict(int, {"apple": 10, "banana": 5, "orange": 3, "grape": 2})
    for item in all_sales:
        stock[item] -= 1
    logging.info(f"Remaining stock: {dict(stock)}")

    # Find out-of-stock products
    out = [k for k, v in stock.items() if v <= 0]
    logging.info(f"Out of stock: {out}")

if __name__ == "__main__":
    main()
