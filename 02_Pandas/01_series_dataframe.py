import pandas as pd

people = {
    'first': ['name1', 'name2', 'name3'],
    'last': ['last1', 'last2', 'last3'],
    'email': ['name1@gmail.com', 'name2@gmail.com', 'name3@gmail.com']
}

df = pd.DataFrame(people)

print(df)
print(df['email'])         # Series
print(df[['last', 'email']])
print(df.columns)

print(df.iloc[0])
print(df.loc[0, 'email'])



