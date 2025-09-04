import threading

def read_file(filename):
    with open(filename, "r") as f:
        data = f.read()
    print(f"{filename} has {len(data.split())} words")

files = ["file1.txt", "file2.txt", "file3.txt"]

threads = []
for f in files:
    t = threading.Thread(target=read_file, args=(f,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Finished reading all files ✅")
