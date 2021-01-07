#!/usr/bin/env python
# coding: utf-8

# # Student Performance Analysis

# ### Loading and checking data

# In[1]:


import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


from plotly.offline import init_notebook_mode, iplot, plot
import plotly as py
init_notebook_mode(connected=True)
import plotly.graph_objs as go

import plotly.figure_factory as ff


# In[15]:


stats = pd.read_csv('C:/Users/Ola/Downloads/StudentsPerformance.csv')


# In[16]:


stats.head()


# In[32]:


stats['score sum'] = stats['math score'] + stats['reading score'] + stats['writing score']
stats.head()


# In[18]:


stats.reset_index(inplace=True)
stats.rename(columns=lambda x: x.replace('index', 'id'), inplace=True)
stats.head()


# In[10]:


stats.info()


# In[19]:


stats.isnull().sum()


# In[20]:


stats.dtypes


# ### Statistical analysis

# In[23]:


stats.drop('id', axis=1, inplace=True)
stats.head()
stats.describe()


# In[33]:


# highest score 
stats[stats['score sum'] == stats['score sum'].max()]


# In[25]:


# average of score sum of students with test preparation course and without
stats.groupby('test preparation course').mean()['score sum']


# In[26]:


# gender analysis
stats['gender'] = stats['gender'].apply(lambda x : x.title())

sns.set_color_codes("muted")
sns.set_style('darkgrid')
sns.set(font_scale = 1.25)

fig, (ax1, ax2) = plt.subplots(nrows = 1, ncols = 2, figsize = (12, 6))

fig.suptitle('Gender Proportion', fontsize = 20)
sns.countplot(stats['gender'], ax = ax1, palette = 'Paired')
ax2.pie(stats['gender'].value_counts(), labels = ['Female', 'Male'], explode=(0.1, 0), autopct = '%1.1f%%', shadow = True, colors = ['lightblue', 'b'])
plt.show()


# In[27]:


# ethinicity analysis

stats['race/ethnicity'] = stats['race/ethnicity'].apply(lambda x : x.title())

sns.set_color_codes("muted")
sns.set_style('darkgrid')
sns.set(font_scale = 1.25)

fig, ax2 = plt.subplots(figsize = (12, 6))

fig.suptitle('Ethnicity Proportion', fontsize = 20)
ax2.pie(stats['race/ethnicity'].value_counts(), autopct = '%1.1f%%', shadow = True, colors = ['lightblue', 'b'])

labels = ['Group A', 'Group B', 'Group C', 'Group D', 'Group E']
plt.legend(labels, loc=(1, 0.5))
plt.show()


# In[34]:


stats.drop(['score sum'], axis=1, inplace=True)
stats.head()


# In[35]:


correlation = stats.corr()
plt.title('Correlation')
sns.heatmap(correlation, xticklabels=correlation.columns, yticklabels=correlation.columns, cmap="Blues", annot=True)


# ##### All values are strongly correlated. 

# In[36]:


# pair plot of student's scores
sns.pairplot(stats)


# In[37]:


viz1=go.Box(
    y=stats['math score'],
    name='Math Score',
    marker=dict(color='rgb(12,12,140)')
)
viz2=go.Box(
    y=stats['writing score'],
    name='Writing Score',
    marker = dict(
        color = 'rgb(12, 128, 128)')
)
viz3=go.Box(
    y=stats['reading score'],
    name='Reading Score',
    marker = dict(
        color = 'rgb(12, 105, 130)')
)

stats1=[viz1,viz2,viz3]
iplot(stats1)


# ##### The average of female students is higher except for mathematics.

# In[42]:


# Creating histograms
x1 = stats['math score']
x2 = stats['reading score']
x3 = stats['writing score']

# Group data together
hist_data = [x1, x2, x3]
colors = ['#835AF1', '#7FA6EE', '#B8F7D4']

group_labels = ['Math Score', 'Reading Score', 'Writing Score']

# Create distplot with custom bin_size
fig = ff.create_distplot(hist_data, group_labels, bin_size=2, colors=colors)
fig.update_layout(title_text = 'Distplot for each score')
fig.show()


# ##### Most scores are above 50 points from each exam. 

# In[ ]:




