from qiskit import QuantumCircuit
from qiskit.visualization import plot_bloch_multivector
from qiskit.extensions import Initialize

import numpy as np
import matplotlib.pyplot as plt

theta = np.random.uniform(0, np.pi)
phi = np.random.uniform(0, 2*np.pi)

psi = [np.cos(theta/2),np.exp(1j * phi) * np.sin(theta/2)]


qc = QuantumCircuit(2)
qc.ry(theta, 0)
qc.rz(phi, 0)
init_gate = Initialize(psi)
qc.append(init_gate, [1])

plot_bloch_multivector(psi)
plot_bloch_multivector(qc)
plt.show()