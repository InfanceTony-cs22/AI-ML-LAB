import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Generate sample data
import numpy as np
X = np.random.rand(1000, 10)
y = np.dot(X, np.array([1.5, -2.0, 3.0, -0.5, 2.5, -1.5, 2.0, -2.5, 1.0, 0.5])) + 0.1 * np.random.randn(1000)

# Define model
model = Sequential([
    Dense(64, activation='relu', input_shape=(10,)),
    Dense(64, activation='relu'),
    Dense(1)
])

# Compile model
model.compile(optimizer='adam', loss='mse')

# Train model
model.fit(X, y, epochs=10, batch_size=32)

# Predictions
print(model.predict(X[:5]))
