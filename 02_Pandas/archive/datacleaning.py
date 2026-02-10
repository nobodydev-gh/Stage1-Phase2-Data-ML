import pandas as pd
import numpy as np


people = {
    'first': ['Corey', 'Jane', 'John', 'Chris', np.nan, None, 'NA'], 
    'last': ['Schafer', 'Doe', 'Doe', 'Schafer', np.nan, np.nan, 'Missing'], 
    'email': ['CoreyMSchafer@gmail.com', 'JaneDoe@email.com', 'JohnDoe@email.com', None, np.nan, 'Anonymous@email.com', 'NA'],
    'age': ['33', '55', '63', '36', None, None, 'Missing']
}



df = pd.DataFrame(people)


## removing custom missing values

df.replace('NA', np.nan, inplace=True)
df.replace("Missing", np.nan, inplace=True)

print(df)

print("\n")

print(df.dropna())

print("\n")
# expanded

print(df.dropna(axis = 'index', how ='any'))

print("\n")

print(df.dropna(axis = 'columns', how= "all"))

### drop rows that are missing vales in specific column

print("\n")

print(df.dropna(axis='index', how="any", subset=["age"]))


#for string to find na 
print(df.isna())


#for missing vales like NaN for int

print(df.fillna(0))




print(df.dtypes)


df['age'] = df['age'].astype(float)

print(df["age"].mean())

print(df.dtypes)




#########################   ON CSV FIELS

na_vals = ['NA', 'Missing']    ##values to remove
df = pd.read_csv('/home/rohan/DEV/Stage1-Phase2-Data-ML/02_Pandas/data/' \
'stack-overflow-developer-survey-2025/survey_results_public.csv', index_col='ResponseId',na_values=na_vals)

print(df.head(10))

print("\n")


print(df['YearsCode'].dtypes)

print(df['YearsCode'].mean())

print(df["YearsCode"].unique())


print(df["YearsCode"].agg(['median','mean']))