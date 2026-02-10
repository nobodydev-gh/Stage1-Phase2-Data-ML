import pandas as pd

df1 = pd.DataFrame({'id':[1,2], 'name':['A','B']})
df2 = pd.DataFrame({'id':[1,2], 'salary':[100,200]})

merged = pd.merge(df1, df2, on='id', how='inner')
print(merged)
