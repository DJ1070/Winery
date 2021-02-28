import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

wwine = pd.read_csv('winequality-white.csv', delimiter = ';')
rwine = pd.read_csv('winequality-red.csv', delimiter = ';')

wwine['wine_type'] = 'white'
rwine['wine_type'] = 'red'

wines = pd.concat([wwine, rwine])

X = wines.iloc[:, -2]
y = wines['quality']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 1)


