import pandas as pd
data=pd.Series(["abd", "xyz","pqr"])
print(data)
result=data.map(lambda x:x.upper())
print(result)