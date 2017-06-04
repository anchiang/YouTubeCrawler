#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup as bs 
import locale

locale.setlocale(locale.LC_ALL,'en_US.UTF-8')

url = "https://www.youtube.com/user/chuchushoeTW/about"
response = urllib.request.urlopen(url) #開連結 
html_cont = response.read() 
soup = bs(html_cont,'html.parser',from_encoding='UTF-8') #結構化 

res = soup.find_all(class_="about-stat")
for line in res[0:2]:
    print(line.b)
'''
people = locale.atoi(res[0].find('b').string)
views = locale.atoi(res[1].find('b').string)
print(n, people, views)
'''