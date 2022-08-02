#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 19:27:01 2022

@author: salvadorguel
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

def findmaxallsites(sites):
    maxtemplist = []
    overall_max_temp = 0
    for i in range(0, len(sites)):
        temp_max = 0
        data_path = Paths.REU_DATA_PATH + sites[i]
        with open(data_path, 'r') as f:
            lines = f.readlines()
            for l in lines[0:]:
                try:
                    temp = float(l.split('\t')[4])
                    if ((temp > temp_max) and (temp < 100)):
                            temp_max = temp
                    if ((temp > overall_max_temp) and ((temp < 100))):
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
    
def Maximum2DGradient(latitudes, longitudes):
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

def findaverageallsites(sites):
    averageslist = []
    for i in range(0, len(sites)):
        temp_array_data = []
        data_path = Paths.REU_DATA_PATH + sites[i]
        with open(data_path, 'r') as f:
            lines = f.readlines()
            for l in lines[0:]:
                try:
                    temp = float(l.split('\t')[4])
                    if ((temp < 100) and (temp > -1)):
                       temp_array_data.append(temp) 
                except ValueError:
                    #print ("Not a float in site => ", sites[i], " ==> ", l.split('\t')[4])
                    continue # Do nothing, just keep going.
        try: 
            average = statistics.mean(temp_array_data)
            averageslist.append(average)
            print("Site ", sites[i], " Average => ", average)
        except:
            print("No data for site -> ", sites[i])
            averageslist.append(0)
    return averageslist

def Average2DGradiant(latitudes, longitudes):
    sites = os.listdir(Paths.FINAL_DATA_PATH)
    mean_longitude = statistics.mean(longitudes)
    mean_latitude = statistics.mean(latitudes)
    averages_list = npy.array(findaverageallsites(sites))
    latitudes = npy.array(latitudes)
    longitudes = npy.array(longitudes)
    print('Number of sites used => ', + len(averages_list))
    
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
    data = npy.stack((latitudes2, longitudes2, averages_list), axis = -1)
    print(data)
    
    # Creating and saving the Heatmap that DOES NOT have labels of the site numbers associated with them
    mapObj = folium.Map(location = [mean_latitude, mean_longitude], 
                        zoom_start = 5,
                        radius = 1,
                        weight = 0.1,
                        opacity = 0.1,
                        fill_opacity = 0.1
                        )
    HeatMap(data).add_to(mapObj)
    mapObj.save(Paths.FULL_PATH_HEATPMAP_NAME)
    
    # Creating and saving the Heatmap that DOES have labels of the site numbers associated with them
    mapObj = folium.Map(location = [mean_latitude, mean_longitude], 
                        zoom_start = 5,
                        radius = 1,
                        weight = 0.1,
                        opacity = 0.1,
                        fill_opacity = 0.1
                        )
    HeatMap(data).add_to(mapObj)
    
    for i in range(0, len(data)):
        folium.Marker(
            location = [latitudes[i], longitudes[i]],
            popup = sites[i]
            ).add_to(mapObj)
        
    mapObj.save(Paths.FULL_PATH_HEATPMAP_NAME_POPUPS)
    
    print("2D Gradiant Successful \n \n")