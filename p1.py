#1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# Reading the dataset
data = pd.read_csv("lab1.csv")
# Setting the value for X and Y
x = data[['TV']]
y = data['Sales']
# Splitting the dataset
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3,random_state=40) 
# Fitting the Linear Regression model
from sklearn.linear_model import LinearRegression
slr = LinearRegression()
slr.fit(x_train, y_train)
# Intercept and Coefficient
print("Intercept:", slr.intercept_)
print("Coefficient:", slr.coef_)
# Prediction of test set
y_pred_slr = slr.predict(x_test)
print("Prediction for test set:", y_pred_slr)
# Actual value and the predicted value
slr_diff = pd.DataFrame({'Actual value': y_test, 'Predicted value': y_pred_slr})  
# Line of best fit
plt.scatter(x_test, y_test)
plt.plot(x_test, y_pred_slr, 'r')
plt.show()
# Model Evaluation
from sklearn import metrics
mean_abs_err = metrics.mean_absolute_error(y_test, y_pred_slr)
mean_sq_err = metrics.mean_squared_error(y_test, y_pred_slr)
root_mean_sq_err = np.sqrt(mean_sq_err)
print('R squared: {:.2f}'.format(slr.score(x_test, y_test) * 100))
print('Mean Absolute Error:', mean_abs_err)
print('Mean Squared Error:', mean_sq_err)
print('Root Mean Square Error:', root_mean_sq_err)

