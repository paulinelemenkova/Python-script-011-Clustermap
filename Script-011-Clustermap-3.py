#!/usr/bin/env python
# coding: utf-8
#
import numpy as np
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
import os
#
os.chdir('/Users/pauline/Documents/Python')
df = pd.read_csv("Tab-Bathy.csv")
sb.set(style="white")
sb.set(color_codes=True)
#
g = sb.clustermap(df, cmap="BuPu")
rotation = 45
for i, ax in enumerate(g.fig.axes):   # getting all axes of the fig object
     ax.set_xticklabels(ax.get_xticklabels(), rotation = rotation)
g.fig.suptitle('Mariana Trench: Clustermap of the bathymetric observations. \nDataset: 25 cross-section profiles, 518 observations in each') 
plt.subplots_adjust(bottom=0.20,top=0.90, right=0.90, left=0.10)
plt.show()
