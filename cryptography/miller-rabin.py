import sys
import random

def is_probably_prime(n, k=10):
    """
    Checks if n is prime using k iterations of Miller-Rabin.
    Returns True if probably prime, False if definitely composite.
    """
    # Handle base cases
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0: 
        print("Even! Composite, 2 is a witness.")
        return False

    # Step 1: Find d and s such that n - 1 = 2^s * d
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    # Step 2: Run the test k times with random bases
    for i in range(k):
        a = random.randrange(2, n - 1)
        
        # The tests from the definition:
        # Check if a^d = 1 (mod n) OR a^(2^r * d) = -1 (mod n)
        
        x = pow(a, d, n) # Calculate a^d mod n efficiently

        if x == 1 or x == n - 1:
            # Passed immediate checks (n - 1 is equivalent to -1 mod n)
            continue

        # Keep squaring x to see if we hit -1 (which is n - 1)
        # We do this s - 1 times
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break # Passed later in the sequence
        else:
            # If the loop finished without breaking, we never hit n - 1.
            # It failed all checks for this base 'a'.
            print(f"Composite! Base {a} is a witness.")
            return False

    print(f"Passes {k} tests. Probably prime.")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python rabin.py <NUMBER>")
        sys.exit(1)
        
    number_to_test = int(sys.argv[1])
    is_probably_prime(number_to_test)
