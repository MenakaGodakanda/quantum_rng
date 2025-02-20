from qiskit import QuantumCircuit

num_bits = 16
qc = QuantumCircuit(num_bits)
qc.h(range(num_bits))  # Apply Hadamard gate to all qubits
qc.measure_all()

print(qc.draw("text"))  # Display the circuit in ASCII

