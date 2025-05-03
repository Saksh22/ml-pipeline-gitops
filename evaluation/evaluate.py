import pandas as pd
from sklearn.metrics import accuracy_score
import joblib

test = pd.read_csv('/data/test.csv')
X_test = test.drop('target', axis=1)
y_test = test['target']

model = joblib.load('/data/model.pkl')
predictions = model.predict(X_test)

acc = accuracy_score(y_test, predictions)
print(f"Model Accuracy: {acc}")
