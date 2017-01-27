import matplotlib
matplotlib.use('Agg')

import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np

df = pd.read_csv("./vehicles.csv")
print(df.columns)

print(df.columns[1])

sns_plot = sns.lmplot(df.columns[0], df.columns[1], data=df, fit_reg=False)

sns_plot.axes[0,0].set_ylim(0,)
sns_plot.axes[0,0].set_xlim(0,)

sns_plot.savefig("scaterplot"+df.columns[1]+".png",bbox_inches='tight')
sns_plot.savefig("scaterplot"+df.columns[1]+".png",bbox_inches='tight')

data = df.values.T[1]

print("Mean: %f") % (np.mean(data))
print("Median: %f") % (np.median(data))
print("Var: %f") % (np.var(data))
print("std: %f") % (np.std(data))

plt.clf()
sns_plot2 = sns.distplot(data, bins=20, kde=False, rug=True).get_figure()

axes = plt.gca()
axes.set_xlabel('Millons of pounds in sales')
axes.set_ylabel('Sales count')

sns_plot2.savefig("histogram"+df.columns[1]+".png",bbox_inches='tight')
sns_plot2.savefig("histogram"+df.columns[1]+".pdf",bbox_inches='tight')

df = pd.read_csv("./newFleet.csv")

print(df.columns[1])

sns_plot = sns.lmplot(df.columns[0], df.columns[1], data=df, fit_reg=False)

sns_plot.axes[0,0].set_ylim(0,)
sns_plot.axes[0,0].set_xlim(0,)

sns_plot.savefig("scaterplot"+df.columns[1]+".png",bbox_inches='tight')
sns_plot.savefig("scaterplot"+df.columns[1]+".png",bbox_inches='tight')

data = df.values.T[1]

print("Mean: %f") % (np.mean(data))
print("Median: %f") % (np.median(data))
print("Var: %f") % (np.var(data))
print("std: %f") % (np.std(data))

plt.clf()
sns_plot2 = sns.distplot(data, bins=20, kde=False, rug=True).get_figure()

axes = plt.gca()
axes.set_xlabel('Millons of pounds in sales')
axes.set_ylabel('Sales count')

sns_plot2.savefig("histogram"+df.columns[1]+".png",bbox_inches='tight')
sns_plot2.savefig("histogram"+df.columns[1]+".pdf",bbox_inches='tight')