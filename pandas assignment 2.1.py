import pandas as pd

data = {
"Employee_ID": [101 , 102 , 103 , 104] ,

"Name": ["vaishnavi" , "saii" , "mayuri" , "sakhii"],

"Department": ["AIML" , "CS", "ENTC", "CIVIL"],

"Salary": [40000 , 50000 ,80000 ,30000],

"City": ["Pune", "Mumbai" , "Nashik" , "Benglore"]
}

#print dataframe

df = pd.DataFrame(data)
print("\n employee dataframe")
print(df)

#top 3 rows
print("\n top 3 rows" )
print(df.head(3))

# last two rows

print(df.tail(2))

#Displya dataset shape
print(df.shape)

#Display column names

print(df.columns)

#Display employee records whose salary is greater than 40000.
print("\n employee with salary > 40000")
print(df[df["Salary"]>40000])


#print employees from pune
print("\n pune employees")
print(df[df["City"]=="Pune"])