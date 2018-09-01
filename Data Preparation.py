
1. Data import

import numpy as np
import pandas as pd

admit = pd.read_excel(r"C:\Sudhanshu\Training_17May\Day1\Day1\admit.xlsx")
admitid=pd.read_excel(r"C:\Sudhanshu\Training_17May\Day1\Day1\admit_visitid.xlsx")

2. data structure
admit.info()
admitid.info()

admit.shape
admit.shape[0]

admit.describe()
admit.head()

3. Checking the dataset is unique or not - then drop the duplicte rows
len(set(admit['ID']))

admit.drop_duplicates(subset=['ID'],keep='first',inplace=True)

len(set(admitid['ID']))

4. Joining the two datasets

admitn=pd.merge(admit,admitid[['ID','total Fees']],left_on='ID',right_on='ID',how='left')

admitn.info()

4. Distributions - categorical variables

admitn['Sex'].value_counts()
admitn['ActLevel'].value_counts()

import seaborn as sns
sns.set(color_codes=True)

5. Barplot

#Univariate
sns.countplot(x="Sex", data=admitn)
sns.countplot(x="ActLevel", data=admitn, palette="Greens_d")

#Reference for seaborn tutorial
#==============================================================================
# https://elitedatascience.com/python-seaborn-tutorial
#==============================================================================

#Bivariate
sns.countplot(x="Sex", hue="ActLevel", data=admitn)

6. Boxplot

#For all numeric variables
sns.boxplot(data=admitn, orient="h", palette="Set2")

#Univariate
sns.boxplot(x=admitn["Age"])
sns.boxplot(x=admitn["Fee"])
sns.boxplot(x=admitn["total Fees"])

#Bivariate
sns.boxplot(x="Age", y="Fee", data=admitn)
sns.boxplot(x="Sex", y="Age", data=admitn)

7. Outlier Treatment - Winsorization or Capping

#capping at 99% percentile
admitn['Age'].quantile(0.99)
#capping at 95% percentile
admitn.Age.quantile(0.95)

admitn['Age_n']=[x if x < admitn.Age.quantile(0.95) else 
                 admitn.Age.quantile(0.95)
                 for x in admitn['Age']]

#capping at 99% percentile
admitn['Age'].quantile(0.01)
#capping at 95% percentile
admitn.Age.quantile(0.05)

admitn['Age_n']=[x if x > admitn.Age.quantile(0.05) else 
                 admitn.Age.quantile(0.05)
                 for x in admitn['Age']]

8. Missing Value treatment

#By mean

admitn['total Fees'] = admitn['total Fees'].fillna(admitn['total Fees'].mean())

#By mode

admitn=pd.merge(admit,admitid[['ID','total Fees']],left_on='ID',right_on='ID',how='left')

from scipy.stats import mode
mode(admitn['total Fees'])
mode(admitn['total Fees']).mode[0]

admitn['total Fees'].fillna(mode(admitn['total Fees']).mode[0], inplace=True)


9. Group by

admitid=pd.read_excel(r"C:\Sudhanshu\Training_17May\Day1\Day1\admit_visitid_ind.xlsx")
admitid.info()

grpd=admitid.groupby(['ID'])[['Ind Fees']].sum()
grpd=admitid.groupby((['ID'])[['Ind Fees']].sum(),as_index='False')
grpd=admitid.groupby(['ID'], as_index=False).agg({"Ind Fees": "sum"})

#Join
admitn=pd.merge(admit,grpd,left_on='ID',right_on='ID',how='left')



def factorial(var):
    if(var == 0 or var ==1):
        return 1
    else:
        return var*factorial(var -1)
    
def factorial1(var):
    i = 1
    for i in range(var):
        fact = fact*(i+1)
        return fact
    








