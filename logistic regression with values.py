# import libraries 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression

# give input and classification of pass fail
X = np.array([[100],[63],[40],[85]])
y = np.array([1,0,1,0])
X_new = np.array([[150]])


# firstly we train the model via logistic regression 
model = LogisticRegression()
# provide X and y to model 
model.fit(X,y)

# it predicts the value according to x 
y_predict = model.predict(X_new)[0]
# we also want to know probability 
probability = model.predict_proba(X_new)[0][1]


X_range = np.linspace(0,160,300).reshape(-1,1)
y_proba = model.predict(X_range)[:,1]


# pltting the sigmoid function
plt.figure(figsize=(10, 9))
plt.scatter(X_new, probability, label="Actual Data")
plt.scatter(X, y, color='blue', label="Training Data")
plt.plot(X_range, y_proba, color='red', label="sigmoid curve")
plt.xlabel("Mark")
plt.ylabel("result")
plt.title("Logistic Regression: Original Scale")
plt.legend()
plt.grid(True)
plt.show()
