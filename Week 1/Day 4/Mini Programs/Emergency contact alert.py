contacts = [
    {"name": "Nikhil", "phone": "9876543210", "alerted": False},
    {"name": "Kiran", "phone": "9876543211", "alerted": False},
    {"name": "Sunita", "phone": "9876543212", "alerted": False},
]

emergency_message = "EMERGENCY ALERT: Please respond immediately!"

print(" Emergency Contact Alert System ")

for contact in contacts:
    print(f"\n Sending alert to {contact['name']} ({contact['phone']})...")
    print(f"Message: {emergency_message}")
    contact['alerted'] = True  

print("\n Alert Sending Completed ")

print("\n Waiting for acknowledgments...")
all_acknowledged = False

while not all_acknowledged:
    all_acknowledged = True
    for contact in contacts:
        if contact['alerted']:
            response = input(f"Has {contact['name']} acknowledged? (yes/no): ").strip().lower()
            if response != "yes":
                all_acknowledged = False
    if not all_acknowledged:
        print("\nNot all contacts have acknowledged. Waiting again...\n")

print("\n All contacts have acknowledged the alert!")
