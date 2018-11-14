import sys

from qiskit import execute

from lib import experiments
from lib import devices

def AsyncRunExperiment(circuit, device):
  print("Running quantum circuit", circuit.name, "on device", device)
  job = execute(circuit, device, shots=1000, max_credits=3)

  print("Job ID:", job.job_id())
  print("Status:", job.status())
  return


if len(sys.argv) < 3:
  print("Usage: run_async.py device experiment_name")
  print("device can be e.g. ibmq_qasm_simulator (simulator) or ibmqx4 (real 5-qubit quantum computer)")
  sys.exit()

device = devices.GetSpecificIBMQDevice(sys.argv[1])

if device.name() == "":
  print("Failed to get the device")
  sys.exit()

experiment = experiments.CreateExperiment(sys.argv[2])

AsyncRunExperiment(experiment, device)
