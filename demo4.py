#for create dataframe 
import pandas  as pd 
data={'Name':['Alice','Bob','Charlie','David'],
      'Age':[24,27,22,32],
    'City':['New York','Los Angeles','Chicago','Houston']}
res=pd.DataFrame(data)
#print(res)
print(res.head())
print(res.head(2)) #view specific row