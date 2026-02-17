import pandas as pd


df = pd.read_csv('/home/rohan/DEV/Stage1-Phase2-Data-ML/02_Pandas/data/' \
'stack-overflow-developer-survey-2025/survey_results_public.csv')

# pd.set_option('display.max_columns', 100)
# print(df.head())


print(df['ConvertedCompYearly'].head(10))
print(df['ConvertedCompYearly'].median())

# print(df['ConvertedCompYearly'].)

print("---------------------------------------")
print(df.median(numeric_only=True))


print("-------------------------------------")
print(df.describe())

print(df["ConvertedCompYearly"].count())  # it will give the value of how many are answered for this 

print(df['PurchaseInfluence'].value_counts())

print(df['RemoteWork'].value_counts())

print(df['RemoteWork'].value_counts(normalize=True))  ## this will give the percentage count

print("-----------------------------")


##grouping


print(df['Country'].count())

print("-----------------------------")



print(df['Country'].value_counts())

print("-----------------------------")


country_group = df.groupby('Country')

print(country_group.get_group('India'))

## for single  country result
filt = df['Country'] == 'India'

print(df.loc[filt]['PurchaseInfluence'].value_counts())


print("---------------------------")


print(country_group['PurchaseInfluence'].value_counts())


print("------------------------------------------")

print(country_group['PurchaseInfluence'].value_counts().loc['Pakistan'])


print(country_group['ConvertedCompYearly'].median())


print("-----------------------------------")
print(country_group['ConvertedCompYearly'].median().loc["India"])

##the above is for onlu one agregate function 

print("----------------------------------")

##for mutiple aggregate functions

print(country_group['ConvertedCompYearly'].agg(['median','count']).loc["India"])



print(country_group['AIAgentExternal'].apply(lambda x: x.str.contains('ChatGPT').sum()))



country_count = df["Country"].value_counts()


country_uses_chatgpt = country_group['AIAgentExternal'].apply(lambda x: x.str.contains('ChatGPT').sum())

chatgpt_users = pd.concat([country_count, country_uses_chatgpt], axis = 'columns', sort = False)

print(chatgpt_users)

chatgpt_users.rename(columns={"count":"Total_Respondants","AIAgentExternal":"Chatgpt_users" },inplace = True)


print(chatgpt_users)

print("---------------------------------")

## to print the percentage
percentage=chatgpt_users["Percentagechatgptusers"] = (chatgpt_users["Chatgpt_users"]/chatgpt_users["Total_Respondants"]) * 100
print("---------------------------------")
print(percentage)

print("-------------------------------")


print(chatgpt_users)

print("---------------------------")



chatgpt_users.sort_values(by="Percentagechatgptusers", ascending=False,inplace=True)

print(chatgpt_users)