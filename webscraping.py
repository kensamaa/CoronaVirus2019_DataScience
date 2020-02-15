# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 04:47:08 2020

@author: amine ab
"""
#https://python-forum.io/Thread-Click-a-button-to-get-next-page

#package for webscraping
#import selenium
from selenium import webdriver
import time

browser = webdriver.Chrome('data/chromedriver.exe')
website="https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset"
browser.get(website)
time.sleep(1)
xpath='//*[@id="downloadFile-dataExplorerPreview"]'
fullxpath='/html/body/main/div/div[2]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/div/div[6]/span/a'
elem=browser.find_element_by_xpath(xpath)
elem.click()