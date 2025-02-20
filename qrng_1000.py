import os
import random
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# Define a function to generate quantum random numbers
def quantum_rng(num_bits):
    """
    Generate a quantum random number using a quantum circuit.
    """
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

    # Get counts (dictionary of measurement results)
    counts = result.get_counts()

    # Select a random outcome among the most frequent ones
    max_count = max(counts.values())  # Get highest count value
    max_count_outcomes = [key for key, value in counts.items() if value == max_count]  # Outcomes with highest count
    random_bits = random.choice(max_count_outcomes)  # Pick one randomly

    return random_bits

def generate_qrng_samples(sample_size=1000, num_bits=16):
    """
    Generate multiple quantum random numbers and analyze distribution.
    """
    # Generate quantum random numbers
    numbers = [int(quantum_rng(num_bits), 2) for _ in range(sample_size)]
    
    # Ensure results directory exists
    os.makedirs("results", exist_ok=True)

    # Plot histogram
    plt.figure(figsize=(10, 6))
    plt.hist(numbers, bins=50, alpha=0.7, color='blue', label="Quantum RNG")
    plt.xlabel("Random Number")
    plt.ylabel("Frequency")
    plt.title(f"Quantum RNG Distribution ({sample_size} samples)")
    plt.legend()
    
    # Save and show the histogram
    plt.savefig("results/qrng_distribution.png")
    plt.show()

    print(f"Generated {sample_size} quantum random numbers and saved histogram to results/qrng_distribution.png")

if __name__ == "__main__":
    generate_qrng_samples()

