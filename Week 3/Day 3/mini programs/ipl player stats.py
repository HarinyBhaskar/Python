import logging
logging.basicConfig(filename="ipl.log", level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")

class PlayerIterator:
    def __init__(self, players): self.players,self.i=players,0
    def __iter__(self): return self
    def __next__(self):
        if self.i<len(self.players): p=self.players[self.i];self.i+=1;return p
        raise StopIteration

n=int(input("No. of players: "))
stats=[{"name":input("Player name: "),
        "runs":[int(input(f"Runs in match {j+1}: ")) for j in range(3)]}
       for i in range(n)]
logging.info(f"Stats for {n} players collected")

for s in stats:
    if any(r<0 for r in s["runs"]):
        logging.error(f"Negative runs entered for {s['name']}")
    s["avg"]=sum(s["runs"])//3
    balls=int(input(f"Balls faced by {s['name']}: "))
    if balls==0:
        logging.error(f"Division by zero for {s['name']} (balls=0)")
        s["sr"]=0
    else:
        s["sr"]=round((sum(s["runs"])/balls)*100,2)
    if s["avg"]<20: logging.warning(f"{s['name']} is underperforming")
    logging.debug(f"Processed {s}")

for s in PlayerIterator(stats):
    print(f"{s['name']} Runs={s['runs']} | Avg={s['avg']} | SR={s['sr']}")
