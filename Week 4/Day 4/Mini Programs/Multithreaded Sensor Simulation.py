import threading, time, random

def sensor(name):
    for _ in range(3):
        value = random.randint(20, 100)
        print(f"{name} sensor reading: {value}")
        time.sleep(1)

sensors = ["Temp", "Pressure", "Humidity"]

threads = []
for s in sensors:
    t = threading.Thread(target=sensor, args=(s,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All sensors completed ✅")
