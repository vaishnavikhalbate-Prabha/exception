import pandas as pd
data = {

"Name": [None , "saiii" , "vaishnavi" , "maiiii" , "shreya" , "saiii"],
"Age":  [21 , 22 , None , 21 , 25 , 22],
"city": [ "Pune" ,  "solapur" , "pune" , "nashik" , "nashik" , "solapur"],


}
#print dataframe

df = pd.DataFrame(data)

#Find missing values.

print(df.isnull())

#Count missing values.

print(df.isnull().sum())

#Replace missing values with 0.

print(df.fillna(0))

#Replace missing age with average age.
avg_age = df["Age"].mean()
df["Age"] = df["Age"].fillna(avg_age)
print(df)

#Identify duplicate records.
print(df.duplicated())

#Remove duplicate records.

print(df.dropna())





