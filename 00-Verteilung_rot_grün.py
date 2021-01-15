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

sns.set_theme(style='whitegrid', color_codes=True)
g = sns.catplot( x='quality',
             kind="count", 
             legend = False,
             palette = ('c', 'red'),
             hue="wine_type",
             data=wines,
             height=6,
             aspect=1.0)

#g.fig.suptitle('Distribution of White and Red Wine in Given Dataset by Quality')
#g.legend.set_title("Wine Color")
g.set_axis_labels("Quality", "Count",fontsize=20)
#plt.savefig("Countplot_or_barplot_with_Seaborn_catplot.png")
plt.show()