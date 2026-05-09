#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import requests
from datetime import datetime , timedelta

#read file

df=pd.read_excel("C:/Users/hp/Documents/Timetable automate.xlsx")

#valid rows

valid_days=["Monday","Tuesday","Wednesday","Thrusday","Friday"]

df= df[df["Day"].isin(valid_days)]

#column positions

column_positions = [1,2,3,4,5,6]

#Get tomorrow

tomorrow_date = datetime.now() + timedelta(days=1)

tomorrow_day = tomorrow_date.strftime("%A")

#Tomorrow row

tomorrow_row= df[df["Day"]==tomorrow_day]

#classes

classes = []
if len(tomorrow_row)>0:
    row_data = tomorrow_row.iloc[0]

    for pos in column_positions:
        cell = row_data.iloc[pos]

        if pd.notna(cell) and str(cell).strip()!="":
            classes.append(str(cell))


#message
if classes:
    message = f" Classes for tomorrow ( {tomorrow_day} ) :\n\n"

    for cls in classes:
        message += f"* {cls}\n"

else:

    message =f" No classes tomorrow ( {tomorrow_day} )! Enjoy"

print (message)


#ntfy

topic = "Automate_Timetable"
requests.post(f"https://ntfy.sh/{topic}",data = message.encode('utf-8'))



# In[ ]:





# In[ ]:





# In[ ]:




