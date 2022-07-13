#!/usr/bin/env python
# coding: utf-8

# In[29]:


import pandas as pd
import csv
from pathlib import Path
from csv import reader


# # 2.Menu_data
# 1. Part 1:
#   - Read the data
#    

# In[30]:


pwd


# In[31]:


ls


# In[32]:


Path ="C:\\Users\\eszczepalink\\Downloads\\Starter_Code (2)\\Starter_Code\\PyRamen\\Resources\\menu_data.csv"


# In[33]:


menu_data = pd.read_csv("menu_data.csv").head()
menu_data


# In[34]:


pd.read_csv("menu_data.csv").head().dtypes


# In[35]:


pd.read_csv("menu_data.csv").columns


# In[36]:


menu = []
with open(Path, 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)
    for row in reader:
        menu.append(row)
#print(menu_data)


# # 2.Sales_data
# 1. Part 1:
#   - Read the data

# In[5]:


Path ="C:\\Users\\eszczepalink\\Downloads\\Starter_Code (2)\\Starter_Code\\PyRamen\\Resources\\sales_data.csv"


# In[6]:


sales_data = pd.read_csv("sales_data.csv").head()
sales_data


# In[7]:


pd.read_csv("sales_data.csv").head().dtypes


# In[8]:


pd.read_csv("sales_data.csv").columns


# In[9]:


sales = []
with open(Path, 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)
    for row in reader:
        sales.append(row)
#print(sales_data)


# # 2. Manipulate the Data
# 

# In[10]:


report = {"01-count":"the total quality for each ramen type",
          "02-revenue": "the total revenue for each ramen type",
          "03-cogs":"the total cost of goods sold for each ramen type",
          "04-profit": "the total profit for each ramen type"}


# In[12]:


# looping through every row in sales list object
Quantity = []
Menu_Item = []
for row in sales:
    Quantity.append(row)
    Menu_Item.append(row)
print(Quantity )   


# In[24]:


# check if sales_item including in report
report.items()


# In[25]:


sales_data


# In[ ]:


sales_item = {"01-count":"the total quality for each ramen type"}


# In[28]:



               new_report = {"sales_item":{"01-count":"the total quality for each ramen type",
          "02-revenue": "the total revenue for each ramen type",
          "03-cogs":"the total cost of goods sold for each ramen type",
          "04-profit": "the total profit for each ramen type"},
                "values":{
                        "01-count": 0,
                         "02-revenue": 0,
                         "03-cogs": 0,
                         "04-profit": 0,
                    
                }}


# In[ ]:


# looping through  row menu 


# In[38]:


menu = []
for row in menu:
    Item.append(row)
    Price.append(row)
    Cost.appent(row)
    

