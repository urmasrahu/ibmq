import sys

# Qiskit SDK
from qiskit import execute

from lib import experiments
from lib import devices

def RunExperiment(circuit, device):
  print("Running quantum circuit", circuit.name, "on device", device)
  job = execute(circuit, device, shots=1000, max_credits=3)

  print("Job ID:", job.job_id())

  result = job.result() # this will wait for the job to complete

  # Show the results
  print("Results:")
  print(result.get_counts(circuit))

if len(sys.argv) < 2:
  print("Usage: run_local_sim.py experiment_name")
  sys.exit()

experiment = experiments.CreateExperiment(sys.argv[1])
device = devices.GetLocalSimulator()

RunExperiment(experiment, device)
