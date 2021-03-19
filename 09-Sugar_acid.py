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
wwine['quality_label'] = wwine['quality'].apply(lambda value: 'Low'
if value <= 5 else 'Medium'
if value <= 7 else 'High')

wwine['quality_label'] = pd.Categorical(wwine['quality_label'],
categories=['Low', 'Medium', 'High'])

rwine['quality_label'] = rwine['quality'].apply(lambda value: 'Low'
if value <= 5 else 'Medium'
if value <= 7 else 'High')

rwine['quality_label'] = pd.Categorical(rwine['quality_label'],
categories=['Low', 'Medium', 'High'])

wines = pd.concat([wwine, rwine])

#fig, ax = plt.subplots(1, 1, figsize=(10, 10))
sns.set_theme(style='whitegrid')
#sns.set_theme(style='whitegrid', palette = ('grey', 'blue', 'green', 'yellow', 'orange','red', 'white'))

#g = sns.jointplot(x=wwine['residual sugar'], y = wwine['citric acid'], data = wwine, kind='scatter', xlim=(0, 25), ylim=(0, 2), color = 'c')
#h = sns.jointplot(x=rwine['residual sugar'], y = rwine['citric acid'], data = rwine, kind='scatter', xlim=(0, 25), ylim=(0, 2), color = 'red')
#g = sns.jointplot(x=wwine['residual sugar'], y = wwine['citric acid'], data = wwine, kind='scatter', xlim=(0, 25), ylim=(0, 2), color = 'c', hue = wwine['quality'], legend = False)
#h = sns.jointplot(x=rwine['residual sugar'], y = rwine['citric acid'], data = rwine, kind='scatter', xlim=(0, 25), ylim=(0, 2), color = 'red', hue = rwine['quality'])

g = sns.jointplot(x=wwine['residual sugar'], y = wwine['citric acid'], data = wwine, kind='scatter', xlim=(0, 25), ylim=(0, 2), color = 'c', hue = wwine['quality'], legend = False)
h = sns.jointplot(x=rwine['residual sugar'], y = rwine['citric acid'], data = rwine, kind='scatter', xlim=(0, 25), ylim=(0, 2), color = 'red', hue = rwine['quality'])

#g = sns.catplot(
#    data=wines, kind="bar",
#    x="quality", y="free sulfur dioxide", hue="wine_type",
#    ci="sd", palette=('g', 'r'), alpha=.6, height=6
#)
#g.despine(left=True)
g.set_axis_labels("Residual Sugar", "Citric Acid", fontsize=20)
g.fig.suptitle("White Wine", fontsize = 24)
h.set_axis_labels("Residual Sugar", "Citric Acid", fontsize=20)
h.fig.suptitle("Red Wine", fontsize = 24)

plt.show()