import time
import math
from concurrent.futures import ProcessPoolExecutor

def is_prime_worker(n):
    """Heavy mathematical operation (CPU-bound)"""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
        
    # Check odd numbers up to the square root
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    # A collection of large numbers near the millions mark to process
    target_numbers = [9999991, 9999997, 10000019, 10000079, 10000103, 10000121]
    
    print(f"=== STARTING PARALLEL PRIME NUMBER EVALUATION ===")
    print(f"Analyzing {len(target_numbers)} large candidate numbers...")
    
    start_time = time.time()
    
    # Spawn a process pool mapping to the system's available cores
    with ProcessPoolExecutor() as executor:
        # Map the heavy math function across our list of numbers
        results = executor.map(is_prime_worker, target_numbers)
        
    final_mapping = dict(zip(target_numbers, results))
    duration = time.time() - start_time
    
    print("\n--- Telemetry Analysis Results ---")
    for num, prime_status in final_mapping.items():
        print(f"  * Number: {num} -> Is Prime? {prime_status}")
    print(f"\nParallel Compute Pool Execution Time: {duration:.4f} seconds")

    