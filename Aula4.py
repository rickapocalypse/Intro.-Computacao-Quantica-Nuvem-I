from qiskit import QuantumCircuit, Aer
import numpy as np
from qiskit.tools.visualization import plot_bloch_multivector, plot_histogram
import matplotlib.pyplot as plt

qasm_sim = Aer.get_backend('qasm_simulator') 

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0,1)
qc.measure_all()
resultado = qasm_sim.run(qc).result()  
counts = resultado.get_counts(qc)
plot_histogram(counts)
plt.show()