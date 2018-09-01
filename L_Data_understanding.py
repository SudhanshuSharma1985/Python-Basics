

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from openpyxl import load_workbook

#==============================================================================
# Importing file as pandas dataframe
#==============================================================================
#input_file_path="C:\LearningPython\Learning\Learning\\"
#output_file_path="C:\LearningPython\Learning\Learning\\"
#input_file_name="model_data_to_share.xlsx"

input_file_path=r"C:\Users\Desktop\All Training Code\\"
output_file_path=r"C:\User\Desktop\All Training Code\\"
input_file_name="L_joiner_data_um_1.xlsx"
in_f=input_file_path+input_file_name
#Reading csv data file
df=pd.read_excel(in_f,sheetname='Sheet1')
#==============================================================================
# Apart from this many other option are available and can be used based on data need
# pd.read_excel
# pd.read_sas
# pd.read_sql
#==============================================================================



#==============================================================================
# Check for imported data
#==============================================================================
df 
#Check the head and tail of the data and validate it with raw data
df.head()
df.tail(3)

#To check start and end of record numbers
df.index 
len(df.index)

# To check number of row and columns
df.shape

#To check data types of all variables
dt=df.dtypes

dt
#To get summary like min max mean etc for all numeric variables 
df.describe()
df.describe().transpose()


#df['Profile Creation Date'] = pd.to_datetime(df['Profile Creation Date'],infer_datetime_format=True)
#df['Application date'] = pd.to_datetime(df['Application date'],infer_datetime_format=True)
#df['Offer Extend Date'] =pd.to_datetime(df['Offer Extend Date'],infer_datetime_format=True)
#df['Offer Accepted Date'] = pd.to_datetime(df['Offer Accepted Date'],infer_datetime_format=True)
#df['Status Change Date'] = pd.to_datetime(df['Status Change Date'],infer_datetime_format=True)
#df['Last Action Date'] = pd.to_datetime(df['Last Action Date'],infer_datetime_format=True)
#df['Candidate Start Date'] = pd.to_datetime(df['Candidate Start Date'],infer_datetime_format=True)
df['DOJ'] = pd.to_datetime(df['DOJ'],infer_datetime_format=True)
#df['Profile_Last_Promotion_Date'] = pd.to_datetime(df['Profile_Last_Promotion_Date'],infer_datetime_format=True)
df['Date_of_leaving'] = pd.to_datetime(df['Date_of_leaving'],infer_datetime_format=True)


#To check data types of all variables
df.dtypes
df.columns = df.columns.str.replace('(','')
df.columns = df.columns.str.replace(')','')
df.columns = df.columns.str.replace(',','')
df.columns = df.columns.str.replace('/','')
df.columns = df.columns.str.replace('/','')
df.columns = df.columns.str.replace('.','')
df.columns = df.columns.str.replace(' ','_')
df.dtypes
#Data summary for all variables

column_name=list(df.columns.values)
#Deleting the already created object
del list

data_summary=pd.DataFrame(columns=('VariableName','Count','Count_distinct','Count_missing'))
i=0     
for col_i in column_name:
#    Counting distinct value for each variables
#    x=pd.Series.value_counts(df[col_i]).to_frame()
#    distinct_count=x.size
    distinct_count=df[col_i].nunique()
    #    Counting missing value for each variables
    missing_count=df[col_i].isnull().sum()
    data_summary.loc[i]=[col_i,len(df.index),distinct_count,missing_count]
    i=i+1
#End of the loop
result=data_summary.sort_values('Count_missing',ascending=False)
#Exporting summary to excel
out_file=output_file_path+'data_summary_dm_Referrer.xlsx'
result.to_excel(out_file,sheet_name='Data_summary')


#Creating data understanding for numeric variables
numeric=df.describe()
#df.describe(percentiles=[.05,.1,.2,.25,.5,.75,.9,.95,1])
#df.describe(include='all')

#Transposing output to get desired results
num_T=numeric.T
num_T.index.name='VariableName'
#Exporting numeric variable details to excel
out_file=output_file_path+'numeric_dm_Referrer.xlsx'
num_T.to_excel(out_file,sheet_name='numeric_summary')


#Creating data understanding for character variables

#Selecting only string data type variables
char_var_list=list(df.select_dtypes(include=['O']).columns)
#Creating excel file to add multiple sheets

out_file=output_file_path+'char_dm_Referrer.xlsx'
writer = pd.ExcelWriter(out_file, engine='openpyxl')
for col_i in char_var_list:
    char=pd.Series.value_counts(df[col_i],dropna=False).to_frame()
    char.index.name=col_i
    char.columns=['count']
#Since excel sheet name have limit of 31 character so truncating the variable name
    if len(col_i)>31:
        sheet_name=col_i[:31]
    else:
        sheet_name=col_i
    char.to_excel(writer,sheet_name=sheet_name)
        
writer.save()   

#End of character data understanding output


#Data understanding for all date variables

date_var_list=list(df.select_dtypes(include=['datetime64']).columns)

date_summary=pd.DataFrame(columns=('VariableName','Min_date','Max_date'))
i=0     
for col_i in date_var_list:
    min_date=df[col_i].min()
    max_date=df[col_i].max()
    date_summary.loc[i]=[col_i,min_date,max_date]
    i=i+1
#Exporting date variables details
out_file=output_file_path+'date_output_dm_Referrer.xlsx'
date_summary.to_excel(out_file,sheet_name='date_summary') 

#End of data understanding code

  
#==============================================================================
# Reading material references:
# https://www.analyticsvidhya.com/blog/2016/01/guide-data-exploration/
# https://www.kaggle.com/pmarcelino/comprehensive-data-exploration-with-python
#==============================================================================
