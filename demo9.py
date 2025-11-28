import pandas as pd
data={

    "a":[10,20,22],
}
df=pd.DataFrame(data)
df["a"]=df["a"].apply(lambda x:x+5)
print(df)