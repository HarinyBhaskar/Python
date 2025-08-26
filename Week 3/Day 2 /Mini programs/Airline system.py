class Airplane:
    def __init__(self, model):
        self.model = model

class EntertainmentMixin:
    def play_movie(self):
        print("Playing in-flight movie")

class WiFiMixin:
    def connect_wifi(self):
        print("Connected to WiFi")

class PassengerPlane(Airplane, EntertainmentMixin, WiFiMixin):
    pass

plane = PassengerPlane("Boeing 737")
plane.play_movie()
plane.connect_wifi()
