import pandas as pd
import numpy as np

df = pd.DataFrame({
    'age':[25, np.nan, 30],
    'name':['A', 'B', None]
})

print(df.dropna())
print(df.fillna(0))

df['age'] = df['age'].astype(float)
print(df['age'].mean())
