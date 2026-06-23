import pandas as pd

#Create Dataframe

Data = {
    "Name":[ "vaishnavi", "saii", "shravani","shreya"],

    "Age": [21 , 20 , 16 , 19],

    "City": ["Pune" ,"Mumbaii" ,"Nashik" , "Banglore"],  

    "marks": [87 , 79 ,95, 65]

        }

#Display Dtaframe

df = pd.DataFrame(Data)
print(df)

#Save Datframe to csv

df.to_csv("student.csv",index=False)
print("\n Data saved to student.csv")
print()


#Read csv file
df = pd.read_csv("student.csv")

print(df)