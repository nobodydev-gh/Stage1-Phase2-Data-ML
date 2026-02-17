import pandas as pd

people = {
    'first' : ["name1", "name2", "name3"],
    'last'  : ['last1', "last2", 'last3'],
    'email' : ['name1last1@gmail.com', 'name2last2@gmail.com', 'name3last3@gmail.com']
}


df = pd.DataFrame(people)


print(df)

print('\n')


print(df['email'])


## Setting indexes

print(df.set_index('email'))   # it will get email in the starting column  it is only for view

# for setting permantly


print(df.set_index('email', inplace = True))


print(df)

print("\n")

print(df.index)


print(df.loc['name1last1@gmail.com', 'last'])


print(df.iloc[0])


#for resetting the index
df.reset_index(inplace=True)

print(df)



###setting index  ResponseId

df = pd.read_csv('/home/rohan/DEV/Stage1-Phase2-Data-ML/02_Pandas/data/' \
'stack-overflow-developer-survey-2025/survey_results_public.csv', index_col='ResponseId')


print(df)


print(df.iloc[3])


schema_df = pd.read_csv('/home/rohan/DEV/Stage1-Phase2-Data-ML/02_Pandas/data/' \
'stack-overflow-developer-survey-2025/survey_results_schema.csv', index_col='qname')

print(schema_df)


schema_df.sort_index()

##sort in ascending order

schema_df.sort_index(ascending=True)
print(schema_df)  #not change

# to change permanetly

schema_df.sort_index(inplace=True)

print(schema_df)

