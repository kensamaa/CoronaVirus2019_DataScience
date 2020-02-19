# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 04:47:08 2020

@author: amine ab
"""
#https://python-forum.io/Thread-Click-a-button-to-get-next-page

#package for webscraping
#import selenium
# inspiration from https://github.com/aj-4/ig-followers/blob/master/main.py
from selenium import webdriver
from time import sleep
class instabot:
    def __init__(self,name):
        self.target_username=name
        self.website="https://www.instagram.com"
        self.website=self.website+"/"+name+"/"
        self.driver= webdriver.Chrome('data/chromedriver.exe')
        self.driver.get(self.website)
        sleep(2)

class FacebookBot:
    def __init__(self,email,password):
        self.email=email
        self.password=password
        self.nbr_friends=0
        self.website="https://www.facebook.com/"
        self.driver= webdriver.Chrome('data/chromedriver.exe')
        self.driver.get(self.website)
        sleep(2)
        self.connection()
        sleep(5)
        self.nbr_friends()
        sleep(5)
        self.get_names()
    def connection(self):
        try:
            self.driver.find_element_by_xpath("//input[@name=\"email\"]")\
                .send_keys(self.email)
            self.driver.find_element_by_xpath("//input[@name=\"pass\"]")\
                .send_keys(self.password)
            self.driver.find_element_by_xpath('//input[@aria-label="Se connecter"]')\
                .click()
            sleep(4)
        except:
            print("smtg wrong in the connection")
        
    def get_number_friends(self):
        self.driver.find_element_by_xpath("//a[contains(@title=\"profile\"]".format(self.username))\
            .click()
        sleep(2)
        self.nbr_friends=self.driver.find_element_by_xpath("//span[contains(@class=\"_gs6\"]")
        print(self.nbr_friends)
        
    def get_names(self):
        try:
            self.driver.find_element_by_xpath("//a[contains(@data-tab-key=\"friends\"]")\
                .click()
            sleep(2)
             
            sleep(2)
            scroll_box=self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div[3]/div/div/div[2]/div/ul[1]")
           
            last_ht=1
            ht=0
        
            while last_ht != ht:
                last_ht = ht
                sleep(1)
                ht = self.driver.execute_script("""
                    arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                    return arguments[0].scrollHeight;
                    """, scroll_box)
            self.driver.executeScript("window.scrollBy(0,1000)")
            links = scroll_box.find_elements_by_tag_name('a')
            names = [name.text for name in links if name.text != '']
               
            return names
        except:
            print("problem  in get names")
        
        
"""
browser = webdriver.Chrome('data/chromedriver.exe')
website="https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset"
browser.get(website)
sleep(1)
xpath='//*[@id="downloadFile-dataExplorerPreview"]'
fullxpath='/html/body/main/div/div[2]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[2]/div/div[6]/span/a'
elem=browser.find_element_by_xpath(xpath)
elem.click()
"""
email=str(input("enter email"))

pwd=str(input("enter password"))

FacebookBot(email,pwd)





















