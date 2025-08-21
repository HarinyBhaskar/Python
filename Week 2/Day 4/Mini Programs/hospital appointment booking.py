import logging

logging.basicConfig(filename="hospital.log", level=logging.INFO)

appointments = []

try:
    patient = input("Enter patient name: ")
    doctor = input("Enter doctor name: ")
    time = input("Enter time: ")
    if not patient or not doctor or not time:
        raise ValueError("All details are required")
    appointments.append({"patient": patient, "doctor": doctor, "time": time})
    logging.info(f"Appointment booked: {patient} with {doctor} at {time}")
    print("Appointment booked successfully.")
except ValueError as e:
    logging.error(e)
    print("Error:", e)
