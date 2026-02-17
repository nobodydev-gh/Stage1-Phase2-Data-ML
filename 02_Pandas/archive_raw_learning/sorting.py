import pandas as pd

people = {
    'first' : ["rohan", "dipak ", "nitesh"],
    'last'  : ['hema', "prasad", 'kumar'],
    'email' : ['rohanhema@gmail.com', 'dipakprasad@gmail.com', 'niteshkumar@gmail.com']
}



df = pd.DataFrame(people)

print(df)


print(df.sort_values(by='first'))

print(df.sort_values(by='first', ascending=False))


print(df.sort_values(by=['last','first'], ascending=[False, True], inplace = True))



print(df)


##sorting index

print(df.sort_index())

# print(df)



df = pd.read_csv('/home/rohan/DEV/Stage1-Phase2-Data-ML/02_Pandas/data/' \
'stack-overflow-developer-survey-2025/survey_results_public.csv')



df.sort_values(by='WorkExp',ascending=False, inplace=True)

# print(df)

print(df['WorkExp'].head(10))


# print(df['JobSat'].nlargest(10))
print(df['JobSat'].nsmallest(10))


print(df.nsmallest(10,'JobSat'))
