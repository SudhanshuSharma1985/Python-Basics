# -*- coding: utf-8 -*-
"""
Created on Wed Feb 14 12:13:43 2018

@author: arunansu.gorai
"""

#Additional resources: https://www.youtube.com/watch?v=HBxCHonP6Ro&list=PL6gx4Cwl9DGAcbMi1sH6oAMk4JHw91mC_

1. Data undersatnding

Dimension of the data=(rows,columns)=(observations,variables)
Type of variables=(categorical, numeric, datetime)
Variable description=(Unique values,Non-Missing values,Frequency of categorical vars, Mean, median,mode,sd, quantiles(univariate) of 
                      numerical vars, Min-Max of time date vars)

Python is case sensitive
2. Data Import

#reading a csv file
import pandas as pd
import os

os.chdir(r"C:\Sudhanshu\Training_17May\Day1\Day1")

class_csv = pd.read_csv(r"class.csv")

#reading an excel file
class_xl = pd.read_excel(r"C:\Sudhanshu\Training_17May\Day1\Day1\class.xlsx")


#reading a sas file
class_sas = pd.read_sas(r"class.sas7bdat", format='SAS7BDAT')

#Automatic creation of index

3. Libraries
import numpy as np
import pandas as pd
from scipy.stats import mode
from scipy.stats import mode as md




4. Commenting a line; CTRL+1 and CTRL+4
5. Running a code: F9 for a single line, For multiple lines CTRL+Enter or F9 after selecting all the relevant lines

6. Data export

class_csv.to_csv(r"class.csv")


7. basic printing
print('we are indians')


8. Data Types - str, int, float
type("Ahfjk")
type(1)
type(1.0)

9. String Joining

7+8

#valid
'a'+'b'

2*'a'

#invalid

'a'-'b'

'a'/'b'

10. upper and lower

s1 = "StrinG"
print(s1.upper())

print(s1[0])
print(s1[2:4])

s2 = s1.lower()
print(s2)

# =============================================================================
# Level 2
# =============================================================================

11. 2. List: concept of 0

list1 = ['a','b','c','c','c']
list2 = ['x','y']
list1.extend(list2)
list1[5]



list[0] #will get the first item 'a'
list[1]

list.append('d') #will add 'd' to the list
list
12. Reading a data Again - Automatic conversion to dataframe
#import pandas as pd
class_csv = pd.read_csv(r"class.csv")

13. Creating a data in python:Manual conversion in dataframe

raw_data = {'first_name': ['Mr. Jason', 'Jason', 'Mr. Jason', 'Tina', 'Mr. Jake', 'Jake'],
        'last_name': ['Miller', 'Miller', 'Statham', 'Ali', 'Milner', np.nan],
        'age': [42, 42, 36,73, np.NaN,np.NaN],
        'age_group': ['42-47', '42-47', '36-41', '24-29', '73-78', '78-81'],
        'gender':['M','F','F','F','M','F'],
        'preTestScore': [4, 4, 31, 2, 3, 4],
        'postTestScore': ['a 25','b 25','25','hdh 62',' 70','hs 238999'],
        'location': ['S','S','S','M','M','S']}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age','age_group','gender', 'preTestScore', 'postTestScore','location'])


#alternatively

raw_data = pd.DataFrame({'first_name': ['Mr. Jason', 'Jason', 'Mr. Jason', 'Tina', 'Mr. Jake', 'Jake'],
        'last_name': ['Miller', 'Miller', 'Statham', 'Ali', 'Milner', np.nan],
        'age': [42, 42, 36,73, np.NaN,np.NaN],
        'age_group': ['42-47', '42-47', '36-41', '24-29', '73-78', '78-81'],
        'gender':['M','F','F','F','M','F'],
        'preTestScore': [4, 4, 31, 2, 3, 4],
        'postTestScore': ['a 25','b 25','25','hdh 62',' 70','hs 238999'],
        'location': ['S','S','S','M','M','S']})

14. Cocept of missing value

np.nan

15. Knowing the data:
    
df.info()
df.describe()
df.gender.describe()
df.describe(include='all')

df.head()
df.head(2)
df.tail()

df.location.unique()
set(df.location.unique())

df.mean()
df.sum()

16. Missing values:
    
df.isnull().sum()

17. rename:
    
df=df.rename(columns={'gender':'Gender','location':'Location'})
df.info()

18. Frequency

#checking frequency
df.age.value_counts() #sorted by freq, by default
df.Location.value_counts() 

df.age.value_counts().sort_index() # sorted by index
df.age.value_counts(dropna=False) # including missing values

19. Remove Duplicates:
    
raw_data={'id':[1,2,2,3,3,3,4,4,4,4],'value':['A','B','C','D','E','F','G','H','I','J']}
df=pd.DataFrame(raw_data,columns=['id','value'])

df.drop_duplicates(subset=['id'],keep='first',inplace=False)
df.drop_duplicates(subset=['id'],keep='last',inplace=False)
df.drop_duplicates(subset=['id'],keep=False,inplace=False)

20. Drop a column:
del df['value']
df.info()

# =============================================================================
# Level 3
# =============================================================================

21. Creating new variables

raw_data = {'first_name': ['Jason', 'Jason', 'Jason', 'Tina', 'Jake', 'Jake'],
        'last_name': ['Miller', 'Miller', 'Statham', 'Ali', 'Miller', 'Cooze'],
        'age': [42, 42, 36, 24, 73, 78],
        'preTestScore': [4, 4, 31, 2, 3, 4],
        'postTestScore': [25, 25, 25, 62, 70, 23]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])

raw_data0 = {'first_name': ['Jason', 'Jason', 'Jason', 'Tina', 'Jake', 'Jake'],
        'last_name': ['Miller', 'Miller', 'Statham', 'Ali', 'Miller', 'Cooze']}
df0 = pd.DataFrame(raw_data0, columns = ['first_name', 'last_name'])


df['sum_score']=df['preTestScore']+df['postTestScore']

22. creating new variable using else condition

df['score_grp']=["<50" if x < 50 else 
                 ">=50"
                 for x in df['sum_score']]
 

df['last_name_miller']=['Miller' if x=='Miller' else 
                        'Others'  
                      for x in df['last_name']]

23. creating new variable using else if condition
df['score_grp']=["<50" if x < 50 else 
                 "50 - 60" if  50<= x <60  else 
                 "60 - 70" if  60<= x <70  else
                 ">=70"
                for x in df['sum_score']]

24. #To keep specific rows based on a condition
df1 = df[(df['preTestScore']>2) & ((df['postTestScore']<70))]

25. #To drop specific rows based on a condition
df1=df.drop(df[(df['postTestScore']<50)].index)

26. concatenation of two datasets
concat = pd.concat([df,df0])

27. merging

raw_data = {'id': ['1', '2', '2', '3', '4', '5'],
        'name1': ['a', 'b', 'c', 'f','y','r']}
df = pd.DataFrame(raw_data, columns = ['id', 'name1'])

raw_data0 = {'id': ['1', '2', '3', '8'],
        'name0': ['x', 'y', 'x', 'o']}
df0 = pd.DataFrame(raw_data0, columns = ['id', 'name0'])

df_merged=pd.merge(df,df0,on='id',how='inner') 
df_merged=pd.merge(df,df0,on='id',how='left') 


28. Merging with different valriable names and keeping a specific set of variables

raw_data = {'id': ['1', '2', '2', '3', '4', '5'],
        'name1': ['a', 'b', 'c', 'f','y','r']}
df = pd.DataFrame(raw_data, columns = ['id', 'name1'])

raw_data0 = {'id0': ['1', '2', '3', '8'],
        'name0': ['x', 'y', 'x', 'o']}
df0 = pd.DataFrame(raw_data0, columns = ['id0', 'name0'])


newdata=pd.merge(df,df0[['id0']],left_on='id',right_on='id0',how='inner')


29. Datetime events
#"Date_time_of_event" column and it is currently read as an object. This will restrict us to perform any date time operation on it. 
#Which command will help to convert the column "Date_time_of_event" to data type "datetime"?

raw_data = {'Date_time_of_event': ['25-08-2012 00:00', '24-08-2012 02:00', '25-08-2012 04:00'],
            'Count': [8,2,3]}
df = pd.DataFrame(raw_data, columns = ['Date_time_of_event', 'Count'])
df.info()

df['Date_time_of_event'] = pd.to_datetime(df.Date_time_of_event, format="%d-%m-%Y %H:%M") 
df.info()

30. Extracting specific info from a datetime column
#How would you you extract only the dates from the given "Date_time_of_event" column?
df.Date_time_of_event.dt.day

#name of weekday the date belongs to
df.Date_time_of_event.dt.weekday_name

#no of the week the date belongs to
df.Date_time_of_event.dt.weekday
