# Quantum Random Number Generator (QRNG)

This project implements a Quantum Random Number Generator (QRNG) using Qiskit, an open-source framework for quantum computing. The quantum RNG utilizes quantum superposition to generate truly random numbers, which are then compared against classical pseudo-random number generators (PRNGs).

## Overview

<img width="878" alt="Screenshot 2025-02-20 at 5 36 42 pm" src="https://github.com/user-attachments/assets/c52555ff-1f2b-4c5f-b3ac-9be52bc9a7e6" />

## Installation & Setup
### 1. Clone the Repository
```
git clone https://github.com/MenakaGodakanda/quantum_rng.git
cd quantum_rng
```

### 2. Set Up a Virtual Environment
```
python3 -m venv qrng
source qrng/bin/activate
```

### 3. Install Dependencies
```
pip install qiskit qiskit-aer matplotlib numpy
```

### 4. Run the Quantum RNG
```
python3 qrng.py
```
![Screenshot 2025-02-20 164053](https://github.com/user-attachments/assets/326c746a-e7c9-4bc7-9c08-5deefc667043)
- This means the quantum circuit generated the binary number 0110, which is 6 in decimal.

#### Quantum RNG Process
- **Quantum Circuit Creation**: A quantum circuit with `n` qubits is initialized.
- **Superposition**: Hadamard gates are applied to qubits, placing them in equal superposition.
- **Measurement**: Qubits collapse randomly to `0` or `1`, producing an unbiased random bitstring.
- **Bit Conversion**: The bitstring is converted into an integer for analysis.

### 5. Run the Classical RNG
```
python3 classical_rng.py
```
![Screenshot 2025-02-20 164103](https://github.com/user-attachments/assets/0e23ca4f-7a4e-4ac4-9095-41846d365c3c)
- This means the classical RNG generated the binary number 1100110101101001, which is 52585 in decimal.

#### Classical RNG Process
- **Pseudo-Random Generation**: Uses Python's `random.randint()` to generate numbers.
- **Pattern Analysis**: Distribution is analyzed and compared against quantum randomness.

### 6. Generate 1000 Samples and Compare
- To compare the randomness between quantum and classical RNGs, we generate 1000 random numbers and visualize their distribution.

#### Quantum RNG:
```
python3 qrng_1000.py
```
- **Histogram Output**: A plot will appear and save to `results/qrng_distribution.png`.
  - The histogram should be uniformly distributed, confirming that the QRNG produces unbiased randomness.
![Screenshot 2025-02-20 165110](https://github.com/user-attachments/assets/cbc6319c-623e-4c57-b235-d941a3a3219f)

#### Classical RNG:
```
python3 classical_rng_1000.py
```
- **Histogram Output**: A plot will appear and save to `results/classical_rng_distribution.png`.
  - The classical RNG's histogram should also be uniformly distributed, but it relies on deterministic algorithms.
![Screenshot 2025-02-20 164636](https://github.com/user-attachments/assets/9c64e1de-199e-412f-a068-8ff8cc06d001)

#### Summary
- After running the scripts, the `results/` folder will contain `qrng_distribution.png` and `classical_rng_distribution.png`. <br>
![Screenshot 2025-02-20 171427](https://github.com/user-attachments/assets/ffcb1bea-c516-48f6-a7eb-ed1455f823f6)

- Both distributions should look fairly uniform, but the quantum version provides true randomness, unlike the classical RNG.
- Classical RNG: Shows uneven distribution, minor clustering.
- Quantum RNG: More evenly distributed, demonstrating true randomness.

## Comparison of Quantum RNG and Classical RNG Distributions
### Classical RNG Distribution (Red Color Distribution)
- The histogram represents the distribution of 1,000 random numbers generated using a classical (pseudo-random) RNG.
- The distribution is somewhat uniform but shows irregular spikes and dips due to the deterministic nature of classical RNGs.
- Classical RNGs rely on algorithms and seed values, meaning they are not truly random but pseudo-random.
- Some bins have noticeably higher frequencies than others, indicating potential patterns or clustering effects.

### Quantum RNG Distribution (Second Color Distribution)
- This histogram represents the distribution of 1,000 random numbers generated using a quantum RNG.
- The distribution appears more uniform compared to the classical RNG, as quantum randomness is inherently unbiased.
- Since quantum RNGs leverage quantum superposition and measurement, they provide true randomness, free from algorithmic patterns.
- The frequency variations between bins are more evenly spread, supporting the claim of unbiased randomness.

### Key Differences and Observations
| Feature |	Classical RNG |	Quantum RNG |
|---------|---------------|-------------|
| Source	| Algorithm-based (deterministic) |	Quantum superposition (true randomness) |
| Uniformity |	Irregular spikes and dips	| More evenly spread distribution |
| Predictability |	Can be predicted if the seed is known	| Fundamentally unpredictable |
| Bias or Clustering |	Shows some uneven clustering |	Less biased and more uniform |

### Conclusion
- The quantum RNG provides a more evenly distributed and unbiased set of numbers, demonstrating the benefits of quantum-based randomness.
- Classical RNGs, while useful, are not truly random and can introduce patterns, as seen in the variations of bar heights in the histogram.
- Quantum RNGs are essential for applications requiring true randomness, such as cryptography, secure communications, and scientific simulations.

## Quantum Circuit for Random Number Generation
- You can visualize the quantum circuit in ASCII format using Qiskit's built-in `QuantumCircuit.draw('text')` method.
- Run `Quantum_circuit_rng.py` script to visualize the quantum circuit:
```
python3 Quantum_circuit_rng.py
```
- Here's how your quantum circuit would look for generating random 16-bit numbers:<br>

![Screenshot 2025-02-20 181652](https://github.com/user-attachments/assets/4fadece7-e6d4-4994-86f7-f2489f2a5c6c)

- Each qubit q_0 to q_15 starts in the |0⟩ state.
- Hadamard gates (H) are applied to each qubit, putting them into superposition, creating a random state.
- The qubits are measured, collapsing them into classical 0s or 1s.
- The resulting bitstring is interpreted as a random number.
- This is the quantum equivalent of flipping a fair coin 16 times, generating a true random binary number.

## Use Cases
- **Cryptography**: Secure encryption key generation.
- **Simulations**: Quantum-based Monte Carlo methods.
- **Gaming**: Fair and unbiased number generation.
- **Scientific Research**: True randomness for experiments.

## Project Structure
```
quantum_rng/
│── qrng.py                             # Main QRNG script
│── qrng_1000.py                        # QRNG script for generating 1000 samples
│── classical_rng.py                    # Classical RNG script
│── classical_rng_1000.py               # Classical RNG script for generating 1000 samples
│── Quantum_circuit_rng.py              # Visualize the quantum circuit of rng
│── results/
│   ├── qrng_distribution.png           # QRNG histogram
│   ├── classical_rng_distribution.png  # Classical RNG histogram
│── README.md                           # Project documentation
```

## License
This project is licensed under the MIT License.
