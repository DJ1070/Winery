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
sns.set_theme(style='whitegrid', palette = ('grey', 'blue', 'green', 'yellow', 'orange','red', 'white'))

#Plotting the differences in Alcohol by wine type and quality
fig, ax = plt.subplots(2, 2, figsize=(10, 10))

#fig.suptitle('Difference in Alcohol Level by Wine Type and  Quality', fontsize=14)

fig.subplots_adjust(top=0.85, wspace=0.3)

sns.boxplot(x="quality", y="alcohol", data=wines[wines['wine_type'] == 'White'], ax=ax[0][0]).set_title("White Wine by Quality", fontsize=15)

ax[0][0].set_xlabel(None)
ax[0][0].set_ylabel("Wine Alcohol %",size = 15,alpha=0.8)
ax[0][0].set(ylim=(7, 15))

sns.boxplot(x="quality", y="alcohol", data=wines[wines['wine_type'] == 'Red'], ax=ax[0][1]).set_title("Red Wine by Quality", fontsize=15)

ax[0][1].set_xlabel(None)
ax[0][1].set_ylabel(None)
ax[0][1].set(ylim=(7, 15))
#ax[0][1].set_yticks([])

sns.boxplot(x="quality", y="residual sugar", data=wines[wines['wine_type'] == 'White'], ax=ax[1][0])

ax[1][0].set_xlabel(None)
ax[1][0].set_ylabel("Residual Sugar",size = 15, alpha=0.8)
ax[1][0].set(ylim=(0, 25))

sns.boxplot(x="quality", y="residual sugar", data=wines[wines['wine_type'] == 'Red'], ax=ax[1][1])

ax[1][1].set_xlabel(None)
ax[1][1].set_ylabel(None)
ax[1][1].set(ylim=(0, 25))

plt.show()
