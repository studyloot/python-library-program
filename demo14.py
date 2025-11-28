


import pandas as pd

data = {
    'A': [10, 20, 30, 40],
    'B': [5, 15, 25, 35],
    'C': [2, 4, 6, 8]
}

df = pd.DataFrame(data)
print(df)

#for axis =0 columnwise
res1=df.apply(lambda x:x.max()-x.min(),axis=0)
print(res1)

#for axis=1 row wise
res2=df.apply(lambda x:x.max()-x.min(),axis=1)  
print(res2)

