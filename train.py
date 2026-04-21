from sklearn.linear_model import LinearRegression
import numpy as np
import pickle

X = np.array([[1000],[1500],[2000]])
y = np.array([200000,300000,400000])

model = LinearRegression()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))
print("Model saved")
