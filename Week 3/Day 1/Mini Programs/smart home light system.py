class Light:
    def __init__(self, room):
        self.room = room
        self.is_on = False

    def switch_on(self):
        self.is_on = True
        print(f"{self.room} light is ON.")

    def switch_off(self):
        self.is_on = False
        print(f"{self.room} light is OFF.")

# Example usage
l1 = Light("Living Room")
l2 = Light("Bedroom")

l1.switch_on()
l2.switch_off()
