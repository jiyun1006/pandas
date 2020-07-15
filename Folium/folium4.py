#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import folium
import json

df = pd.read_excel('./경기도인구데이터.xlsx', index_col = '구분')
df.columns = df.columns.map(str)

geo_path = './경기도행정구역경계.json'

try:
    geo_data = json.load(open(geo_path, encoding = 'utf-8'))
except:
    geo_data = json.load(open(geo_path, encoding='utf-8-sig'))
    
    
g_map = folium.Map(location=[37.5502,126.982], tiles = 'Stamen Terrain', zoom_start = 9)

year = '2007'


folium.Choropleth(geo_data = geo_data, data=df[year], columns = [df.index, df[year]], fill_color ='YIOrRd', fill_opacity=0.7,
                 line_opacity=0.3, threshold_scale=[10000,100000,300000,500000,700000], key_on = 'feature.properties.name')

