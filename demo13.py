#wap to calculate max min and sum on dataframe with apply function


import pandas as pd

data = {
    'A': [10, 20, 30, 40],
    'B': [5, 15, 25, 35],
    'C': [2, 4, 6, 8]
}

df = pd.DataFrame(data)
sumdata= df.apply(lambda x: x.sum())
print(sumdata)
maxdata= df.apply(lambda x: x.max())        
print(maxdata)
mindata= df.apply(lambda x: x.min())    
print(mindata)
