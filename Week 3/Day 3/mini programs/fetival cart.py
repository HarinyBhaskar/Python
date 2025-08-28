import logging
logging.basicConfig(filename="shopping.log", level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")

class CartIterator:
    def __init__(self, items): self.items,self.i=items,0
    def __iter__(self): return self
    def __next__(self):
        if self.i<len(self.items): x=self.items[self.i];self.i+=1;return x
        raise StopIteration

n=int(input("Enter number of items: "))
items=[(input("Item: "), int(input("Price: "))) for _ in range(n)]
logging.info("Collected shopping items")

cart=[{"item":i,"price":p,"final":p*0.85 if p>1000 else p*0.9} for i,p in items]

for c in cart:
    if c["price"]<=0: logging.error(f"Invalid price {c}")
    if c["final"]>2000: logging.warning(f"Very costly item {c}")
    logging.debug(f"Processed {c}")

if not cart: logging.critical("No items in shopping cart!")

for c in CartIterator(cart):
    print(f"{c['item']}: ₹{c['price']} → ₹{c['final']:.2f}")
