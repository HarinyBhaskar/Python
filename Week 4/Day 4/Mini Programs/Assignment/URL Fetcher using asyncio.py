import asyncio
import aiohttp
import time

async def fetch_url(url, session):
    print(f"Starting: {url}")
    async with session.get(url) as response:
        text = await response.text()
        print(f"Finished: {url} | Size: {len(text)} chars")

async def main():
    urls = [
        "https://www.python.org",
        "https://www.wikipedia.org",
        "https://www.openai.com"
    ]
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(url, session) for url in urls]
        await asyncio.gather(*tasks)

start = time.time()
asyncio.run(main())
print(f"All fetches done in {time.time() - start:.2f} seconds ✅")
