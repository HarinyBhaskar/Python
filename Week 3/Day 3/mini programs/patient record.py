import logging
logging.basicConfig(filename="hospital.log", level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")

class PatientIterator:
    def __init__(self, patients): self.patients,self.i=patients,0
    def __iter__(self): return self
    def __next__(self):
        if self.i<len(self.patients): x=self.patients[self.i];self.i+=1;return x
        raise StopIteration

n=int(input("Enter number of patients: "))
patients=[{"name":input("Name: "),
           "age":int(input("Age: ")),
           "bp":int(input("BP Level: "))} for _ in range(n)]
logging.info(f"Collected {n} patients")

for p in patients:
    if p["age"]<=0: logging.error(f"Invalid age for {p['name']}")
    if p["bp"]>140: logging.warning(f"High BP detected for {p['name']}")
    if p["bp"]<60: logging.warning(f"Low BP detected for {p['name']}")
    logging.debug(f"Processed patient {p}")
if not patients: logging.critical("No patients entered!")

for p in PatientIterator(patients):
    status="Normal" if 80<=p["bp"]<=120 else "Checkup Needed"
    print(f"{p['name']} (Age {p['age']}) → BP={p['bp']} | {status}")
