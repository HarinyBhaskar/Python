import threading, time

def send_email(user):
    print(f"Sending email to {user}...")
    time.sleep(2)
    print(f"Email sent to {user}")

def log_activity(activity):
    print(f"Logging: {activity}")
    time.sleep(1)
    print(f"Logged: {activity}")

# Start threads for background tasks
t1 = threading.Thread(target=send_email, args=("user@example.com",))
t2 = threading.Thread(target=log_activity, args=("User logged in",))

t1.start()
t2.start()

print("Main program is free to do other work 🚀")

t1.join()
t2.join()
