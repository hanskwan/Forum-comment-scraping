#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 12:43:10 2021

@author: Hans
"""

import pandas as pd
import re
import time
from datetime import datetime
import time
import csv

import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

# need to change
# url info
post = "2462646"

###
# Class id
topic_class = "Po8iCa0b9ZUovZ9Ofa_Gk _3UWhC8w0s5w1-V4_sdp4Yd"
post_num_class = "_3SqN3KZ8m8vCsD9FNcxcki " # positoin of the post
comm_class = "_2cNsJna0_hV8tdMj3X6_gJ" # normal comment
encry_comm_class = "_2yeBKooY3VAK8NLhM4Esov" # encry comment
reply_class = "oStuGCWyiP2IrBDndu1cY" # reply comment

###
# Srape Topic of the post
driver.get("https://lihkg.com/thread/" + str(post) + "/page/" + str(1))
time.sleep(1.5)
topic = driver.find_elements_by_xpath('//*[@id="app"]/nav/div[2]/div[1]/span')[0].text
time.sleep(1)
topic

###
# Scrape how many pages for the post
driver.get("https://lihkg.com/thread/" + str(post) + "/page/" + str(1))
time.sleep(1)
page_list = driver.find_elements_by_xpath('//*[ @class = "_1H7LRkyaZfWThykmNIYwpH"]')
time.sleep(1)
page_text = page_list[0].text
last_page_split = page_text.split("\n")
last_page = int(re.search(r'\d+', last_page_split[-1]).group())
last_page

###
# Scrape comm of the post, including normal comment, reply comment and encry comment
comm_list = []
comm_list.append("Topic: " + str(topic))
comm_list.append("Total page: " + str(last_page))


for i in range(last_page+1):
    driver.get("https://lihkg.com/thread/" + str(post) + "/page/" + str(i))
    time.sleep(1)
    comm = driver.find_elements_by_xpath('//*[ @class = "_3SqN3KZ8m8vCsD9FNcxcki" or  @class = "_2cNsJna0_hV8tdMj3X6_gJ" or @class = "_2yeBKooY3VAK8NLhM4Esov" or @class = "oStuGCWyiP2IrBDndu1cY" ]')
    time.sleep(1)
    for j in range(len(comm)):
        comm_list.append(comm[j].text)
comm_list

###


price = []
price.append(comm_list[0])
price.append(comm_list[1])

for i in comm_list:
    if (re.search("[4-6][0-9][0-9]", i)):
        price.append(i)

[i.encode("utf-8") for i in price]
price

pd.DataFrame(price).to_excel("xl.xlsx", header = None)





