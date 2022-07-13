#!/usr/bin/env python
# coding: utf-8

# In[165]:


import pandas as pd
import csv
from csv import reader


# In[166]:


#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)


# # 1. budget_data:
# 1. Read and Manipulate Data
# 

# In[167]:


path = "C:\\Users\\eszczepalink\\Downloads\\Starter_Code (2)\\Starter_Code\\PyBank\\Resources\\budget_data.csv"


# In[168]:


budget_data = pd.read_csv(path)
budget_data.head()


# # 2. make a copy of original Dataframe

# In[169]:


DF_b = budget_data.copy()


# In[170]:


DF_b_d = DF_b.set_index("Date")
DF_b_d.tail()


# In[171]:


DF_b_d.dtypes


# # Calculations

# In[172]:


#   Total Months: 86
Total_Months = len(DF_b_d)
Total_Months


# In[173]:


#   Total: $38382578
Total = DF_b_d["Profit/Losses"].sum()
Total 


# In[252]:


# Create an empy lists to store data in them  
Total_Months = []
Total = []


# In[254]:


# open csv file, eliminate headers than loop through entire rows and store into list each items needed 
with open(path,'r') as file:
    reader = csv.reader(file)
    headers = next(reader)
    for row in reader:
        Total_Months.append(row[0])
        Total.append(int(row[1]))
        #print(row[0])
        #print(row[1]
   


# In[255]:


# Loop Through Profits/Losses list 
totalProf= 0
for j in Total:
    totalProf = j + totalProf
print(totalProf)
  


# In[256]:


#   Average  Change: $-2315.12
# row (next row - current row) ---


# In[257]:


len(Total)


# In[259]:


# profits/Losses change
# using list comprehention to create a new list
ProfLossChange = [Total[i+1] - Total[i] for i in range(0,len(Total)-1)]


# In[260]:


print(ProfLossChange)


# In[241]:


len(ProfLossChange)


# In[284]:


# average change
average_change = sum(ProfLossChange)/len(ProfLossChange)
average_change
    
    


# In[244]:


#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)


# In[277]:


max(ProfLossChange)


# In[278]:


min(ProfLossChange)

