import random

def classical_rng(num_bits=16):
    """
    Generate a classical random number.
    """
    random_number = random.getrandbits(num_bits)
    return bin(random_number)[2:].zfill(num_bits)  # Convert to binary

if __name__ == "__main__":
    num_bits = 16
    random_bits = classical_rng(num_bits)
    print(f"Classical Random Number (Binary): {random_bits}")
    print(f"Classical Random Number (Decimal): {int(random_bits, 2)}")

