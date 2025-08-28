import logging
logging.basicConfig(filename="itinerary.log", level=logging.DEBUG, format="%(levelname)s:%(message)s")

# Generator
def flatten(plan):
    for item in plan:
        if isinstance(item, list):
            logging.debug(f"Expanding: {item}")
            yield from flatten(item)
        else:
            logging.debug(f"Yielding: {item}")
            yield item

# Iterator
class Itinerary:
    def __init__(self, plan): self.flat, self.i = list(flatten(plan)), 0
    def __iter__(self): return self
    def __next__(self):
        if self.i < len(self.flat): 
            val, self.i = self.flat[self.i], self.i + 1
            return val
        logging.info("All items processed."); raise StopIteration

# Main
try:
    n = int(input("Enter number of destinations: "))
    if n <= 0: logging.warning("Non-positive count"); raise ValueError("Invalid count")

    plan = []
    for i in range(n):
        dest = input(f"Destination {i+1}: ")
        acts = input(f"Activities in {dest} (',' sep, ';' for sub): ")
        plan.append([dest] + [[a if ';' not in a else a.split(';') for a in acts.split(",")]])

    comp_list = [p for p in flatten(plan)]
    print("\nComprehension:", comp_list)
    print("Iterator:", [p for p in Itinerary(plan)])

except ValueError as ve:
    logging.error(f"ValueError: {ve}"); print("Invalid input! Try again.")
except Exception as e:
    logging.critical(f"Critical error: {e}"); print("Critical error! Check logs.")
