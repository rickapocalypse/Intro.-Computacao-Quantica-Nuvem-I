from qiskit import QuantumCircuit
from qiskit.visualization import plot_bloch_multivector
from qiskit.extensions import Initialize
import matplotlib.pyplot as plt

qc = QuantumCircuit(1)
qc.h(0)
qc.h(0)

qc2 = QuantumCircuit(1,1)
qc2.h(0)
qc2.sdg(0)
qc2.h(0)

qc3 = QuantumCircuit(1,1)
qc3.h(0)
plot_bloch_multivector(qc3)
plot_bloch_multivector(qc2)
plot_bloch_multivector(qc)
plt.show()