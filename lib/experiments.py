# Qiskit SDK
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister

def CreateExperiment_SimpleMeasurement():
  # Create a Quantum Register with 2 qubits.
  q = QuantumRegister(2)

  # Create a Classical Register with 1 bit.
  c = ClassicalRegister(1)

  # Create a Quantum Circuit.
  qc = QuantumCircuit(q, c, name="SimpleMeasurement")

  # Add a H gate on both qubits, putting them in superpositions.
  qc.h(q[0])
  qc.h(q[1])

  # Measure qubit 0 (qubit 1 is not measured).
  qc.measure(q[0], c[0])

  return qc


def CreateExperiment_SimpleEntanglement():
  # Create a Quantum Register with 2 qubits.
  q = QuantumRegister(2)

  # Create a Classical Register with 2 bits.
  c = ClassicalRegister(2)

  # Create a Quantum Circuit
  qc = QuantumCircuit(q, c, name="SimpleEntanglement")

  # Add a H gate on qubit 1, putting this qubit in superposition.
  qc.h(q[1])

  # Add a CX (CNOT) gate on control qubit 1 and target qubit 0, putting
  # the qubits in a Bell state.
  qc.cx(q[1], q[0])

  # Add a Measure gate to see the state.
  qc.measure(q, c)

  return qc

def CreateExperiment_Teleportation():
    q = QuantumRegister(3)
    c0 = ClassicalRegister(1, "c0")
    c1 = ClassicalRegister(1, "c1")
    cFinal = ClassicalRegister(1, "cFinal")
    qc = QuantumCircuit(q, c0, c1, cFinal, name="Teleportation")

    qc.h(q[1]) # A (Alice's qubit)
    qc.cx(q[1], q[0]) # A controls NOT(B)

    # now Alice and B each have entangled qubits, A and B respectively

    qc.h(q[2]) # create the transported qubit

    qc.cx(q[2], q[1]) # transported qubit controls NOT(A)
    qc.h(q[2]) # transported qubit

    qc.measure(q[2], c0[0]) # transported qubit
    qc.measure(q[1], c1[0]) # A

    # Conditionally manipulate B (Bob's qubit) based on the two classical bits received.

    # Note that according to https://quantumcomputing.stackexchange.com/questions/4270/how-would-one-implement-a-quantum-equivalent-of-a-while-loop-in-ibm-qiskit,
    # "classical conditionals like these are not currently supported on quantum hardware". So running this experiment on a simulator works but fails on a real
    # quantum computer.
    qc.z(q[0]).c_if(c0, 1)
    qc.x(q[0]).c_if(c1, 1)

    # now q[0] (B, Bob's qubit) has been transformed into the teleported qubit (originally q[2])
    # measuring it is not part of teleportation but let's do it anyway to end the experiment

    qc.measure(q[0], cFinal[0])

    return qc

def CreateExperiment(name):
  functionDict = {"SimpleMeasurement" : CreateExperiment_SimpleMeasurement, "SimpleEntanglement" : CreateExperiment_SimpleEntanglement, "Teleportation" : CreateExperiment_Teleportation}
  return functionDict[name]()
