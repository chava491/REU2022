#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 15:54:16 2022
@author: salvadorguel
"""
import os

def CheckRequest(response):
    if (response == 200):
        return "Success"
    elif (response == 404):
        print("-- There was a 404 error  => ", end= "")
        return "404"
    else: 
        print ("-- There was an unknown error  => ", end= "")
        return "Unknown"
    
def URLgenerator(siteno, begindate, enddate):
    urla = 'https://nwis.waterdata.usgs.gov/nwis/uv?cb_00010=on&format=rdb&site_no='
    # sitno goes here
    urlb = '&period=&begin_date='
    # begin date should go here (of the water quality measurements)
    urlc = "&end_date="
    # end date should go next (of the water quality measurements)
    return (urla + siteno + urlb + begindate + urlc + enddate)

def stripfile(filename):
    output = "/Users/salvadorguel/.spyder-py3/FinalProgramREU/stripped/AllStationsWithTemp.txt"
    with open(filename, "r") as infile:
        with open(output, "w") as file:
            for line in infile:
                if line.startswith('USGS'):
                    file.write(line)
    return output

def checkEmpty(filename):
    filesize = os.stat(filename).st_size
    print('os stat   =>', filesize)
    if(filesize == 0):
        print("full path =>", filename)
        os.remove(filename)
        print('empty     => true')
        return True
    else:
        print('empty     => False')
        return False