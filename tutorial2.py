#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup as bs
import locale
import re

locale.setlocale(locale.LC_ALL,'eng') 

url = "https://www.youtube.com/user/chuchushoeTW/about"
response = urllib.request.urlopen(url) #開連結 
html_cont = response.read() 
soup = bs(html_cont,'html.parser',from_encoding='UTF-8') #結構化 
result = soup.find_all(class_="about-stat")
people = locale.atoi(result[0].b.string)
view = locale.atoi(result[1].b.string)
date = result[2].string
year = re.findall("[0-9]{1,2}月",date)[0]
title = soup.find(class_="spf-link branded-page-header-title-link yt-uix-sessionlink").string
print(title,people,view,year)