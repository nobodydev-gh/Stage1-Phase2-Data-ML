import pandas as pd

df = pd.read_csv('/home/rohan/DEV/Stage1-Phase2-Data-ML/02_Pandas/data/stack-overflow-developer-survey-2025/survey_results_public.csv')

print(df)

print(df.head())   #give the first 5 rows

print(df.head(10))  # give custom rows so i have given 10


print(df.tail())   #give the last 5 rows

print(df.tail(8)) # give custom last rows



print(df.shape)

print(df.info())

schema_df = pd.read_csv('/home/rohan/DEV/Stage1-Phase2-Data-ML/02_Pandas/data/stack-overflow-developer-survey-2025/survey_results_schema.csv')

print(schema_df)


print(df['Year'])

# print(df.Year)
print("\n-------------------------\n")

print(df[['Year', 'Production']])

print("\n-------------------------\n")

print(df[['Year', 'Production']].head())

print("\n-------------------------\n")

print(df[['Year', 'Production']].tail())

print("\n-------------------------\n")

print(df.columns)  # give the  name of all the columns

print("\n-------------------------\n")

print(df.iloc[2])                    #iloc       # allows us to access rows by integer location

print("\n-------------------------\n")

print(df.iloc[0])

print("\n-------------------------\n")

#for multiple rows

print(df.iloc[[0,1]])

