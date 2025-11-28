#map with numerical data
import pandas as pd
s=pd.Series([10,20,30,40,50])
res=s.map(lambda x:x*2)
print(res)  