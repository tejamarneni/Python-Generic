import numpy as np
from tdigest import TDigest

# 1. Create a "Huge" dataset (simulated)
# A mix of two distributions to make it interesting
data_part1 = np.random.normal(loc=50, scale=10, size=50000)
data_part2 = np.random.normal(loc=100, scale=20, size=50000)
full_data = np.concatenate([data_part1, data_part2])

# 2. Initialize the TDigest engine
# K parameter controls accuracy/memory trade-off (higher K = more accurate)
digest = TDigest()

# 3. Process in Batches (Streaming)
chunk_size = 10000
for i in range(0, len(full_data), chunk_size):
    chunk = full_data[i : i + chunk_size]
    
    # TDigest updates element-by-element or via batch_update if supported
    # The python implementation usually takes an update loop or batch update
    digest.batch_update(chunk) 

# 4. Query the Results
estimated_median = digest.percentile(50)  # 50th percentile = Median
estimated_99th = digest.percentile(99)    # 99th percentile

# 5. Compare with "True" NumPy results (calculated in memory)
true_median = np.median(full_data)
true_99th = np.percentile(full_data, 99)

print(f"--- Median (50th Percentile) ---")
print(f"True Value:      {true_median:.5f}")
print(f"T-Digest Est:    {estimated_median:.5f}")
print(f"Error:           {abs(true_median - estimated_median):.5f}")

print(f"\n--- 99th Percentile ---")
print(f"True Value:      {true_99th:.5f}")
print(f"T-Digest Est:    {estimated_99th:.5f}")
