import numpy as np
from sklearn.linear_model import LinearRegression

# Sample data
X = np.array([[1, 2, 3, 4, 5]]).T
y = np.array([5, 7, 9, 11, 13])

# Initialize and fit model
model = LinearRegression()
model.fit(X, y)

# Predictions
print(model.predict(np.array([[6]])))  # Predict for a new input
