from pypylon import pylon

devices = pylon.TlFactory.GetInstance().EnumerateDevices()
for device in devices:
    print("Device found:", device.GetFriendlyName())
