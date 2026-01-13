from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import numpy as np

# 1. Prepare your data (1000 samples, 1 feature)
X = np.random.randint(100, 1000, size=(1000, 1))
y = (X > 500).astype(int).ravel() # Dummy target: 1 if > 500, else 0

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 2. Define the Pipeline
# Each step is a tuple: ("name", transformer/estimator)
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression())
])

# 3. The Magic Step
# This fits the scaler AND the model on X_train ONLY
pipe.fit(X_train, y_train)

# 4. Predict
# This automatically uses the scaler's 'training rules' on X_test 
# before passing it to the model for prediction.
predictions = pipe.predict(X_test)

print(f"Model Accuracy: {pipe.score(X_test, y_test)}")
