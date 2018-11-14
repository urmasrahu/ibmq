IBMQ -- some trivial IBM Quantum Experience Python scripts based on Qiskit Terra
================================================================================

This repo contains some simple Python scripts I have created for playing with IBM Quantum Experience ("IBMQ") using Qiskit Terra.

Requires:
* Qiskit Terra, https://github.com/Qiskit/qiskit-terra
* An account at IBM Quantum Experience, https://quantumexperience.ng.bluemix.net/qx

Setup:
1. Download and install Qiskit Tierra, see the above link.
2. Get the IBM Quantum Experience API token (see the above Qiskit Tierra link for this also) and save it in an environment variable **IBMQ_TOKEN**.

There are Visual Studio files ibmq.sln and ibmq.pyproj here as I have used Visual Studio for editing the scripts, they are not strictly needed.

The following scripts are available.

list_devices.py
---------------
Lists the available IBM devices (both real quantum computers and simulators).

Usage: list_devices.py

get_device_info.py
------------------
Provides details about an IBM device.

Usage: get_device_info.py device

Use the **list_devices.py** script for getting the list of available device names.

Example:
```
get_device_info.py ibmqx4
```

run_local_sim.py
----------------
Runs an experiment on the local simulator and prints the results; this is the only script that does not require the IBMQ account as it does not use the IBM backends.

Usage: run_local_sim.py experiment_name

See **lib/experiments.py** for available experiments and their names (see **functionDict** towards the end of the script).

Example:
```
run_local_sim.py SimpleMeasurement
```

run_async.py
------------
Starts an experiment (a job) on a given IBM device, does not wait for it to complete. If the job is created successfully, prints the job ID that should be used for checking the job status using **job_status.py**.

Usage: run_async.py device experiment_name

See **lib/experiments.py** for available experiments and their names (see **functionDict** towards the end of the script).

Example:
```
run_async.py ibmq_qasm_simulator SimpleMeasurement
```

job_status.py
-------------
Checks the experiment (job) status on a given IBM device. If the status is "DONE", prints the results of the experiment. If the job is in the queue, prints the job's position in the queue.

Usage: job_status.py device job_id

Example:
```
job_status.py ibmq_qasm_simulator 5bebe0123456789abcdef012
```
