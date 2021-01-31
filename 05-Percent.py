import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statistics as st
import seaborn as sns

wwine = pd.read_csv('winequality-white.csv', delimiter = ';')
rwine = pd.read_csv('winequality-red.csv', sep = ';')

wwine['wine_type'] = 'White Wine'
rwine['wine_type'] = 'Red Wine'

wines = pd.concat([wwine, rwine])

# What does this do? 
#wwine['quality'] = wwine['quality'].astype(int)
#wwine['quality'] = pd.to_numeric(wwine['quality'])
#print(type(wwine['quality']))


w3 = (wwine[wwine['quality'] == 3]['quality'].count())/wwine.shape[0]*100
w4 = (wwine[wwine['quality'] == 4]['quality'].count())/wwine.shape[0]*100
w5 = (wwine[wwine['quality'] == 5]['quality'].count())/wwine.shape[0]*100
w6 = (wwine[wwine['quality'] == 6]['quality'].count())/wwine.shape[0]*100
w7 = (wwine[wwine['quality'] == 7]['quality'].count())/wwine.shape[0]*100
w8 = (wwine[wwine['quality'] == 8]['quality'].count())/wwine.shape[0]*100
w9 = (wwine[wwine['quality'] == 9]['quality'].count())/wwine.shape[0]*100

ww_quality_df = pd.DataFrame(
[[w3],
[w4],
[w5],
[w6],
[w7],
[w8],
[w9]],
index=[3, 4, 5, 6, 7, 8, 9],
columns=['quality in percent'])

r3 = (rwine[rwine['quality'] == 3]['quality'].count())/rwine.shape[0]*100
r4 = (rwine[rwine['quality'] == 4]['quality'].count())/rwine.shape[0]*100
r5 = (rwine[rwine['quality'] == 5]['quality'].count())/rwine.shape[0]*100
r6 = (rwine[rwine['quality'] == 6]['quality'].count())/rwine.shape[0]*100
r7 = (rwine[rwine['quality'] == 7]['quality'].count())/rwine.shape[0]*100
r8 = (rwine[rwine['quality'] == 8]['quality'].count())/rwine.shape[0]*100
r9 = (rwine[rwine['quality'] == 9]['quality'].count())/rwine.shape[0]*100

rw_quality_df = pd.DataFrame(
[[r3],
[r4],
[r5],
[r6],
[r7],
[r8],
[r9]],
index=[3, 4, 5, 6, 7, 8, 9],
columns=['quality in percent'])

sns.set_theme(style='whitegrid')

plt.bar(x=ww_quality_df.index.values, height=ww_quality_df['quality in percent'], color = 'c')
#g.set_labels("Quality", "Quality Level in Percent", fontsize=20)
plt.xlabel("Quality", fontsize=20)
plt.ylabel("Quality Level in Percent", fontsize=20)
plt.show()
plt.bar(x=rw_quality_df.index.values, height=rw_quality_df['quality in percent'], color = 'red')
#h.set_labels("Quality", "Quality Level in Percent of Red Wine", fontsize=20)
plt.xlabel("Quality", fontsize=20)
plt.ylabel("Quality Level in Percent", fontsize=20)
plt.show()

#print(rwine['quality'].plot(kind='hist', bins = 10))