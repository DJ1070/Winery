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
#sns.set_theme(style='whitegrid')
sns.set_theme(style='whitegrid', palette = ('c', 'red', 'm'))

#g = sns.jointplot(x=wwine['free sulfur dioxide'], y = wwine['total sulfur dioxide'], data = wwine, kind='scatter', xlim=(0, 150), ylim=(0, 300), color = 'c')
#h = sns.jointplot(x=rwine['free sulfur dioxide'], y = rwine['total sulfur dioxide'], data = rwine, kind='scatter', xlim=(0, 150), ylim=(0, 300), color = 'red')
g = sns.jointplot(x=wwine['free sulfur dioxide'], y = wwine['total sulfur dioxide'], data = wwine, kind='scatter', xlim=(0, 150), ylim=(0, 300), hue = wwine['quality_label'], legend = False)
h = sns.jointplot(x=rwine['free sulfur dioxide'], y = rwine['total sulfur dioxide'], data = rwine, kind='scatter', xlim=(0, 150), ylim=(0, 300), hue = rwine['quality_label'], legend = False)
#g = sns.catplot(
#    data=wines, kind="bar",
#    x="quality", y="free sulfur dioxide", hue="wine_type",
#    ci="sd", palette=('g', 'r'), alpha=.6, height=6
#)
#g.despine(left=True)
g.set_axis_labels("Free Sulfur Dioxide", "Total Sulfur Dioxide", fontsize=20)
h.set_axis_labels("Free Sulfur Dioxide", "Total Sulfur Dioxide", fontsize=20)   

plt.show()