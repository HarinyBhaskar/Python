class Staff:
    def __init__(self, name):
        self.name = name

class EmergencyMixin:
    def handle_emergency(self):
        print(f"{self.name} is handling an emergency!")

class OnlineConsultMixin:
    def consult_online(self):
        print(f"{self.name} is consulting a patient online.")

class Doctor(Staff, EmergencyMixin, OnlineConsultMixin):
    pass

doc = Doctor("Dr. House")
doc.handle_emergency()
doc.consult_online()
