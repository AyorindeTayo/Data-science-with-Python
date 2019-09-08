
# coding: utf-8

# In[ ]:


# imort pandas library
import pandas as pd
pandas.read_csv()


# In[ ]:


# Import pandas library
import pandas as pd

# Read the online file by the URLprovides above, and assign it to variable "df"
other_path = "https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DA0101EN/auto.csv"
df = pd.read_csv(other_path, header=None)


# In[12]:


# show the first 5 rows using dataframe.head() method
print("The first 5 rows of the dataframe")
df.head(5)


# In[ ]:


print("The last 10 rows of the dataframe\n")
df.trail(10)
      


# In[15]:


# create headers list 
headers = ["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors","body-style","drive-wheels","engine-location","wheel-base","length","width","height","curb-weight","engine-type","num-of-cylinders","engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm","city-mpg","high-mpg","price"]
print("headers\n",headers)


# In[14]:


df.columns = headers
df.head(10)


# In[16]:


df.dropna(subset=["price"], axis=0)


# In[33]:


print(df.columns)

