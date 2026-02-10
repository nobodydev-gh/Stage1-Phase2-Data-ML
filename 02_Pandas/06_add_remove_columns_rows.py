import pandas as pd

df = pd.DataFrame({'A':[1,2], 'B':[3,4]})

df['C'] = df['A'] + df['B']
print(df)

df.drop(columns=['B'], inplace=True)
print(df)

new_row = pd.DataFrame([{'A':5, 'C':9}])
df = pd.concat([df, new_row])
print(df)
