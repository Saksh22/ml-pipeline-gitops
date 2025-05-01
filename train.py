from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

data = load_iris()
X, y = data.data, data.target

model = LogisticRegression()
model.fit(X, y)

print("Model trained with accuracy:", model.score(X, y))
