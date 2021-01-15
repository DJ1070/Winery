import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from collections import Counter
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, cohen_kappa_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

wwine = pd.read_csv('winequality-white.csv', delimiter = ';')
rwine = pd.read_csv('winequality-red.csv', delimiter = ';')

wwine['wine_type'] = 'White Wine'
rwine['wine_type'] = 'Red Wine'

wines = pd.concat([wwine, rwine])

# bucket wine quality scores into qualitative quality labels
wines['quality_label'] = wines['quality'].apply(lambda value: 'Low'
if value <= 5 else 'Medium'
if value <= 7 else 'High')

wines['quality_label'] = pd.Categorical(wines['quality_label'],
categories=['Low', 'Medium', 'High'])

wtp_features = wines.iloc[:,:-3]
wtp_feature_names = wtp_features.columns
wtp_class_labels = np.array(wines['quality_label'])
#wtp_class_labels = np.array(wines['wine_type'])

# Best results with test_size = 3 !!!
wtp_train_X, wtp_test_X, wtp_train_y, wtp_test_y = train_test_split(wtp_features, wtp_class_labels, test_size=0.2, random_state=16)

#print(Counter(wtp_train_y), Counter(wtp_test_y))
#print('Features:', list(wtp_feature_names))

# Define the scaler
wtp_ss = StandardScaler().fit(wtp_train_X)
# Scale the train set
wtp_train_SX = wtp_ss.transform(wtp_train_X)
# Scale the test set
wtp_test_SX = wtp_ss.transform(wtp_test_X)

# Random Forest Classifier Training
wtp_rf = RandomForestClassifier(n_estimators = 900, criterion = 'entropy', random_state = 5)
wtp_rf.fit(wtp_train_SX, wtp_train_y)
wtp_rf_predictions = wtp_rf.predict(wtp_test_SX)
score = accuracy_score(wtp_test_y, wtp_rf_predictions)
print(classification_report(wtp_test_y, wtp_rf_predictions))
print('Accuracy Score: ', score)

kappa_rf = cohen_kappa_score(wtp_test_y, wtp_rf_predictions)
print('Kappa: ', kappa_rf)
