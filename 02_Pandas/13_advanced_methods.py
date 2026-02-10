import pandas as pd
import numpy as np

# Sample Data
df = pd.DataFrame({
    'name': ['Rohan', 'Hema', 'Ravi', 'Hema', 'Rohan'],
    'age': [21, 22, 23, 22, 21],
    'country': ['India', 'USA', 'India', 'UK', 'India']
})

print(df)

# -------------------------
# UNIQUE / NUNIQUE
print(df['name'].unique())
print(df['name'].nunique())

# -------------------------
# VALUE COUNTS
print(df['country'].value_counts())
print(df['country'].value_counts(normalize=True))

# -------------------------
# APPLY & LAMBDA
print(df['age'].apply(lambda x: x + 5))

# -------------------------
# MAP
mapping = {'Rohan': 'Engineer', 'Hema': 'Scientist'}
print(df['name'].map(mapping))

# -------------------------
# REPLACE
df['country'] = df['country'].replace({'UK': 'United Kingdom'})
print(df)

# -------------------------
# STRING METHODS
df['name_upper'] = df['name'].str.upper()
print(df)

# -------------------------
# CONTAINS / FILTER STRINGS
print(df[df['country'].str.contains('India', na=False)])

# -------------------------
# CLIP
ages = pd.Series([5, 15, 25, 35])
print(ages.clip(lower=10, upper=30))

# -------------------------
# WHERE
print(df['age'].where(df['age'] > 21, 'Young'))

# -------------------------
# SORT COMPLEX
print(df.sort_values(by=['country', 'age'], ascending=[True, False]))
