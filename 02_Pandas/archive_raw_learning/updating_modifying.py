import pandas as pd

people = {
    'first' : ["name1", "name2", "name3"],
    'last'  : ['last1', "last2", 'last3'],
    'email' : ['name1last1@gmail.com', 'name2last2@gmail.com', 'name3last3@gmail.com']
}

df =pd.DataFrame(people)

print(df)

print("\n")

print(df.columns)


## renaming the columns

df.columns = [ 'first_name', 'last_name', 'email']

print(df)

## upper case all of the columns

df.columns = [x.upper() for x in df.columns]
print(df)


##replace   replace("replacing element","modifying element")

df.columns = df.columns.str.replace('_','||')

print(df)

df.columns = [x.lower() for x in df.columns]

print(df)



df.rename(columns={'first||name': 'first', 'last||name': 'last'}, inplace=True)

print(df)

## for changing the data 

df.loc[2]  = ['NAME3', 'LAST3',"NAME3LAST3@gmail.com"]

print(df)

#or

df.at[2, 'last'] = 'last3'

print(df)

df['email'] = df['email'].str.lower()


#apply = used for calling a function on values  can be applied on dataframe or series

#on series
print(df['email'].apply(len))


def update_email(email):
    return email.upper()

df['email'] = df['email'].apply(update_email)  
print(df)

df['email'] = df['email'].apply(lambda x : x.lower())
print(df)


# for dataframe
df.apply(pd.Series.min)

print(df.map(len))

print(df.map(str.lower))


print(df["first"].map({'name1': 'rohan','name2': 'hema'}))
 ## if we dont give the other values it will be change to NaN

# SO we use replace

print(df['first'].replace({'name1': 'rohan','name2': 'hema'}))

print(df)







######### on csv data



df = pd.read_csv('/home/rohan/DEV/Stage1-Phase2-Data-ML/02_Pandas/' \
'data/stack-overflow-developer-survey-2025/survey_results_public.csv')

df.rename(columns={'EdLevel': 'StudyLevel'}, inplace=True)

print(df.columns)

print(df['StudyLevel'])

df['AIAgentOrchWrite'].replace({'NaN': 'Nothing'}, inplace=True)