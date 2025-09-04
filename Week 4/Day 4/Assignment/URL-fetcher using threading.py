import threading
import requests
import time

urls = [
    "https://www.google.com",
    "https://www.python.org",
    "https://www.github.com"
]

def fetch_url(url):
    response = requests.get(url)
    print(f"{url} -> {response.status_code}")

start = time.time()
threads = []

for url in urls:
    t = threading.Thread(target=fetch_url, args=(url,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"All fetches done in {time.time() - start:.2f} seconds")
