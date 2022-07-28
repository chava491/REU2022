#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 01:53:36 2022

Author: salvadorguel
Mentor: Dr. Anthony Parolari
Date: Summer 2022
Universtiy: Marquette University
Project: Summer Research Experience for Undergraduates (REU). Focusing on Hardware, Embedded Software, and Analytics for Environment Quality Monitoring
Description: This script is what contains the functions that are mostly used to obtain longitude of sites and latitudes, as well as the 2D gradient functionality.
"""
import requests                    #
import os                          #
import folium                      # Must run this command in the terminal 'python -m pip install folium'
import statistics                  #
import Paths                       #

import HFuncs as HELPER_FUNC       # Imports all of the functions I defined in HFuncs
import numpy as npy                #
import matplotlib.pyplot as pt     #

from folium.plugins import HeatMap # Must run this command in the terminal 'python -m pip install folium'
from datetime import datetime      #

SITE_INFO_PATH = '/Volumes/SeagateBackupPlusDrive/reuriverdata/lists/SiteInfoFinal.txt'         #
DATA_INFO_PATH = '/Volumes/SeagateBackupPlusDrive/reuriverdata/data/'                           #
SAVE_LOCATION_LATITUDE = '/Volumes/SeagateBackupPlusDrive/reuriverdata/temp/templatitude.txt'   #
SAVE_LOCATION_LONGITUDE = '/Volumes/SeagateBackupPlusDrive/reuriverdata/temp/templongitude.txt' #
REU_DATA_PATH = '/Volumes/SeagateBackupPlusDrive/reuriverdata/data/'                            #


def obtainlatitude(siteno):
    urla = 'https://waterdata.usgs.gov/nwis/uv?referred_module=qw&search_site_no='
                                                                       # sitno goes here (aka when URL is put together)
    urlb = '&search_site_no_match_type=exact&index_pmcode_00010=1&index_pmcode_91110=1&index_pmcode_91111=1&group_key=NONE&format=sitefile_output&sitefile_output_format=rdb&column_name=agency_cd&column_name=dec_lat_va&column_name=dec_long_va&range_selection=days&period=7&rdb_compression=file&list_of_search_criteria=search_site_no%2Crealtime_parameter_selection'
    URL = urla + siteno + urlb                                         #
    response = requests.get(URL)                                       # Getting content from the URL we are currently on.
    if (HELPER_FUNC.CheckRequest(response.status_code) == "Success"):  # Here we check that the URL was indeed valid and we got something back.)
        with open(SAVE_LOCATION_LATITUDE, 'wb') as f:                  #
               f.write(response.content)                               #
        with open(SAVE_LOCATION_LATITUDE, "r") as temp:                #
            lines = temp.readlines()                                   #
            for l in lines[0:]:                                        #
                if (l.startswith('USGS')):                             #
                    latitude = l.split()[1]                            #
    return latitude
            
def obtainlongitude(siteno):
    urla = 'https://waterdata.usgs.gov/nwis/uv?referred_module=qw&search_site_no='
    # sitno goes here (aka when URL is put together)
    urlb = '&search_site_no_match_type=exact&index_pmcode_00010=1&index_pmcode_91110=1&index_pmcode_91111=1&group_key=NONE&format=sitefile_output&sitefile_output_format=rdb&column_name=agency_cd&column_name=dec_lat_va&column_name=dec_long_va&range_selection=days&period=7&rdb_compression=file&list_of_search_criteria=search_site_no%2Crealtime_parameter_selection'
    URL = urla + siteno + urlb                                        #
    response = requests.get(URL)                                      # Getting content from the URL we are currently on.
    if (HELPER_FUNC.CheckRequest(response.status_code) == "Success"): # Here we check that the URL was indeed valid and we got something back.)
        with open(SAVE_LOCATION_LONGITUDE, 'wb') as f:                #
            f.write(response.content)                                 #
        with open(SAVE_LOCATION_LONGITUDE, "r") as temp:              #
            lines = temp.readlines()                                  #
            for l in lines[0:]:                                       #
                if (l.startswith('USGS')):                            #
                    longitude = l.split('\t')[2]                      # This is saying (from left to right) we are getting the item in the 3rd column of the current line     
    return longitude                                                  #

def findmax(array):
    maximum = 0
    for i in range(0, len(array)):
        if (array[i] > maximum):
            maximum = array[i]
    return maximum

def findmin(array):
    minimum = array[0]
    for i in range(0, len(array)):
        if (array[i] < minimum):
            minimum = array[i]
    return minimum

def graphlengthsoftimeseries(begindates, enddates):
    no_days = []
    x = []
    x.append(0)
    for i in range(1, len(begindates)):
        x.append((x[i-1]+1))
    
    if ((len(begindates)) == (len(enddates))):
        for i in range(0,len(begindates)):
            bd = datetime.strptime(begindates[i], "%Y-%m-%d") #YEAR/MONTH/DAY
            ed = datetime.strptime(enddates[i], "%Y-%m-%d") #YEAR/MONTH/DAY
            no_days.append((ed - bd).days)
    pt.title("Time Series Lengths For Each Site")
    pt.scatter(x, no_days, s = 1, color = "red")
    pt.grid()
    pt.xlabel('Site Number Index In Relation To The SITE_NO Array')
    pt.ylabel('Total Number Of Days From Begin To End Date')
    pt.savefig("/Volumes/SeagateBackupPlusDrive/reuriverdata/Graphs/TimeSeriesLengthsGraph", dpi=1200)
    pt.show()
    print("---------------------------")
    print("Smallest Number Of Days => ", findmin(no_days))
    print("Largest Number Of Days  => ", findmax(no_days))
    print("--------------------------- \n")
    return no_days

def graphlengthsofgroupedtimeseries(begindates, enddates, period):
    no_days = []        # This array will contain the difference between the begin and start dates of each site
    x_axis = []         # This array will contain the (#, #) range of how many days a site has
    y_axis = []         # This array will contain the no_sites with their no_days being inside of the 
    if ((len(begindates)) == (len(enddates))):
        for i in range(0,len(begindates)):
            bd = datetime.strptime(begindates[i], "%Y-%m-%d") #YEAR/MONTH/DAY
            ed = datetime.strptime(enddates[i], "%Y-%m-%d") #YEAR/MONTH/DAY
            no_days.append((ed - bd).days)
    maximumpoint = findmax(no_days)
    minimumpoint = findmin(no_days)
    
    
    rangemax = maximumpoint + (period - (maximumpoint%period))  # Want a nice maximum point that coincides with the wanted period
                                                                     # So if max point is 98 and our period is 10 the following will occur
                                                                     # maximumpoint = 98 + (10 - (98%10)) = 98 + (10-8) = 98 + 2 = 100
                                                                     # Thus one can see 100 is a much nicer number to play around with
    initial = period
    periodtracker = 1
    for x in range(initial, (rangemax+period), period): # The last arguement tells the for loop to increment x by the period
        count = 0
        temp = x
        lower_range = temp - period
        higher_range = (period*periodtracker)-1
        lower_range_string = str(lower_range)
        higher_range_string = str(higher_range)
        for i in range(0, len(begindates)):
          if ((no_days[i] <= higher_range) and (no_days[i] >= lower_range)):
              count += 1
        temp1 = "(" + lower_range_string + ", " + higher_range_string + ")"
        periodtracker += 1
        x_axis.append(temp1) # Inclusive Range
        y_axis.append(count)
    tle = "Time Series Lengths For Each Site Grouped by " + str(period) + " days" # We must convert period to string to be able to concatenate all this strings.
    pt.title(tle)
    pt.bar(x_axis, y_axis, color = "red")
    pt.grid()
    pt.xlabel('Number of Days Site Active')
    pt.ylabel('Number of Sites')
    pt.xticks(rotation = 45, fontsize = 'xx-small')
    pt.tight_layout()
    add_labels_bargraph(x_axis, y_axis)
    pt.savefig("/Volumes/SeagateBackupPlusDrive/reuriverdata/Graphs/TimeSeriesLengthsGraphGrouped", dpi=1200)
    pt.show()
    return no_days

def add_labels_bargraph(x_coor,y_coor):
    for i in range(0, len(x_coor)):
        pt.text(i,y_coor[i], y_coor[i], fontsize = 'xx-small')
"""
    
def max_array_temperatures():
    sites = getsites()
    max_temps = []
    
    for i in range(0, len(sites)):
        temp = []
        path = SITE_DATA_PATH + str(sites[i]) + ".txt"
        with open(path, 'r') as f:
            lines = f.readlines()
            for l in lines[0:]:
                temp.append(l.split('\t')[5])
        max_temps.append(findmax(temp))
    print(max_temps)
    return max_temps

"""

def findmaxallsites(sites):
    maxtemplist = []
    overall_max_temp = 0
    for i in range(0, len(sites)):
        temp_max = 0
        data_path = REU_DATA_PATH + sites[i]
        with open(data_path, 'r') as f:
            lines = f.readlines()
            for l in lines[0:]:
                try:
                    temp = float(l.split('\t')[4])
                    if (temp > temp_max):
                            temp_max = temp
                    if (temp > overall_max_temp):
                            overall_max_temp = temp
                except ValueError:
                    print ("Not a float in site => ", sites[i], " ==> ", l.split('\t')[4])
        print(sites[i], " ==> max: ", temp_max)
        maxtemplist.append(temp_max)
    return constrainmaxlist(maxtemplist, overall_max_temp)

def constrainmaxlist(maxtemplist, overall_max_temp):
    for i in range(0, len(maxtemplist)):
        temp_max_list_value = float(maxtemplist[i])
        maxtemplist[i] = (temp_max_list_value/overall_max_temp)
    return maxtemplist
    
def average2DGradient(latitudes, longitudes):
    sites = os.listdir(Paths.FINAL_DATA_PATH)
    mean_longitude = statistics.mean(longitudes)
    mean_latitude = statistics.mean(latitudes)
    max_temp_list = npy.array(findmaxallsites(sites))
    latitudes = npy.array(latitudes)
    longitudes = npy.array(longitudes)
    print('Number of sites used => ', + len(max_temp_list))
    
    # For the heat map, the input data must be an array of arrays so for example:
        # data = [[latitude, longitude, data],
        #         [latitude, longitude, data],
        #         [latitude, longitude, data]]
    # This is what the below line will do and result in the data array we want.
    
    latitudes2 = []
    longitudes2 = []
    
    for i in range(0, len(sites)):
        latitudes2.append(latitudes[i])
        longitudes2.append(longitudes[i])
    data = npy.stack((latitudes2, longitudes2, max_temp_list), axis = -1)
    print(data)
    
    # Creating and saving the Heatmap that DOES NOT have labels of the site numbers associated with them
    mapObj = folium.Map(location = [mean_latitude, mean_longitude], 
                        zoom_start = 5
                        )
    HeatMap(data).add_to(mapObj)
    mapObj.save(Paths.FULL_PATH_HEATPMAP_NAME)
    
    # Creating and saving the Heatmap that DOES have labels of the site numbers associated with them
    mapObj = folium.Map(location = [mean_latitude, mean_longitude], 
                        zoom_start = 5
                        )
    HeatMap(data).add_to(mapObj)
    
    for i in range(0, len(data)):
        folium.Marker(
            location = [latitudes[i], longitudes[i]],
            popup = sites[i]
            ).add_to(mapObj)
        
    mapObj.save(Paths.FULL_PATH_HEATPMAP_NAME_POPUPS)
    
    print("2D Gradiant Successful \n \n")
