import logging
logging.basicConfig(filename="student.log", level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")

class StudentIterator:
    def __init__(self, students): self.students,self.i=students,0
    def __iter__(self): return self
    def __next__(self):
        if self.i < len(self.students): s=self.students[self.i];self.i+=1;return s
        raise StopIteration

n=int(input("No. of students: "))
students=[
    {"name":input("Name: "),
     "marks":{sub:int(input(f"{sub}: ")) for sub in ["Maths","Sci","Eng"]}}
    for _ in range(n)
]
logging.info(f"Collected {n} students")

for s in students:
    s["avg"]=sum(s["marks"].values())//3
    if any(m<0 or m>100 for m in s["marks"].values()):
        logging.error(f"Invalid marks for {s['name']}")
    s["result"]="Pass" if all(m>=40 for m in s["marks"].values()) else "Fail"
    if s["result"]=="Fail": logging.warning(f"{s['name']} is failing")
    logging.debug(f"Processed {s['name']} → {s}")

for s in StudentIterator(students):
    print(f"{s['name']} → {s['marks']} | Avg={s['avg']} | {s['result']}")
