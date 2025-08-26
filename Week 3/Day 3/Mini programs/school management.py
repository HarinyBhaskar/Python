class Person:
    def __init__(self, name):
        self.name = name

class LoggingMixin:
    def log(self, action):
        print(f"[LOG] {self.name}: {action}")

class EmailMixin:
    def send_email(self, message):
        print(f"Sending email to {self.name}: {message}")

class Teacher(Person, LoggingMixin, EmailMixin):
    pass

teacher = Teacher("Mr. Smith")
teacher.log("Graded assignments")
teacher.send_email("Meeting tomorrow")
