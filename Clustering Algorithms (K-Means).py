import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Generate sample data
np.random.seed(0)
X = np.random.rand(100, 2)

# Initialize and fit model
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

# Predictions
labels = kmeans.labels_

# Plot results
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.show()
