from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer

# Define the Quantum and Classical Registers
q = QuantumRegister(1)
c = ClassicalRegister(1)

# Build the circuit
superposition_state_xbasis = QuantumCircuit(q, c)
superposition_state_xbasis.h(q)
#superposition_state_xbasis.barrier()
superposition_state_xbasis.h(q)
superposition_state_xbasis.measure(q, c)

# Execute the circuit
job = execute(superposition_state_xbasis, backend = Aer.get_backend('qasm_simulator'), shots=1024)
result = job.result()

print(superposition_state_xbasis)
# Print the result
print(result.get_counts(superposition_state_xbasis))
