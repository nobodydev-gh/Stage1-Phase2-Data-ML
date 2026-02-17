import pandas as pd

people = {
    'first' : ["name1", "name2", "name3"],
    'last'  : ['last1', "last2", 'last3'],
    'email' : ['name1last1@gmail.com', 'name2last2@gmail.com', 'name3last3@gmail.com']
}


df=pd.DataFrame(people)

print(df)

print(df['last'] == 'last3')

filt=df['last'] == 'last3'

print(df[filt])

print(df.loc[filt, 'email'])


print('------------------------')



filt =(df['last'] == 'last2') & (df['first'] == 'name2')
# filt =(df['last'] == 'last2') | (df['first'] == 'name2')

print(df.loc[filt, 'email'])


# not filt
print(df.loc[-filt, 'email'])







df = pd.read_csv('/home/rohan/DEV/Stage1-Phase2-Data-ML/' \
'02_Pandas/data/stack-overflow-developer-survey-2025/survey_results_public.csv')


## Filter String

countries = ['Ukraine','India', 'Netherlands']
filt = df['Country'].isin(countries)


print(df.loc[filt,'Country'])

print(df.columns)



####
filt = df['EdLevel'].str.contains('Master’s degree',na=False)

print(df.loc[filt,'EdLevel'])




