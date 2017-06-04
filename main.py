#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup as bs
import locale

youtubes = open('youtubes.csv')
output = open('output.csv','w')
locale.setlocale(locale.LC_ALL,'en_US.UTF-8')
output.write("n, title, url, people, views\n")
    
n = 0
for line in youtubes:
    url = line.rstrip('\n') + "/about"
    print(url)
    n += 1
    response = urllib.request.urlopen(url)
    html_cont = response.read()
    soup = bs(html_cont,'html.parser',from_encoding='UTF-8')
    res = soup.find_all(class_="about-stat")
    people = locale.atoi(res[0].find('b').string)
    views = locale.atoi(res[1].find('b').string)
    title = soup.find(class_="spf-link branded-page-header-title-link yt-uix-sessionlink").string
    output.write("%d, %s, %s, %d, %d \n" % (n, title, url, people, views))
    
youtubes.close()
output.close()