import csv
import logging

# Setup logging
logging.basicConfig(filename="sales_parser.log",
                    level=logging.ERROR,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def parse_sales_csv(file_name):
    sales = []
    try:
        with open(file_name, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    # Expecting Product, Quantity(int), Price(float)
                    product = row['Product']
                    qty = int(row['Quantity'])
                    price = float(row['Price'])
                    total = qty * price
                    sales.append((product, qty, price, total))
                except (ValueError, KeyError) as e:
                    logging.error(f"Error in row {row}: {e}")
    except FileNotFoundError:
        logging.error(f"File {file_name} not found.")
    except csv.Error as e:
        logging.error(f"CSV parsing error: {e}")
    return sales

# Example execution
records = parse_sales_csv("sales.csv")
print("Processed Sales Data:")
for rec in records:
    print(rec)
