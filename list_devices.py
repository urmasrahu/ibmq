from lib import devices

list = devices.GetListOfIBMQDevices()

for device in list:
  print(device.name(), ": status=", device.status(), sep="")
