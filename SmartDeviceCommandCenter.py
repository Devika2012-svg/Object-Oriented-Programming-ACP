from abc import ABC, abstractmethod

class SmartDevice(ABC):

    def show_device(self):
        print("Smart Device")

    @abstractmethod
    def turn_on(self):
        pass

class SmartLight(SmartDevice):

    def turn_on(self):
        print("💡 Smart Light is turned on.")


class SmartFan(SmartDevice):

    def turn_on(self):
        print("✇ Smart Fan is turned on.")


class SmartSpeaker(SmartDevice):

    def turn_on(self):
        print("📢 Smart Speaker is turned on.")

light = SmartLight()
fan = SmartFan()
speaker = SmartSpeaker()

light.show_device()
light.turn_on()

fan.show_device()
fan.turn_on()

speaker.show_device()
speaker.turn_on()

class SecurityCamera:

    def check_status(self):
        print("📸 Security Camera is recording.")
class DoorLock:

    def check_status(self):
        print("🔑 Door Lock is secured.")

camera = SecurityCamera()
lock = DoorLock()

devices = [camera, lock]

for device in devices:
    device.check_status()
