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

# 1
#fig, ax = plt.subplots(1, 1, figsize=(10, 10))
#sns.set_theme(style='whitegrid')
#sns.kdeplot(wwine['fixed acidity'], ax = ax, data = wwine, color = 'green').set_title("fixed acidity")
#sns.kdeplot(rwine['fixed acidity'], ax = ax, data = rwine, color = 'red')

# 2
f, ax = plt.subplots(figsize=(10, 4))
sns.boxplot(x="quality", y="fixed acidity", palette=["c", "r"], hue = 'wine_type', data=wines, ax = ax)
ax.set_xlabel('Quality', fontsize=20)
ax.set_ylabel('Fixed Acidity', fontsize=20)
ax.legend('')   

# 3
#f, ax = plt.subplots(figsize=(10, 4))
#sns.swarmplot(x="quality", y="fixed acidity", palette=["c", "r"], hue = 'wine_type', data=wines, ax = ax)
#sns.set_theme(style='whitegrid')
#sns.despine(offset=10, trim=True)
#ax.legend(loc='upper right')
#ax.set_xlabel('Quality', fontsize=20)
#ax.set_ylabel('Fixed Acidity', fontsize=20)

# 4a Fixed Acidity
#g = sns.catplot(data=wines, x='quality', kind="violin", y='fixed acidity', palette=["c", "r"], hue='wine_type', legend = False)
#g.set_axis_labels("Quality", "Fixed Acidity", fontsize=20)
#g.fig.set_figwidth(12)
#g.fig.set_figheight(10)

# 4b Volatile Acidity
#g = sns.catplot(data=wines, x='quality', kind="violin", y='volatile acidity', palette=["c", "r"], hue='wine_type', legend = False)
#g.set_axis_labels("Quality", "Volatile Acidity", fontsize=20)
#g.fig.set_figwidth(12)
#g.fig.set_figheight(10)

# 4c Citric Acid
#g = sns.catplot(data=wines, x='quality', kind="violin", y='citric acid', palette=["c", "r"], hue='wine_type', legend = False)
#g.set_axis_labels("Quality", "Citric Acid", fontsize=20)
#g.fig.set_figwidth(12)
#g.fig.set_figheight(10)

plt.show()