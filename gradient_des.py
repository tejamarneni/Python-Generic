import numpy as np
import matplotlib.pyplot as plt

# 0. Create some sample data
# Let's create data that roughly follows y = 2x + 1
X = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([2.8, 5.2, 7.1, 8.9, 11.0, 13.2, 15.1, 17.3])

# Plot the raw data
plt.scatter(X, y, label="Data")
plt.title("Linear Regression Data")
plt.xlabel("X")
plt.ylabel("y")
plt.grid(True)
plt.show()

# 1. Initialize parameters
m = 0.0  # Initial guess for slope
b = 0.0  # Initial guess for intercept

# 2. Set hyperparameters
learning_rate = 0.01
epochs = 1000
n = float(len(X)) # Number of data points

# 3. The Gradient Descent Loop
print("Starting gradient descent for linear regression...")
for i in range(epochs):
    # Calculate current predictions
    y_pred = m * X + b
    
    # Calculate the loss (MSE) - optional, but good for tracking
    loss = np.mean((y - y_pred)**2)
    
    # Calculate the gradients (partial derivatives)
    grad_m = (-2/n) * np.sum(X * (y - y_pred))
    grad_b = (-2/n) * np.sum(y - y_pred)
    
    # Update the parameters m and b
    m = m - learning_rate * grad_m
    b = b - learning_rate * grad_b
    
    if (i+1) % 100 == 0:
        print(f"Epoch {i+1:4}: m = {m:7.4f}, b = {b:7.4f}, Loss = {loss:7.4f}")

print("\nOptimization finished.")
print(f"Final model: y = {m:.4f}x + {b:.4f}")

# --- Plotting the final result ---
plt.figure(figsize=(10, 6))
plt.scatter(X, y, label="Original Data")
plt.plot(X, m * X + b, color='red', label="Fitted Line (y = {:.4f}x + {:.4f})".format(m, b))
plt.title("Linear Regression with Gradient Descent")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
