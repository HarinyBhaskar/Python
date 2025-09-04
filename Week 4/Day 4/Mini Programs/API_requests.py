import threading, requests

def get_api(url):
    print(f"Fetching {url}")
    res = requests.get(url)
    print(f"Done {url}, Status: {res.status_code}")

apis = [
    "https://api.github.com",
    "https://jsonplaceholder.typicode.com/posts",
    "https://httpbin.org/get"
]

threads = []
for url in apis:
    t = threading.Thread(target=get_api, args=(url,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All API calls done ✅")
