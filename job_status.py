import sys

from lib import devices

if len(sys.argv) < 3:
  print("Usage: job_status.py device job_id")
  print("device can be e.g. ibmq_qasm_simulator (simulator) or ibmqx4 (real 5-qubit quantum computer)")
  sys.exit()

id = sys.argv[2]

device = devices.GetSpecificIBMQDevice(sys.argv[1])

try:
  print("Using device", device.name())
except:
  print("Failed to get the device")
  sys.exit()

print("Getting job with ID", id)

job = device.retrieve_job(id)

if job.job_id() == "":
  print("Job not found")
  sys.exit()

status = job.status().name

print("Job status:", status)

if status == "QUEUED":
  print("Creation date:", job.creation_date())
  print("Queue position:", job.queue_position())

if status == "DONE":
  print("Job result:")
  result = job.result()
  counts = result.get_counts()
  print(counts)
