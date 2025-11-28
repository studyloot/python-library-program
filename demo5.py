#for create dataframe 
import pandas  as pd 
data={'Name':['Alice','Bob','Charlie','David'],
      'Age':[24,27,22,32],
    'City':['New York','Los Angeles','Chicago','Houston']}
res=pd.DataFrame(data)
#to view specific column data
#print(res['Name'])
#print(res["City"])

#for provide condition with dataframe
print(res[res["Age"]>25])