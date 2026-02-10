import pandas as pd

people = {
    'first': ['a', 'b', 'c'],
    'last': ['x', 'y', 'z']
}

df = pd.DataFrame(people)

df.rename(columns={'first': 'FirstName'}, inplace=True)
df['FirstName'] = df['FirstName'].str.upper()

print(df)
