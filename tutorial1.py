#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup as bs 

url = "https://www.youtube.com/user/chuchushoeTW"
response = urllib.request.urlopen(url) #開連結 
html_cont = response.read() 
soup = bs(html_cont,'html.parser',from_encoding='UTF-8') #結構化 
'''
results = soup.find_all("www.youtube.com\/yt\/")
for line in results:
'''
print(soup.link)