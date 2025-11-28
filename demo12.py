#apply with dataframe
import pandas as pd 
data={
    "A":[10,20,30],     
    "B":[5,15,25],
}
df=pd.DataFrame(data)
df["A"]=df["A"].apply(lambda x:x*2)
print(df["A"])

df["B"]=df["B"].apply(lambda x:x+3)
print(df["B"])