import logging
from collections import deque
from itertools import cycle

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    # User enters songs
    n = int(input("How many songs to add to playlist? "))
    songs = deque()
    for i in range(n):
        songs.append(input(f"Enter song {i+1}: "))

    logging.info(f"Initial playlist: {list(songs)}")

    # Rotate (simulate skip)
    skip = int(input("How many songs to skip? "))
    songs.rotate(-skip)
    print(f"\nPlaylist after skipping {skip}: {list(songs)}")

    # Repeat mode
    repeat = cycle(songs)
    count = int(input("How many songs to play in repeat mode? "))
    played = [next(repeat) for _ in range(count)]
    logging.info(f"Played sequence: {played}")
    print(f"Repeat mode played: {played}")

if __name__ == "__main__":
    main()
