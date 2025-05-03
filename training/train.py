import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

train = pd.read_csv('/data/train.csv')
X = train.drop('target', axis=1)
y = train['target']

model = LogisticRegression()
model.fit(X, y)

joblib.dump(model, '/data/model.pkl')
