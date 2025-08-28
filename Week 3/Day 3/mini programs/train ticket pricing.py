import logging
logging.basicConfig(filename="rail.log", level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")

class TrainIterator:
    def __init__(self,trains): self.trains,self.i=trains,0
    def __iter__(self): return self
    def __next__(self):
        if self.i<len(self.trains): t=self.trains[self.i];self.i+=1;return t
        raise StopIteration

n=int(input("No. of routes: "))
routes=[(input("From: "),input("To: "),int(input("Price: "))) for _ in range(n)]
logging.info("Collected train routes")

trains=[{"src":s,"dst":d,"base":p,"final":p-(0.1*p if p>1000 else 0.05*p)}
        for s,d,p in routes]

for t in trains:
    if t["base"]<0: logging.error(f"Negative price for {t['src']}→{t['dst']}")
    if t["final"]>2000: logging.warning(f"Very costly ticket {t}")
    logging.debug(f"Processed train {t}")

for t in TrainIterator(trains):
    print(f"{t['src']} → {t['dst']} | Base ₹{t['base']} | Final ₹{t['final']}")
