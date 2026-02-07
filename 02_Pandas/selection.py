import pandas as pd

df = pd.read_csv('/home/rohan/DEV/Stage1-Phase2-Data-ML/02_Pandas/data/stack-overflow-developer-survey-2025/survey_results_public.csv')

print(df)


print(df.columns)

print(df['AIOpen'])


print(df['AIOpen'].value_counts())


print("---------")

### ROWS

print(df.loc[0, 'Age'])

print("---------")


print(df.loc[[0,1,2],'Age'])

print("---------")

print(df.loc[5:9,'Age'])

print("---------")

print(df.loc[5:9,'Age':'EmploymentAddl'])

#######


### COLUMNS




# print(df.iloc[0])     


# print(df.iloc[2])

# ##  df.iloc[[rows],column]

# print(df.iloc[[0,1], 2])

