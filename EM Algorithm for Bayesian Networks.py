import numpy as np
from pomegranate import *

# Define the distributions
d1 = DiscreteDistribution({'T': 0.6, 'F': 0.4})
d2 = ConditionalProbabilityTable(
    [['T', 'T', 0.8],
     ['T', 'F', 0.2],
     ['F', 'T', 0.4],
     ['F', 'F', 0.6]], [d1])

# Define the Bayesian Network structure
s1 = State(d1, name="A")
s2 = State(d2, name="B")

network = BayesianNetwork("Simple Network")
network.add_states(s1, s2)
network.add_edge(s1, s2)
network.bake()

# Fit model using EM
data = np.array([['T', 'T'], ['T', 'F'], ['F', 'T'], ['F', 'F']])
network.fit(data, algorithm='em')

# Display fitted distributions
print(network.probability([['T', 'T']]))
