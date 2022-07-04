#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: salvadorguel
Mentor: Dr. Anthony Parolari
Date: Summer 2022
Universtiy: Marquette University
Project: Summer Research Experience for Undergraduates (REU). Focusing on Hardware, Embedded Software, and Analytics for Environment Quality Monitoring
Description:
    a) This program, gives "reu2022urldownload.py" the functions needed to make things simpler and more
    readable in the main python script. Thus, these helper functions are the crucial pieces to help in accomplishment.
"""
import os # Need this module to be able to have the OS access the file explorer and delete things for us.

""" 
# Really no need for this function. The 200 code always happens even if .txt file empty.

def CheckRequest(response):
    if (response == 200):
        return "Success"
    elif (response == 404):
        print("-- There was a 404 error  => ", end= "")
        return "404"
    else: 
        print ("-- There was an unknown error  => ", end= "")
        return "Unknown"
"""

#%% URLgenerator(siteno, begindate, enddate):
#    => This function is used to generate a URL note that you need 3 arguements. These paraameters are used to
#       create the unique URLs for each and every site that takes a river's temperature.
#    => It returns a generated URL
#%%
def URLgenerator(siteno, begindate, enddate):
    urla = 'https://nwis.waterdata.usgs.gov/nwis/uv?cb_00010=on&format=rdb&site_no='
    # sitno goes here
    urlb = '&period=&begin_date='
    # begin date should go here (of the water quality measurements)
    urlc = "&end_date="
    # end date should go next (of the water quality measurements)
    return (urla + siteno + urlb + begindate + urlc + enddate)

#%% stripfile(filename):
#    => This function just takes off the entire header of the .txt files (aka all the lines that have no data).
#    => This only returns the cd directory link to the newly produced AllStationsWithTemp.txt.
#%%
def stripfile(filename):
    output = "/Users/salvadorguel/.spyder-py3/FinalProgramREU/stripped/AllStationsWithTemp.txt"
    with open(filename, "r") as infile:
        with open(output, "w") as file:
            for line in infile:
                if line.startswith('USGS'):
                    file.write(line)
    return output

#%%
# checkEmpty(filename)
#    => This function allows me to delete the data for the sites that literally have no data available so
#       we dont waste space with blank text files.
#%%
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