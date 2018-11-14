import sys
import time

# Qiskit SDK
from qiskit import execute

# by Urmas
from lib import experiments
from lib import devices

def RunExperiment(circuit, device):
  print("Running quantum circuit", circuit.name, "on device", device)
  job = execute(circuit, device, shots=1000, max_credits=3)

  print("Job ID:", job.job_id())

  lapse = 0
  interval = 2 # seconds
  while job.status().name != 'DONE':
    print('Status @ {} seconds'.format(interval * lapse), ": ", job.status(), sep="")
    time.sleep(interval)
    lapse += 1

  print(job.status())
  result = job.result()

  # Show the results
  print("Experiment:", result)
  print(result.get_counts(circuit))

  return


if len(sys.argv) < 2:
  print("Usage: run_local_sim.py experiment_name")
  sys.exit()

experiment = experiments.CreateExperiment(sys.argv[1])
device = devices.GetLocalSimulator()

RunExperiment(experiment, device)
