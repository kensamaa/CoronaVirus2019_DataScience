# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 20:29:42 2020

@author: USER
"""
from datetime import datetime

class country:

    def __init__(self):
        print("initialse object")
        self.date=0
        self.name=0
        self.TtCase=0
        self.newCase=0
        self.TtDeath=0
        self.NewDeath=0
        self.TtRecovered=0
        self.ActiveCase=0
        self.SeriousCritical=0
        
    def setdata(self,lst):
        #obj=country(str(date),str(lst[0]),str(lst[1]),str(lst[2]),str(lst[3]),str(lst[4]),str(lst[5]),str(lst[6]).str(lst[7]))
        print("setting the data")
        self.date=str(datetime.now().strftime("%d/%m/%Y"))
        self.name=lst[0]
        self.TtCase=lst[1]
        self.newCase=lst[2]
        self.TtDeath=lst[3]
        self.NewDeath=lst[4]
        self.TtRecovered=lst[5]
        self.ActiveCase=lst[6]
        self.SeriousCritical=lst[7]
        
    def print(self):
        print("date :"+self.date)
        print("name :"+self.name)
        print("total cases :"+self.TtCase)
        print("new cases :"+self.newCase)
        print("total death :"+self.TtDeath)
        print("new death :"+self.NewDeath)
        print("total recovered :"+self.TtRecovered)
        print("active cases :"+self.ActiveCase)
        print("serious critical :"+self.SeriousCritical)
        
    def class_to_array(self):
        print("class to array")
        lst=[]
        lst.append(self.date)
        lst.append(self.name)
        lst.append(self.TtCase)
        lst.append(self.newCase)
        lst.append(self.TtDeath)
        lst.append(self.NewDeath)
        lst.append(self.TtRecovered)
        lst.append(self.ActiveCase)
        lst.append(self.SeriousCritical)
        return lst
       

''' def __init__(self,date,name,TtCase,newCase,TtDeath,NewDeath,TtRecovered,ActiveCase,SeriousCritical):
        self.date=date
        self.name=name
        self.TtCase=TtCase
        self.newCase=newCase
        self.TtDeath=TtDeath
        self.NewDeath=NewDeath
        self.TtRecovered=TtRecovered
        self.ActiveCase=ActiveCase
        self.SeriousCritical=SeriousCritical'''