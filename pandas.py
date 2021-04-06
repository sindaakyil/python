import pandas as pd
import numpy as np
numbers=[10,20,30,40,50]
letters=['a','b','c','d']
scalar= 5
dict={'a':10,'b':20,'c':30,'d':40}
pandas_series=pd.Series(numbers)
pandas_series=pd.Series(letters)
pandas_series=pd.Series(5,['a','b','c','d'])
pandas_series=pd.Series(numbers,['a','b','c','d','e'])
pandas_series=pd.Series(dict)
result=np.random.randint(10,100,6)
pandas_series=pd.Series(result)
result=pandas_series[0]
pandas_series=pd.Series([10,20,30,40,50],['a','b','c','d','e'])
result=pandas_series[0]
result=pandas_series[:2]
result=pandas_series[-2:]
result=pandas_series[:-1]
result=pandas_series['a']
result=pandas_series[['d','a']]
result=pandas_series.ndim
result=pandas_series.sum()
result=pandas_series.max()
result=pandas_series.min()
result=pandas_series+pandas_series
result=pandas_series+50
result=pandas_series-10
result=np.sqrt(pandas_series)
result=pandas_series>=50
result=pandas_series %2==0
print(result)
opel2018=pd.Series([10,20,30,40],['astra','corsa','insigna','mokka'])
opel2019=pd.Series([40,20,30,10],['astra','corsa','grandland','mokka'])
total=opel2018+opel2019
print(total)


print(pandas_series)