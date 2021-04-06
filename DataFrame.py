import pandas as pd

df=pd.DataFrame()
df=pd.DataFrame([1,2,3,4,5])
df=pd.DataFrame([['ALİ',60],['AHMETİ',60],['AYŞEİ',60],['ALİHAN',60]])
data=['ALİ',60],['AHMETİ',60],['AYŞEİ',60],['ALİHAN',60]
df=pd.DataFrame(data,columns=['names','grade'],index=[1,2,3,4])
print(df)
s1=pd.Series([1,2,3,4])
s2=pd.Series([5,6,7,8])

data=dict(apples=s1,orange=s2)
df=pd.DataFrame(data)
dict={'name':['ali','ahmet','ayşe'],'grade':[10,20,30]}
df=pd.DataFrame(dict)
dict_list=[
    {'name':'ahmet','grade':50},
    {'name':'ali','grade':70},
    {'name':'ayse','grade':90}
  ]
df=pd.DataFrame(dict_list)
print(df)