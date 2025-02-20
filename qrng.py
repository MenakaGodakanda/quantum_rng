from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# Define a function to generate quantum random numbers
def quantum_rng(num_bits):
    # Create a quantum circuit with num_bits qubits
    qc = QuantumCircuit(num_bits)
    qc.h(range(num_bits))  # Apply Hadamard gate to put qubits in superposition
    qc.measure_all()

    # Use AerSimulator instead of Aer.get_backend()
    simulator = AerSimulator()

    # Transpile the circuit
    compiled_circuit = transpile(qc, simulator)

    # Run the simulation directly on the circuit
    job = simulator.run(compiled_circuit)
    result = job.result()

    # Get the most frequent outcome
    random_bits = result.get_counts().most_frequent()
    return random_bits

# Run the QRNG for 4 bits
num_bits = 4
random_bits = quantum_rng(num_bits)

print(f"Quantum Random Number (Binary): {random_bits}")
print(f"Quantum Random Number (Decimal): {int(random_bits, 2)}")

