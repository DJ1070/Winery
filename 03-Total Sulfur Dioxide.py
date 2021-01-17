import pandas as pd
import numpy as np
import statistics as st
import matplotlib.pyplot as plt
import seaborn as sns

wwine = pd.read_csv('winequality-white.csv', delimiter = ';')
rwine = pd.read_csv('winequality-red.csv', delimiter = ';')

wwine['wine_type'] = 'White'
rwine['wine_type'] = 'Red'

wines = pd.concat([wwine, rwine])

# bucket wine quality scores into qualitative quality labels
wines['quality_label'] = wines['quality'].apply(lambda value: 'Low'
if value <= 5 else 'Medium'
if value <= 7 else 'High')

wines['quality_label'] = pd.Categorical(wines['quality_label'],
categories=['Low', 'Medium', 'High'])

sns.set_theme(style='whitegrid')
fig, ax = plt.subplots(1, 1, figsize=(10, 10))

#sns.kdeplot(wwine['total sulfur dioxide'], ax = ax, data = wwine, color = 'c', shade='True').set_title("Total Sulfur Dioxide")
sns.kdeplot(wwine['total sulfur dioxide'], ax = ax, data = wwine, color = 'c', shade='True')
sns.kdeplot(rwine['total sulfur dioxide'], ax = ax, data = rwine, color = 'red', shade='True')
ax.set_xlabel('Total Sulfur Dioxide', fontsize = 20)
ax.set_ylabel('Density', fontsize = 20)

print(wwine['total sulfur dioxide'].min())
print(wwine['total sulfur dioxide'].max())
print(rwine['total sulfur dioxide'].min())
print(rwine['total sulfur dioxide'].max())
plt.show()