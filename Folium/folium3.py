#!/usr/bin/env python
# coding: utf-8

# In[1]:


import folium
import pandas as pd

df = pd.read_excel('./서울지역 대학교 위치.xlsx')

seoul_map = folium.Map(location=[37.55,126.98], tiles='Stamen Terrain', zoom_start=12)


for name, lat, lng in zip(df.index, df.위도, df.경도):
    folium.Marker([lat,lng], popup=name).add_to(seoul_map)
    
seoul_map.save('./sesoul_colleges.html')

