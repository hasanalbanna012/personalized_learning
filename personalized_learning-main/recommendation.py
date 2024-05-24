import numpy as np
from sklearn.tree import DecisionTreeClassifier

# Sample data
X = np.array([
    [1, 0, 1],  # Student 1's quiz results
    [0, 1, 0],  # Student 2's quiz results
    [1, 1, 1],  # Student 3's quiz results
])
y = np.array([
    1,  # Learning Path 1
    2,  # Learning Path 2
    1,  # Learning Path 1
])

# Train the model
model = DecisionTreeClassifier()
model.fit(X, y)

def recommend_path(quiz_results):
    return model.predict([quiz_results])
