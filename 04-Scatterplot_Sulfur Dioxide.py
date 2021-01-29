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

#fig, ax = plt.subplots(1, 1, figsize=(10, 10))
sns.set_theme(style='whitegrid')
g = sns.jointplot(x=wwine['free sulfur dioxide'], y = wwine['total sulfur dioxide'], data = wwine, kind='scatter', xlim=(0, 150), ylim=(0, 300), palette = ('c'))
g = sns.jointplot(x=rwine['free sulfur dioxide'], y = rwine['total sulfur dioxide'], data = rwine, kind='scatter', xlim=(0, 150), ylim=(0, 300), palette = ('r'))

#g = sns.catplot(
#    data=wines, kind="bar",
#    x="quality", y="free sulfur dioxide", hue="wine_type",
#    ci="sd", palette=('g', 'r'), alpha=.6, height=6
#)
#g.despine(left=True)
g.set_axis_labels("Quality", "Free Sulfur Dioxide", fontsize=20)
#h.set_axis_labels("Quality", "Free Sulfur Dioxide", fontsize=20)
#g.legend.set_title("")

plt.show()