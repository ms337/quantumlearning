from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer

q = QuantumRegister(1)
c = ClassicalRegister(1)

mes = QuantumCircuit(q,c)
mes.measure(q,c)

job = execute(mes, backend = Aer.get_backend('qasm_simulator'), shots = 1024)
result = job.result()

print(mes)
print(result.get_counts(mes))