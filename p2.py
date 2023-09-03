#2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import f1_score
a = pd.read_csv('seattle-weather.csv')
print(a)
a['weather'].value_counts()
l=LabelEncoder()
a['w']=l.fit_transform(a['weather'])
print(a)
a = a.drop(['date', 'weather'], axis=1)
x = a[['temp_max', 'temp_min', 'wind']]
y = a['w']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=40)
m = LinearRegression()
m.fit(x_train, y_train)
y_predict = m.predict(x_test).round(0)
y_test = y_test.round(0)
f1score = f1_score(y_test, y_predict, average='micro')
i = np.array(range(50))
plt.scatter(i, y_predict[0:50])
plt.scatter(i, y_test[0:50])
print("F1-score:", f1score)
