# -*- coding: utf-8 -*-
"""Zomatoinsights

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dMvzNKfhxoegYDPfGlu4F3RyhT41Pjx6
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

df=pd.read_csv("/content/zomato.csv",encoding='latin-1')

df.head()

df.shape

df.columns

df.info()

df.describe()

#missing value
#explore abput nuberical variables
#explore about categorical variable
#finding  relationship between features

df.isnull().sum()

[features for features in df.columns if df[features].isnull().sum()>1]



sns.heatmap(df.isnull(),yticklabels=False,cbar=False)



df.info()

df.City.value_counts()

city_names=df.City.value_counts().index

city_value=df.City.value_counts().values

plt.pie(x=city_value[:4],labels=city_names[:4],autopct='%1.2f%%')

df.columns

ratings=df.groupby(['Aggregate rating','Rating color','Rating text']).size().reset_index().rename(columns={0:'Rating_Count'})

ratings.head()

ratings.shape

ratings['Rating_Count'].sum()

import matplotlib
matplotlib.rcParams['figure.figsize']=(12,6)
sns.barplot(data=ratings,x='Aggregate rating',y='Rating_Count',hue='Rating color',palette=['white','red','orange','green','green'])

sns.countplot(x='Rating color',data=ratings,palette=['white','red','orange','green','green'])

ratings.head()

df.head()

df.columns

df.groupby([['Aggregate rating'==0],'City']).size().reset_index().head(30)

df[df['Aggregate rating']==0].groupby('City').size().reset_index().head()

df[df['Aggregate rating'] == 0].groupby('City').size().reset_index(name='Count').head(30)

city_final=df.City.value_counts()
cityt_labed=df.City.value_counts().index

plt.pie(city_final[:5],labels=cityt_labed[:5],autopct='%1.2f%%')

!apt-get install git

!git clone https://github.com/sushantswarup/Zomato_insights_EDA.git

!ls /content