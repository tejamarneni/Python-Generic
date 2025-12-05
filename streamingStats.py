import numpy as np

class StreamingStats:
    def __init__(self):
        self.n = 0          # Total count
        self.mean = 0.0     # Running mean
        self.M2 = 0.0       # Sum of squares of differences from the mean

    def add_batch(self, batch):
        """
        Updates the running statistics with a new batch of data.
        Uses Chan's Algorithm for parallel/batch updates.
        """
        batch = np.array(batch)
        
        # 1. Calculate stats for the current batch (b)
        n_b = len(batch)
        if n_b == 0:
            return
            
        mean_b = np.mean(batch)
        # M2_b is the sum of squared differences for this batch
        # M2 = variance * n (for population) OR variance * (n-1) (for sample)
        # We use simple sum((x - mean)^2) here
        M2_b = np.sum((batch - mean_b)**2)

        # 2. If this is the very first batch, just store it
        if self.n == 0:
            self.n = n_b
            self.mean = mean_b
            self.M2 = M2_b
            return

        # 3. Merge current batch stats (b) with global stats (a)
        n_a = self.n
        mean_a = self.mean
        M2_a = self.M2

        delta = mean_b - mean_a
        
        # Update Global Count
        self.n = n_a + n_b
        
        # Update Global Mean
        # Formula: new_mean = old_mean + delta * (n_batch / total_n)
        self.mean = mean_a + delta * (n_b / self.n)
        
        # Update Global M2 (Sum of Squares)
        # This is the "magic" formula that combines variances correctly
        self.M2 = M2_a + M2_b + (delta ** 2) * (n_a * n_b / self.n)

    def get_stats(self):
        """Returns a dictionary of the current statistics."""
        if self.n < 2:
            return {"mean": self.mean, "std_dev": 0.0, "variance": 0.0}

        # Calculate final variance/std based on M2
        variance_sample = self.M2 / (self.n - 1)
        std_sample = np.sqrt(variance_sample)
        
        return {
            "count": self.n,
            "mean": self.mean,
            "variance_sample": variance_sample,
            "std_sample": std_sample
        }

# --- Example Usage ---

# 1. Create a "Huge" dataset
full_data = np.random.normal(loc=50, scale=10, size=100000)

# 2. Initialize our streaming calculator
stats_engine = StreamingStats()

# 3. Simulate reading in chunks (e.g., from a CSV)
chunk_size = 10000
for i in range(0, len(full_data), chunk_size):
    chunk = full_data[i : i + chunk_size]
    stats_engine.add_batch(chunk)

# 4. Compare results
my_results = stats_engine.get_stats()
numpy_results = np.std(full_data, ddof=1)

print(f"True Mean (NumPy):     {np.mean(full_data):.5f}")
print(f"Streaming Mean:        {my_results['mean']:.5f}")
print("-" * 30)
print(f"True Std Dev (NumPy):  {numpy_results:.5f}")
print(f"Streaming Std Dev:     {my_results['std_sample']:.5f}")
