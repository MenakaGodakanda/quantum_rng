# Quantum Random Number Generator (QRNG)

This project implements a Quantum Random Number Generator (QRNG) using Qiskit, an open-source framework for quantum computing. The quantum RNG utilizes quantum superposition to generate truly random numbers, which are then compared against classical pseudo-random number generators (PRNGs).

## Overview

<img width="878" alt="Screenshot 2025-02-20 at 5 36 42 pm" src="https://github.com/user-attachments/assets/c52555ff-1f2b-4c5f-b3ac-9be52bc9a7e6" />

## Explanation:



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

### 5. Run the Classical RNG
```
python3 classical_rng.py
```

### 6. Generate 1000 Samples and Compare
```
python3 qrng_1000.py
python3 classical_rng_1000.py
```
- Classical RNG: Shows uneven distribution, minor clustering.
- Quantum RNG: More evenly distributed, demonstrating true randomness.


## Comparison of Quantum RNG and Classical RNG Distributions
### Classical RNG Distribution (First Image - Red)
- The histogram represents the distribution of 1,000 random numbers generated using a classical (pseudo-random) RNG.
- The distribution is somewhat uniform but shows irregular spikes and dips due to the deterministic nature of classical RNGs.
- Classical RNGs rely on algorithms and seed values, meaning they are not truly random but pseudo-random.
- Some bins have noticeably higher frequencies than others, indicating potential patterns or clustering effects.

### Quantum RNG Distribution (Second Image - Blue)
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


## Use Cases
- Cryptography: Secure encryption key generation.
- Simulations: Quantum-based Monte Carlo methods.
- Gaming: Fair and unbiased number generation.
- Scientific Research: True randomness for experiments.

## Project Structure
```
quantum_rng/
│── qrng.py                             # Main QRNG script
│── qrng_1000.py                        # QRNG script for generating 1000 samples
│── classical_rng.py                    # Classical RNG script
│── classical_rng_1000.py               # Classical RNG script for generating 1000 samples
│── results/
│   ├── qrng_distribution.png           # QRNG histogram
│   ├── classical_rng_distribution.png  # Classical RNG histogram
│── README.md                           # Project documentation
```

## License
This project is licensed under the MIT License.
