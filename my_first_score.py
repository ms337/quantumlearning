
# score.py
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer

# Define the Quantum and Classical Registers
q = QuantumRegister(2)
c = ClassicalRegister(2)

# Build the circuit
score = QuantumCircuit(q, c)

# # Pauli operations 
# score.x(q[0])
# score.y(q[1])
# score.z(q[0])
# score.barrier(q)

#Clifford Operations
score.h(q)
score.s(q[0])
score.s(q[1]).inverse()
score.cx(q[0], q[1])
#score.barrier(q)

#non Clifford Operations
score.t(q[0])
score.t(q[1]).inverse()
#score.barrier(q)

score.measure(q,c)

#Executing
job = execute(score, backend = Aer.get_backend('qasm_simulator'), shots=1024)
result = job.result()

print(score)
#Print
print(result.get_counts(score))

