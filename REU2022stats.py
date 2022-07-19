#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 01:53:36 2022

@author: salvadorguel
"""
import requests
import os
from HFuncs import * # Imports all of the functions I defined in HFuncs
from datetime import datetime
import numpy as npy
import matplotlib.pyplot as pt

SITE_INFO_PATH = '/Volumes/SeagateBackupPlusDrive/reuriverdata/lists/SiteInfoFinal.txt'
SAVE_LOCATION_LATITUDE = '/Volumes/SeagateBackupPlusDrive/reuriverdata/temp/templatitude.txt'
SAVE_LOCATION_LONGITUDE = '/Volumes/SeagateBackupPlusDrive/reuriverdata/temp/templongitude.txt'

def average2DGradient():
    #Need to check how to pass in an array as an arguement
    print("2D Gradiant Successful \n \n")

def getsites():
    sites = []
    with open(SITE_INFO_PATH, 'r') as f:
        lines = f.readlines()
        for l in lines[0:]:
            sites.append(l.split('\t')[0])
    return sites

def getbegindates():
    begindates = []
    with open(SITE_INFO_PATH, 'r') as f:
        lines = f.readlines()
        for l in lines[0:]:
            begindates.append(l.split('\t')[1])
    return begindates

def getenddates():
    enddates = []
    with open(SITE_INFO_PATH, 'r') as f:
        lines = f.readlines()
        for l in lines[0:]:
            enddates.append(l.split('\t')[2])
    return enddates

def latitudes():
    latitudes = []
    with open(SITE_INFO_PATH, 'r') as f:
        lines = f.readlines()
        for l in lines[0:]:
            latitudes.append(l.split('\t')[3])
    return latitudes

def longitudes():
    longitudes = []
    with open(SITE_INFO_PATH, 'r') as f:
        lines = f.readlines()
        for l in lines[0:]:
            longitudes.append(l.split('\t')[4])   
    return [x[:-1] for x in longitudes] # We need to do this because this array is '#\n'. Thus, by adding the 
                                        # [x[:-1] for x in ARRAYNAME] we just keep the # and not the \n character

def obtainlatitude(siteno):
    urla = 'https://waterdata.usgs.gov/nwis/uv?referred_module=qw&search_site_no='
    # sitno goes here (aka when URL is put together)
    urlb = '&search_site_no_match_type=exact&index_pmcode_00010=1&index_pmcode_91110=1&index_pmcode_91111=1&group_key=NONE&format=sitefile_output&sitefile_output_format=rdb&column_name=agency_cd&column_name=dec_lat_va&column_name=dec_long_va&range_selection=days&period=7&rdb_compression=file&list_of_search_criteria=search_site_no%2Crealtime_parameter_selection'
    URL = urla + siteno + urlb
    response = requests.get(URL)     # Getting content from the URL we are currently on.
    if (CheckRequest(response.status_code) == "Success"):                                   # Here we check that the URL was indeed valid and we got something back.)
        with open(SAVE_LOCATION_LATITUDE, 'wb') as f:
               f.write(response.content)
        with open(SAVE_LOCATION_LATITUDE, "r") as temp:
            lines = temp.readlines()
            for l in lines[0:]:
                if (l.startswith('USGS')):
                    latitude = l.split()[1]
    return latitude
            
def obtainlongitude(siteno):
    urla = 'https://waterdata.usgs.gov/nwis/uv?referred_module=qw&search_site_no='
    # sitno goes here (aka when URL is put together)
    urlb = '&search_site_no_match_type=exact&index_pmcode_00010=1&index_pmcode_91110=1&index_pmcode_91111=1&group_key=NONE&format=sitefile_output&sitefile_output_format=rdb&column_name=agency_cd&column_name=dec_lat_va&column_name=dec_long_va&range_selection=days&period=7&rdb_compression=file&list_of_search_criteria=search_site_no%2Crealtime_parameter_selection'
    URL = urla + siteno + urlb
    response = requests.get(URL)  # Getting content from the URL we are currently on.
    if (CheckRequest(response.status_code) == "Success"):                                   # Here we check that the URL was indeed valid and we got something back.)
        with open(SAVE_LOCATION_LONGITUDE, 'wb') as f:
            f.write(response.content)
        with open(SAVE_LOCATION_LONGITUDE, "r") as temp:
            lines = temp.readlines()
            for l in lines[0:]:
                if (l.startswith('USGS')):
                    longitude = l.split('\t')[2] # This is saying (from left to right) we are getting the item in the 3rd column of the current line     
    return longitude

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