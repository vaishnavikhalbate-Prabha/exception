import pandas as pd

data = {
"Employee_ID": [101 , 102 , 103 , 104] ,

"Name": ["vaishnavi" , "saii" , "mayuri" , "sakhii"],

"Department": ["AIML" , "CS", "ENTC", "CIVIL"],

"Salary": [40000 , 50000 ,80000 ,70000],

"City": ["Pune", "Mumbai" , "Nashik" , "Benglore"]
}

#print dataframe

df = pd.DataFrame(data)
print("\n employee dataframe")
print(df)

#Display employee records whose salary is greater than 50000.
print("\n employee with salary > 40000")
print(df[df["Salary"]>50000])


