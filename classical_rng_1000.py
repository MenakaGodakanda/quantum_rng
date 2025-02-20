import random
import matplotlib.pyplot as plt

def classical_rng(num_bits=16):
    """
    Generate a classical random number.
    """
    random_number = random.getrandbits(num_bits)
    return bin(random_number)[2:].zfill(num_bits)  # Convert to binary

def generate_classical_samples(sample_size=1000, num_bits=16):
    """
    Generate multiple classical random numbers and analyze distribution.
    """
    numbers = [int(classical_rng(num_bits), 2) for _ in range(sample_size)]

    # Plot histogram
    plt.hist(numbers, bins=50, alpha=0.7, color='red', label="Classical RNG")
    plt.xlabel("Random Number")
    plt.ylabel("Frequency")
    plt.title(f"Classical RNG Distribution ({sample_size} samples)")
    plt.legend()
    plt.savefig("results/classical_rng_distribution.png")
    plt.show()

if __name__ == "__main__":
    generate_classical_samples()
