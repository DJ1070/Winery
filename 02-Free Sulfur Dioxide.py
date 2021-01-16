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

fig, ax = plt.subplots(1, 1, figsize=(10, 10))
sns.set_theme(style='whitegrid')
sns.kdeplot(wwine['free sulfur dioxide'], ax = ax, data = wwine, color = 'green').set_title("Free Sulfur Dioxide")
sns.kdeplot(rwine['free sulfur dioxide'], ax = ax, data = rwine, color = 'red')
ax.set_xlabel('Free Sulfur Dioxide')

plt.show()