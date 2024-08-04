import numpy as np

# Generate sample data
np.random.seed(0)
X = np.random.rand(100, 1)
y = 3 * X.squeeze() + 2 + np.random.randn(100)

# Importing models
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

# Initialize models
model1 = LinearRegression()
model2 = DecisionTreeRegressor()
model3 = RandomForestRegressor()

# Fit models
model1.fit(X, y)
model2.fit(X, y)
model3.fit(X, y)

# Make predictions
pred1 = model1.predict(X)
pred2 = model2.predict(X)
pred3 = model3.predict(X)

# Average predictions
final_pred = (pred1 + pred2 + pred3) / 3

# Display predictions
print(final_pred[:10])
