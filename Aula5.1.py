from qiskit import QuantumCircuit, execute, Aer
import matplotlib.pyplot as plt

qc = QuantumCircuit(3,1)

qc.x(0)
qc.x(1)
qc.ccx(0,1,2)
qc.measure(2,0)
qasm_sim = Aer.get_backend('qasm_simulator')  
job = execute(qc, backend=qasm_sim, shots=1)

result_sim = job.result()
counts = result_sim.get_counts(qc)
print(counts)