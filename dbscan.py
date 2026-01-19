

import pandas as pd
import numpy as np

df=pd.read_csv(r'/content/Mall_Customers.csv')
df.info()

df.describe()

df.columns

df.columns.isnull()

for col in df.columns:
  print(df[col].name,df[col].value_counts().unique())
  print(df[col].values)

df.shape

df['Genre']=df['Genre'].map({'Male':0,'Female':1})

from sklearn.cluster import DBSCAN
x=df[['Annual_Income_(k$)','Spending_Score']]
model=DBSCAN(eps=9,min_samples=5,metric='euclidean')
y=model.fit_predict(x)

model.labels_

import matplotlib.pyplot as plt
plt.scatter(x['Annual_Income_(k$)'],x['Spending_Score'],c=y,s=15)
plt.title('DBSCAN')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.show()

