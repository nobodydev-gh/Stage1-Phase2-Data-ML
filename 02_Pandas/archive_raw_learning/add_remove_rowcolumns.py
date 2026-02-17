import pandas as pd


people = {
    'first' : ["name1", "name2", "name3"],
    'last'  : ['last1', "last2", 'last3'],
    'email' : ['name1last1@gmail.com', 'name2last2@gmail.com', 'name3last3@gmail.com']
}

df = pd.DataFrame(people)

print(df)


## adding columns

df['fullname'] = df['first'] + ' ' + df['last']

print(df)



##deleteing columns

df.drop(columns=['first', 'last'])  ## it just give us view it wil not apply
df.drop(columns=['first', 'last'], inplace= True)  ## this will apply the changes

print(df)


#split the fullname column into two columns


print(df['fullname'].str.split(' ', expand=True))


df[['first', 'last']] = df['fullname'].str.split(' ', expand=True)

print(df)



## add single row

# df.append({'first': "hello","last": "hi"}, ignore_index=True)


new_row = pd.DataFrame([{'first': "hello","last": "hi"}])

df =pd.concat([df,new_row])

print(df)



## dlete last row

print(df.drop(index=0))

# print(df)