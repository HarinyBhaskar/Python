import logging
from itertools import cycle
from collections import Counter

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    # Ask user for destinations
    n = int(input("How many destinations do you want to add? "))
    destinations = []
    for i in range(n):
        place = input(f"Enter destination {i+1}: ")
        destinations.append(place)

    # Ask number of days
    days = int(input("How many days is your trip? "))

    # Rotate destinations using cycle
    plan = []
    for day in range(1, days+1):
        stop = next(cycle(destinations))
        plan.append((f"Day {day}", stop))

    # Print itinerary
    print("\nYour Travel Itinerary:")
    for day, stop in plan:
        print(f"{day}: {stop}")

    # Analyze most frequent destinations
    count = Counter([s for _, s in plan])
    logging.info(f"Destination frequency: {dict(count)}")
    fav = count.most_common(1)[0]
    print(f"\nMost visited place: {fav[0]} ({fav[1]} times)")

if __name__ == "__main__":
    main()
