import pandas as pd

df = pd.read_csv('/home/rohan/DEV/Stage1-Phase2-Data-ML/02_Pandas/data/stack-overflow-developer-survey-2025/survey_results_public.csv')


filt = (df['Country'] == 'India')

india_df=df.loc[filt]


## To extarct onlt the filt to a separate csv

india_df.to_csv('data/modified_india.csv')

india_df.to_csv('data/modified_india.tsv', sep='\t')


### xlwt used to write in older excel files
### write to a newer excel use oopenpyxl
### to read a excel file we use xlrd



india_df.to_excel("data/modified.xlsx")

test = pd.read_excel('data/modified.xlsx')

print(test.head(10))


## to create a json file of the dataframe of india_df


india_df.to_json("data/modified.json")

india_df.to_json("data/modified1.json", orient='records', lines=True)

## to read json file

test1 = pd.read_json('data/modified1.json',orient='records', lines=True)




########  datafarem to SQL file type


from sqlalchemy import create_engine

import psycopg2


# engine = create_engine('mariadb://dbuser:dbass@localhost:5432/sample_db')


# india_df.to_sql('sample_table',engine)


# india_df.to_sql('sample_table',engine, if_exists='replace')

# sql_df = pd.read_sql("sample_table", engine, index_col= 'ResponceId')



USER = 'PUBLIC'
PASSWORD = ''
HOST = 'local host'

DATABASE = 'my_database'

connection_string = f"mariadb+mysqldb://{USER}:{PASSWORD}@{HOST}/{DATABASE}"

engine = create_engine(connection_string)



try:
    with engine.connect() as connection:
        print("Success")
except Exception as e:
    print(f"Error:{e}")



india_df.to_sql('sample_table', engine, if_exists='replace' )
sql_df = pd.read_sql("sample_table", engine, index_col='ResponceId')


### Run query

sql_df = pd.read_sql("SELECT * FROM sample_table", engine, index_col='ResponceId')

sql_df
