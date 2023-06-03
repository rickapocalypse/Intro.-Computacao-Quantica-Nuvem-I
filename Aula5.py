from qiskit import QuantumCircuit, execute, Aer
import matplotlib.pyplot as plt

qc = QuantumCircuit(5,2)

# Full adder circuit
def full_adder_circuit(qc):
    qc.cx(0,3)
    qc.cx(1,3)
    qc.cx(2,3)
    qc.ccx(0,1,4)
    qc.ccx(0,2,4)
    qc.ccx(1,2,4)

    qc.measure(3,0)
    qc.measure(4,1)
    return qc

x = input(f"Qubit for input A: ")
y = input(f"Qubit for Input B: ")
z = input(f"Qubit for Input Cin: ") 


if x == "1":
    qc.x(0)
if y == "1":
    qc.x(1)
if z == "1":
    qc.x(2)

full_adder_circuit(qc)
qc.draw("mpl")
plt.show()
qasm_sim = Aer.get_backend('qasm_simulator')  
job = execute(qc, backend=qasm_sim, shots=1)

result_sim = job.result()
counts = result_sim.get_counts(qc)
print(counts)