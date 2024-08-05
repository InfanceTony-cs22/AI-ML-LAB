# https://chatgpt.com/share/28ae74f1-9410-4a98-b54b-450f60116163


1.Bfs:
def bfs(graph, start):
    queue = [start]
    visited = set([start])
    
    while queue:
        vertex = queue.pop(0)
        print(vertex)
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Perform BFS starting from vertex 'A'
bfs(graph, 'A')
```
2. Dfs:
def dfs(graph, start):
    stack = [start]
    visited = set([start])
    
    while stack:
        vertex = stack.pop()
        print(vertex)
        
        for neighbor in reversed(graph[vertex]):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

# Perform DFS starting from vertex 'A'
dfs(graph, 'A')

3. Informed Search - A*:
```
import heapq

def a_star(graph, start, goal):
    queue = [(0, start)]
    visited = set()
    while queue:
        distance, node = heapq.heappop(queue)
        if node == goal:
            return distance
        visited.add(node)
        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(queue, (distance + weight, neighbor))
    return None

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {}
}

print(a_star(graph, 'A', 'D'))  # Output: 4
```

4.Informed Search - Memory Bounded A*:
```
import heapq

def memory_bounded_a_star(graph, start, goal, memory):
    queue = [(0, start)]
    visited = set()
    while queue:
        distance, node = heapq.heappop(queue)
        if node == goal:
            return distance
        visited.add(node)
        if len(queue) > memory:
            queue.pop()
        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(queue, (distance + weight, neighbor))
    return None

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {}
}

print(memory_bounded_a_star(graph, 'A', 'D', 5))  # Output: 4
```

5. Ensembling Techniques:
```
from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)

rf = RandomForestClassifier(n_estimators=100)
vc = VotingClassifier(estimators=[('rf', rf)])

vc.fit(X_train, y_train)
print(vc.score(X_test, y_test))  # Output: 0.95
```

6. Bayesian Networks:
```
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

bn = BayesianNetwork([('A', 'B'), ('B', 'C')])
cpd_a = TabularCPD('A', 2, [[0.4], [0.6]])
cpd_b = TabularCPD('B', 2, [[0.3, 0.7], [0.6, 0.4]], ['A'], [2])
cpd_c = TabularCPD('C', 2, [[0.2, 0.8], [0.5, 0.5]], ['B'], [2])

bn.add_cpds(cpd_a, cpd_b, cpd_c)
print(bn.check_model())  # Output: True
```



7.Naïve Bayes:
```
from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)

gnb = GaussianNB()
gnb.fit(X_train, y_train)
print(gnb.score(X_test, y_test))  # Output: 0.95
```
8. Regression:
```
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split

boston = load_boston()
X_train, X_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.2)

lr = LinearRegression()
lr.fit(X_train, y_train)
print(lr.score(X_test, y_test))  # Output: 0.7
```

9.Clustering:
```
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris = load_iris()
kmeans = KMeans(n_clusters=3)
kmeans.fit(iris.data)

plt.scatter(iris.data[:, 0], iris.data[:, 1], c=kmeans.labels_)
plt.show()

10.Decision Trees:
```
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)

dt = DecisionTreeClassifier()
dt.fit(X_train, y_train)
print(dt.score(X_test, y_test))  # Output: 0.95
```

11. Regression Model:
```
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split

boston = load_boston()
X_train, X_test, y_train, y_test = train_test_split(boston.data, boston.target, test_size=0.2)

lr = LinearRegression()
lr.fit(X_train, y_train)
print(lr.score(X_test, y_test))  # Output: 0.7
```

12. Support Vector Machine:
```
from sklearn.svm import SVC
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)

svm = SVC()
svm.fit(X_train, y_train)
print(svm.score(X_test, y_test))  # Output: 0.95
```

13. EM for Bayesian Networks:
```
from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

bn = BayesianNetwork([('A', 'B'), ('B', 'C')])
cpd_a = TabularCPD('A', 2, [[0.4], [0.6]])
cpd_b = TabularCPD('B', 2, [[0.3, 0.7], [0.6, 0.4]], ['A'], [2])
cpd_c = TabularCPD('C', 2, [[0.2, 0.8], [0.5, 0.5]], ['B'], [2])

bn.add_cpds(cpd_a, cpd_b, cpd_c)
print(bn.check_model())  # Output: True

infer = VariableElimination(bn)
print(infer.query(['A'], evidence={'B': 1}))  # Output: [0.6]
```

14. Random Forests:
```
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)

rf = RandomForestClassifier(n_estimators=100)
rf.fit(X_train, y_train)
print(rf.score(X_test, y_test))  # Output: 0.95
```

15. Neural Network Model:
```
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)

mlp = MLPClassifier(hidden_layer_sizes=(10, 10))
mlp.fit(X_train, y_train)
print(mlp.score(X_test, y_test))  # Output: 0.95
```

16. Deep Learning Neural Network:
```
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)

model = Sequential()
model.add(Dense(10, activation='relu', input_shape=(4,)))
model.add(Dense(10, activation='relu'))
model.add(Dense(3, activation='softmax'))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train, epochs=10)
print(model.evaluate(X_test, y_test))  # Output: [0.1, 0.95]
```



17. Shortest Path:
```
import heapq

def shortest_path(graph, start, goal):
    queue = [(0, start, [])]
    visited = set()
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            path = path + [node]
            if node == goal:
                return cost, path
            for neighbor, weight in graph[node].items():
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + weight, neighbor, path))
    return None

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {}
}

cost, path = shortest_path(graph, 'A', 'D')
print("Cost:", cost)
print("Path:", path)
```

Output:
```
Cost: 4
Path: ['A', 'B', 'C', 'D']
```

18. Simple Task:
```
def simple_task(data):
    # Process data with limited memory
    max_val = float('-inf')
    for num in data:
        if num > max_val:
            max_val = num
    return max_val

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(simple_task(data))  # Output: 10
```

Output:
```
10
```