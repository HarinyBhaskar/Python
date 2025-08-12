doctors = {
    1: {"name": "Dr. Smith", "specialization": "Cardiologist", "slots": ["10:00 AM", "11:00 AM"]},
    2: {"name": "Dr. Lee", "specialization": "Dermatologist", "slots": ["2:00 PM", "3:00 PM"]},
    3: {"name": "Dr. Kumar", "specialization": "Pediatrician", "slots": ["4:00 PM", "5:00 PM"]}
}

print("Available Doctors:")
for key, doc in doctors.items():
    print(f"{key}. {doc['name']} - {doc['specialization']}")

choice = int(input("Choose doctor (1-3): "))
if choice not in doctors:
    print("Invalid choice!")
else:
    print(f"Available slots for {doctors[choice]['name']}:")
    for i, slot in enumerate(doctors[choice]['slots'], 1):
        print(f"{i}. {slot}")
    
    slot_choice = int(input("Choose slot: "))
    if 1 <= slot_choice <= len(doctors[choice]['slots']):
        selected_slot = doctors[choice]['slots'][slot_choice - 1]
        print(f"Appointment confirmed with {doctors[choice]['name']} at {selected_slot}.")
    else:
        print("Invalid slot selection.")
