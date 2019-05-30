#!/usr/bin/env python
# coding: utf-8

# In[36]:


from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
import os
os.chdir('/Users/pauline/Documents/Python')
sb.set(style="white")
df = pd.read_csv("Tab-Bathy.csv")
sb.set(color_codes=True)

#g = sb.clustermap(df, metric="correlation")
g = sb.clustermap(df, cmap="mako", robust=True)
#g = sb.clustermap(df, z_score=0)
#g = sb.clustermap(df, standard_scale=1)
rotation = 45
for i, ax in enumerate(g.fig.axes):   ## getting all axes of the fig object
     ax.set_xticklabels(ax.get_xticklabels(), rotation = rotation)
        
g.fig.suptitle('Mariana Trench: Clustermap of the bathymetric observations. \nDataset: 25 cross-section profiles, 518 observations in each. \nMethod: ignored outliers in colormap limits') 
plt.subplots_adjust(bottom=0.20,top=0.90, right=0.90, left=0.10)
plt.show()





