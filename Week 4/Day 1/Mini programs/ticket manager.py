import logging
from collections import deque, defaultdict

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    # User enters tickets
    n = int(input("How many tickets to add? "))
    tickets = deque()
    for i in range(n):
        tid = input(f"Enter Ticket ID {i+1}: ")
        issue = input("Enter issue type: ")
        tickets.append((tid, issue))

    logging.info(f"All Tickets: {list(tickets)}")

    # Count issue categories
    categories = defaultdict(int)
    for _, issue in tickets:
        categories[issue] += 1
    logging.info(f"Category counts: {dict(categories)}")
    print(f"\nTicket Categories: {dict(categories)}")

    # Process queue
    print("\nProcessing Tickets...")
    while tickets:
        tid, issue = tickets.popleft()
        logging.info(f"Processing {tid}")
        print(f"Resolved {tid} - {issue}")

if __name__ == "__main__":
    main()
