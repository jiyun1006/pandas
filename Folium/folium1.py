#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import folium

seoul_map = folium.Map(location = [37.55,126.98], zoom_start=12)

seoul_map.save('./seoul.html')

