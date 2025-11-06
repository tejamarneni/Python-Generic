def get_prime_factors(num):
    """
    Returns a list of the prime factors of a given number, 
    including multiplicity (e.g., 100 -> [2, 2, 5, 5]).
    """
    factors = []
    
    # First, "divide out" all factors of 2
    while num % 2 == 0:
        factors.append(2)
        num //= 2  # Integer division to update the number
        
    # Now, num must be odd. We can check only odd numbers.
    # We start at i = 3.
    i = 3
    # We only need to check up to the square root of the *remaining* number
    while i * i <= num:
        # Keep dividing by i as long as it's a factor
        while num % i == 0:
            factors.append(i)
            num //= i
        # Move to the next ODD number (i.e., skip even numbers)
        i += 2
        
    # If num is still greater than 1 after all that,
    # the remaining number itself is a large prime factor.
    if num > 1:
        factors.append(num)
        
    return factors

def analyze_prime_factors(num):
    """
    Handles special cases and prints the analysis of the number's
    prime factors in your desired format.
    """
    # --- Handle Special Cases ---
    if num < 0:
        print("Please Enter a Valid number")
        return  # Exit the function
    if num == 0 or num == 1:
        print(f"{num} is neither a composite number nor a prime number")
        return
    if num == 2:
        print("2 is an even prime number")
        print("The prime factors of 2 are: [2]")
        print("The smallest prime factor of 2 is 2")
        print("The largest prime factor of 2 is 2")
        return

    # --- Get Prime Factors Using the Optimized Function ---
    prime_factors = get_prime_factors(num)

    # --- Print Analysis ---
    
    # If the list has only one item and it's the number itself, it's prime
    if len(prime_factors) == 1:
        print(f"{num} is a prime number")
    else:
        # Your original code showed the *unique* prime factors.
        # We can get this by converting the list to a set and back.
        unique_prime_factors = sorted(list(set(prime_factors)))
        
        print(f"The prime factors of {num} are: {unique_prime_factors}")
        
        # We can just use min() and max() on the list
        print(f"The smallest prime factor of {num} is {unique_prime_factors[0]}") # or min(unique_prime_factors)
        print(f"The largest prime factor of {num} is {unique_prime_factors[-1]}") # or max(unique_prime_factors)
        
        # This is also useful information (the full factorization)
        print(f"The full prime factorization (with repeats) is: {prime_factors}")

# --- Example for testing the code ---

print("--- Analysis for 105 ---")
analyze_prime_factors(105)

print("\n--- Analysis for 13 ---")
analyze_prime_factors(13) # Test a prime number

print("\n--- Analysis for 100 ---")
analyze_prime_factors(100) # Test a number with repeated factors

print("\n--- Analysis for 1 ---")
analyze_prime_factors(1) # Test an edge case
