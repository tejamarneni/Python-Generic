import time

def timer(func):
    def wrapper(*args):
        t1 = time.time()
        result = func(*args)
        t2 = time.time() - t1
        print(f'{func.__name__} took {round(t2,3)} seconds to run')
        return result
    return wrapper

@timer
def primelist(num):
    # Initialize the list of prime numbers with 2 (the only even prime)
    prime_list = [2]
    # Start checking for prime numbers from 3 (the next odd number)
    j = 3
    # Continue until we have found 'num' prime numbers
    while len(prime_list) < num:
        is_prime = True  # Assume j is prime  
        # Check if j is divisible by any odd number from 3 to sqrt(j)
        for k in range(3, int(j**0.5) + 1, 2):
            if j % k == 0:
                is_prime = False
                break  # No need to continue checking  
        if is_prime:
            prime_list.append(j)
        # Move to the next odd number
        j += 2
    return prime_list



# Example usage: Generate the first 10 prime numbers
print(primelist(10))

