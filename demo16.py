#reindex on dataframe

import pandas as pd
data=pd.DataFrame({
    'A':[10,20,30],
    'B':[20,30,40]  
    
},index=['a','b','c'])

print(data)