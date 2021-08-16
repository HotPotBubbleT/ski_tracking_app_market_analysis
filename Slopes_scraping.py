#!/usr/bin/env python
# coding: utf-8

# In[13]:


#import package
import pandas as pd
import os


# In[14]:


os.getcwd()


# In[15]:


os.chdir('/Users/johnli/Desktop/Forkia')


# In[16]:


os.getcwd()


# In[31]:


# for scraping app reviews from App Store
from app_store_scraper import AppStore
# for scraping app info from App Store
from itunes_app_scraper.scraper import AppStoreScraper
from pprint import pprint


# In[32]:


## Read in file containing app names and IDs
app_df = pd.read_csv('/Users/johnli/Desktop/Forkia/app_ids.csv')
app_df.head()


# In[33]:


## Get list of app names and app IDs
app_names = list(app_df['iOS_app_name'])
app_ids = list(app_df['iOS_app_id'])


# In[34]:



## Set up App Store Scraper
scraper = AppStoreScraper()
app_store_list = list(scraper.get_multiple_app_details(app_ids))

## Pretty print the data for the first app
pprint(app_store_list[0])


# In[35]:


app_info_df = pd.DataFrame(app_store_list)
app_info_df.to_csv('/Users/johnli/Desktop/Forkia/app_info.csv', index=False)
app_info_df.head()


# In[37]:


## Instantiate AppStore class for desired app
my_app = AppStore(
  country='us',        # required, 2-letter code
  app_name='slopes-ski-snowboard', # required, found in app's url
  app_id=643351983    # technically not required, found in app's url
) 


# In[42]:


my_app.review()


# In[47]:


reviews = my_app.reviews


# In[57]:


pprint(my_app.reviews)


# In[66]:


print(type(reviews))
review_df = pd.DataFrame(my_app.reviews)
print(review_df)


# In[70]:


review_df.to_csv('slopes-ski-snowboard' + '.csv', index=False)


# In[117]:


# Start with loading all necessary libraries
import numpy as np
import wordcloud
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt


# In[118]:


text = " ".join(review for review in review_df.review)
print ("There are {} words in the combination of all review.".format(len(text)))


# In[119]:


stopwords = set(STOPWORDS)
stopwords.update(["app", "day", "Slopes", "see","use","used","using","good","love","great","awesome","well","amazing","best","s","apps","ski","skiing","run","runs","really"])


# In[126]:


# Generate a word cloud image
wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(text)


# In[127]:


plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


# In[114]:


wordcloud.to_file("/Users/johnli/Desktop/Forkia/Slopes_review.png")

