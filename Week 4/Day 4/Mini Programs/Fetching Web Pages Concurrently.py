import threading
import requests
import time

# Function to fetch a web page
def fetch_url(url):
    print(f"Starting: {url}")
    response = requests.get(url)
    print(f"Finished: {url} | Size: {len(response.text)} chars")

# List of websites
urls = [
    "https://www.python.org",
    "https://www.wikipedia.org",
    "https://www.openai.com"
]

threads = []
start = time.time()

# Create and start a thread for each URL
for url in urls:
    t = threading.Thread(target=fetch_url, args=(url,))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

print(f"All fetches completed in {time.time() - start:.2f} seconds ✅")
