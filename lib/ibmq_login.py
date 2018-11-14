import os
from qiskit import IBMQ

def login():
  try:
    token = os.environ['IBMQ_TOKEN']
  except:
    print("IBMQ_TOKEN environment variable not found. You must set this variable to the account token string.")
    return False

  print("Connecting to IBMQ account...")

  try:
    IBMQ.enable_account(token)
  except:
    print("Unable to access IBMQ account")
    return False

  return True
