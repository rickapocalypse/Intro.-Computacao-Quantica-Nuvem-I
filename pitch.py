from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, Aer, execute
from qiskit.visualization import plot_histogram, plot_bloch_multivector
import matplotlib.pyplot as plt

qubits = QuantumRegister(2)
bits = ClassicalRegister(2)
qc = QuantumCircuit(qubits, bits)

qc.h(0)

qc.cx(0,1)

qc.measure(qubits,bits)



qasm_sim = Aer.get_backend('qasm_simulator') 
job = execute(qc, backend=qasm_sim, shots=1024)

result_sim = job.result()
counts = result_sim.get_counts(qc)
plot_histogram(counts)
plt.show()