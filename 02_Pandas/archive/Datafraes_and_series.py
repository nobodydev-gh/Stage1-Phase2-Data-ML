import pandas as pd

people = {
    'first' : ["name1", "name2", "name3"],
    'last'  : ['last1', "last2", 'last3'],
    'email' : ['name1last1@gmail.com', 'name2last2@gmail.com', 'name3last3@gmail.com']
}


df = pd.DataFrame(people)

df

df['email']  #series


# both works same but using brackets is much good

df.email

type(df['email'])   # series= rows of single column
  # dataframe = (rows and columns) container of multiple of series objects  it is 2d

df.count()

df[['last', 'email']]


df.columns


#iloc       # allows us to access rows by integer location

df.iloc[0]     


df.iloc[2]

##  df.iloc[[rows],column]

df.iloc[[0,1], 2]

## loc   access rows by labels 
df.loc[[0,1], 'email']

df.loc[[0,1],['email', 'last']]

