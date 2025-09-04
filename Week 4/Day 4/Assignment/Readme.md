# URL Fetcher: Threading vs Asyncio

This program demonstrates how to fetch multiple web pages concurrently in Python using **two different approaches**:

1. **Threading** – Uses multiple system threads to perform blocking I/O operations (like HTTP requests) in parallel.
2. **Asyncio** – Uses Python's asynchronous event loop with non-blocking I/O, allowing efficient concurrency without creating many system threads.

---

## Features
- Fetch multiple URLs concurrently.
- Compare performance between **threading** and **asyncio**.
- Demonstrates real-world concurrency with Python (`requests` and `aiohttp`).

---

## Requirements

Install dependencies before running:

```bash
pip install requests aiohttp
