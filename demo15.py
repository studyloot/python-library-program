#sort_index() in series

import pandas as pd 
data=pd.Series([10,20,30],index=[2,3,4])
#res=data.sort_index()
res=data.sort_values(ascending=False)

print(res)
