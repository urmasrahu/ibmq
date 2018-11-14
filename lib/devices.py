# Qiskit SDK
from qiskit import execute, Aer
from qiskit import IBMQ
from qiskit.backends.ibmq import least_busy

# by Urmas
from lib import ibmq_login

def GetLocalSimulator():
  print("Getting local simulator...")
  sim = Aer.get_backend('qasm_simulator')
  print("Local simulator:", sim)
  return sim


def GetIBMQDevice(useSimulator):
  if not ibmq_login.login():
    return

  print("Getting the list of IBMQ backends (simulator=", useSimulator, ")...", sep="")
  backends = IBMQ.backends(simulator=useSimulator)
  print("IBMQ backends:", backends)

  print("Obtaining the least busy device...")
  least_busy_device = least_busy(backends)
  print("Least busy device:", least_busy_device)

  return least_busy_device

def GetSpecificIBMQDevice(name):
  if not ibmq_login.login():
    return

  backends = IBMQ.backends(name=name)
  if (len(backends) == 0):
    print("No backend matching name ', name, ' found", sep="")
    return

  if (len(backends) > 1):
    print("More than one backend with matching name found")
    return

  return backends[0]

def GetListOfIBMQDevices():
  if not ibmq_login.login():
    return

  print("Getting the list of IBMQ backends")
  return IBMQ.backends()
