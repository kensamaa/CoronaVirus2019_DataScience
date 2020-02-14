# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 04:47:08 2020

@author: amine ab
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#main site where i got the data
#https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset
#for reference
#https://towardsdatascience.com/a-data-scientists-perspective-on-the-wuhan-coronavirus-4d1110446478


def number_of_confirmed_cases_over_time(data):
    #plotting a bar chart of confirmed cases over time
    sns.axes_style("whitegrid")
    sns.barplot(
            x="Date_date", 
            y="Confirmed", data=data.groupby(['Date_date']).sum().reset_index(drop=None)
            )
    plt.xticks(rotation=60)
    plt.ylabel('Number of confirmed cases',fontsize=15)
    plt.xlabel('Dates',fontsize=15)
    
def Rate_of_death_vs_rate_of_recovery(data):
    #plotting two line plots for deaths and recoveries respectively
    plt.plot('Date_date', 'Deaths', data=data.groupby(['Date_date']).sum().reset_index(drop=None), color='red')
    plt.plot('Date_date', 'Recovered', data=data.groupby(['Date_date']).sum().reset_index(drop=None), color='green')
    plt.xticks(rotation=60)
    plt.ylabel('Number of cases',fontsize=15)
    plt.xlabel('Dates',fontsize=15)
    plt.legend()
    plt.show()
    #               10 most affected countries, besides China

def ten_most_affected_countries_besides_China(df_country):   
    #We know that China is the most affected country by a large margin, #so lets create a bar plot to compare countries other than China
    #increasing the figure size
    plt.rcParams['figure.figsize']=(15,7)
    sns.barplot(
            x="Country",
            y="Confirmed",
            data=df_country[df_country.Country!='China'].nlargest(10,'Confirmed'),
            palette=sns.cubehelix_palette(15, reverse=True)
            )
    plt.ylabel('Number of cases',fontsize=15)
    plt.xlabel('Countries',fontsize=15)
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)


def A_closer_look_at_the_10_most_affected_provinces_in_China(data):
    
    #creating a separate dataframe for provinces
    df_province=data[data['Country']=='China'].groupby(['Province/State']).max().reset_index(drop=None)
    #selecting 10 most affected provinces
    df_province=df_province.nlargest(10,'Confirmed')
    df_province=df_province[['Province/State','Deaths','Recovered']]
    #for multi-bar plots in seaborn, we need to melt the dataframe so #that the the deaths and recovered values are in the same column
    df_province= df_province.melt(id_vars=['Province/State'])

    sns.barplot(
            x='Province/State', 
            y='value', 
            hue='variable', 
            data=df_province
            )
    plt.xlabel('Provinces',fontsize=15)
    plt.ylabel('Number of cases',fontsize=15)





#reading the data from the csv
data= pd.read_csv("data/2019_nCoV_data.csv")

#checking the number of rows and columns
check_nbr_row_colmn=data.shape

#dropping the 1st and 5th column
data.drop("Sno", axis=1, inplace=True)
data.drop("Last Update", axis=1, inplace=True)

#getting a summary of the columns
description=data.describe()
print(description)

#checking for duplicate rows
duplicate_rows=data.duplicated(['Country','Province/State','Date'])
data[duplicate_rows]

#listing all the countries where the virus has spread to
country_list=list(data['Country'].unique())
print(country_list)
print(len(country_list))

#merging China and Mainland China
data.loc[data['Country']=='Mainland China','Country']='China'

dates=list(data['Date'].unique())
print(dates)
print(len(list(data['Date'].unique())))

#converting 'Date' column to datetime object
data['Date'] = pd.to_datetime(data['Date'])
#extracting dates from timestamps
data['Date_date']=data['Date'].apply(lambda x:x.date())


'''
Since the data is cumulative, 
we need to use the max() function with groupby() 
in order to get the maximum number of reported cases for each country.
 If we use sum(), we will be double counting.
'''

#getting the total number of confirmed cases for each country
df_country=data.groupby(['Country']).max().reset_index(drop=None)
#print(df_country[['Country','Confirmed','Deaths','Recovered']])

#preparing data for a time-series analysis
df_by_date=data.groupby(['Date_date']).sum().reset_index(drop=None)
df_by_date['daily_cases']=df_by_date.Confirmed.diff()
df_by_date['daily_deaths']=df_by_date.Deaths.diff()
df_by_date['daily_recoveries']=df_by_date.Recovered.diff()
#print(df_by_date)


#number_of_confirmed_cases_over_time(data)
#Rate_of_death_vs_rate_of_recovery(data)
#ten_most_affected_countries_besides_China(df_country)
A_closer_look_at_the_10_most_affected_provinces_in_China(data)



