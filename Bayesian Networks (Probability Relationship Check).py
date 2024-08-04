import numpy as np
import pandas as pd
from pomegranate import BayesianNetwork

# Sample data generation
np.random.seed(0)
data = pd.DataFrame(data={
    'A': np.random.binomial(1, 0.5, size=1000),
    'B': np.random.binomial(1, 0.7, size=1000),
    'C': np.random.binomial(1, 0.8, size=1000)
})

# Create a Bayesian Network
model = BayesianNetwork.from_samples(data, algorithm='exact')

# Check probability relationships
print(model.probability([1, 0, 1]))
