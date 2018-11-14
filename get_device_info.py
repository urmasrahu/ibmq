import sys
import pprint

from lib import devices

if len(sys.argv) < 2:
  print("Usage: get_device_info.py device")
  print("You can use the list_devices.py script to get the list of available devices")
  sys.exit()

device = devices.GetSpecificIBMQDevice(sys.argv[1])

print(device.name(), ": status=", device.status(), sep="")
print("Configuration:")
pprint.PrettyPrinter().pprint(device.configuration())
#print(device.configuration())
