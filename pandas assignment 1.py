import pandas as pd
Data = {
    "Name":[ "vaishnavi", "saii", "shravani","shreya"],

    "Age": [21 , 20 , 16 , 19],

    "City": ["Pune" ,"Mumbaii" ,"Nashik" , "Banglore"]  
        }
df = pd.DataFrame(Data)

print(df)