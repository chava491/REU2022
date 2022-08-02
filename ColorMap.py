#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 14:50:57 2022

@author: salvadorguel
"""
import os
import Paths
import statistics
import numpy

import matplotlib.pyplot as pt
import REU2022stats as stats

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

def findvarianceallsites(sites):
    varianceslist = []
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
            variance = numpy.var(temp_array_data)
            varianceslist.append(variance)
            print("Site ", sites[i], " Variance => ", variance)
        except:
            print("No data for site -> ", sites[i])
            varianceslist.append(0)
    return varianceslist

def create_color_map(latitudes, longitudes):
    sites = os.listdir(Paths.FINAL_DATA_PATH)
    
    #FINDING MIN AND MAX VALUES OF GRAPH INPUT ARGUEMENTS (NOT OF DATA)
    averages_list = findaverageallsites(sites)
    vmax = stats.findmax(averages_list)
    vmin = stats.findmin(averages_list)
    lat_min = stats.findmin(latitudes)
    lat_max = stats.findmax(latitudes)
    long_min = stats.findmin(longitudes)
    long_max = stats.findmax(longitudes)
    print(long_min)
    print(long_max)
    
    #AVERAGE GRAPH PLOT IMPLEMENTATION
    average_graph_title = "Average Temperature of " + str(len(averages_list)) + " Sites In Degrees Celsius"
    pt.title(average_graph_title)
    pt.grid()
    pt.xlabel('(WEST) Longitude (EAST)')
    pt.ylabel('(SOUTH) Latitude (NORTH)')
    pt.tight_layout()
    pt.scatter(longitudes, latitudes, s = 3, c = averages_list, vmin = vmin, vmax = vmax, cmap = 'coolwarm')
    pt.colorbar()
    pt.xlim(-170, -60)
    pt.ylim((lat_min-(lat_min*(0.05))), (lat_max+(lat_max*(0.05))))
    pt.locator_params(axis='x', nbins = 18)
    pt.xticks(fontsize = 'small')
    pt.savefig(Paths.FULL_PATH_COLOR_MAP_AVERAGE, dpi=1200)
    pt.clf()
    pt.cla()
    pt.close()
    
    #VARIANCE GRAPH PLOT IMPLEMENTATION
    variance_list = findvarianceallsites(sites)
    variance_graph_title = "Variances of Temperature (C) of " + str(len(variance_list)) + " Sites"
    pt.title(variance_graph_title)
    pt.grid()
    pt.xlabel('(WEST) Longitude (EAST)')
    pt.ylabel('(SOUTH) Latitude (NORTH)')
    pt.tight_layout()
    pt.scatter(longitudes, latitudes, s = 3, c = variance_list, vmin = vmin, vmax = vmax, cmap = 'brg')
    pt.colorbar()
    pt.xlim(-170, -60)
    pt.ylim((lat_min-(lat_min*(0.05))), (lat_max+(lat_max*(0.05))))
    pt.locator_params(axis='x', nbins = 18)
    pt.xticks(fontsize = 'small')
    pt.savefig(Paths.FULL_PATH_COLOR_MAP_VARIANCES, dpi=1200)
    pt.clf()
    pt.cla()
    pt.close()
    
    print("LONGITUDE MINIMUM => ", long_min)
    print("LONGITUDE MAXIMUM => ", long_max)
    print('Number of sites used => ', + len(averages_list))
    