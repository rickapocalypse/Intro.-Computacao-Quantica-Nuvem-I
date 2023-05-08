from qiskit import QuantumCircuit, Aer
import numpy as np
from qiskit.tools.visualization import plot_bloch_multivector, plot_histogram
import matplotlib.pyplot as plt

qasm_sim = Aer.get_backend('qasm_simulator') 

x = np.random.randint(0,2)
y = np.random.randint(0,2)

qc = QuantumCircuit(2,2)

# Parte da Alice

qc.h(0)
qc.cx(0,1)

for i in range(0,x):
    qc.z(0)
for i in range(0,y):
    qc.x(0)


print(f'Alice deseja enviar os bits x={x} e y={y}')

# Parte do bob

qc.cx(0,1)
qc.h(0)

qc.measure([0,1],[0,1])

resultado = qasm_sim.run(qc).result()
counts = resultado.get_counts(qc)
plot_histogram(counts)
plt.show()