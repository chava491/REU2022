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
    b) Below you will find some brief explanation of what each function does.
    
  ______________________________________________________________________________________________
 |                              Function Table (Summaraization)                                 |
 |______________________________________________________________________________________________|
 |__________Name________|__________Format_____________________|__________Description____________|
 |                      |                                     | This will check if the url      |
 |      CheckRequest    |       CheckRequest(response)        | was used successfully to        |
 |______________________|_____________________________________|_download its entire contents____|
 |                      |                                     |                                 |
 |      URLgenerator    | URLgenerator(begin date, end date)  | This will generate a url with   |
 |______________________|_____________________________________|_the desired passed in parameters|
 |                      |                                     | This will strip the file of any |
 |      stripfile       |        stripfile(filename)          | and every line not starting with|
 |______________________|_____________________________________|_usgs____________________________|
 |                      |                                     | This function will check that   |
 |      checkEmpty      |        checkEmpty(filename)         | the given file path is not empty|
 |______________________|_____________________________________|_________________________________|
 |                      |                                     | This function will save an array|
 |      savearray       |   savearray(filenamewanted, array)  | in the form of [' ',...,' '] in |
 |______________________|_____________________________________|_a textfile on the disk__________|
 |                      |                                     | This function will save an array|
 |    savearrayline     | savearrayline(filenamewanted, array,| with each element of that array |
 |______________________|__choice)____________________________|_taking up only one line_________|  
 |                      |                                     | This function just generates all|
 |      getsites        |            getsites()               | the needed URLs to compile the  |
 |                      |                                     | list of sites with end and begin| 
 |______________________|_____________________________________|_dates___________________________| 
"""
import os            # Need this module to be able to have the OS access the file explorer and delete things for us.
import numpy as npy
import itertools
import URLs          # Imports all the URL variables I have defiend 

def CheckRequest(response):
    if (response == 200):
        return "Success"
    elif (response == 404):
        print("-- There was a 404 error  => ", end= "")
        return "404"
    else: 
        print ("-- There was an unknown error  => ", end= "")
        return "Unknown"

#%% URLgenerator(siteno, begindate, enddate):
#    => This function is used to generate a URL note that you need 3 arguements. These paraameters are used to
#       create the unique URLs for each and every site that takes a river's temperature.
#    => It returns a generated URL
#%%
def URLgenerator(siteno, begindate, enddate):
    urla = 'https://nwis.waterdata.usgs.gov/nwis/uv?cb_00010=on&format=rdb&site_no='
    # sitno goes here (aka when URL is put together)
    urlb = '&period=&begin_date='
    # begin date should go here (of the water quality measurements. Aka when URL is put together)
    urlc = "&end_date="
    # end date should go next (of the water quality measurements. Aka when URL is put together)
    return (urla + siteno + urlb + begindate + urlc + enddate)
    
#%% stripfile(filename):
#    => This function just takes off the entire header of the .txt files (aka all the lines that have no data).
#    => This only returns the cd directory link to the newly produced AllStationsWithTemp.txt.
#%%
def stripfile(filename):
    output = "/Volumes/SeagateBackupPlusDrive/reuriverdata/temp/stripped/tempstatecodegrab.txt"
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
    
#%%
# savearray(filenamewanted, array)
#    => This function saves an array of your choosing with the name of your choosing in the format seen in the example below
#        [1, 2, 3, 4, 5] => This is how it would look when the textfile is opened
#%%
def savearray(filenamewanted, array):
    arraytosave = npy.array(array)
    filepath = '/Volumes/SeagateBackupPlusDrive/reuriverdata/temp/' + filenamewanted + '.txt'
    file = open(filepath, "w+")

    # Save array to file
    content = str(arraytosave)
    file.write(content)
    file.close()
    
#%% Following code provided by 
# https://stackoverflow.com/questions/14941854/how-to-print-several-array-elements-per-line-to-text-file
def grouper(n, iterable):
    it = iter(iterable)
    while True:
       chunk = tuple(itertools.islice(it, n))
       if not chunk:
           return
       yield chunk
       
def savearrayline(filenamewanted, array, choice):
    if (choice == 'S'):
        filepath = '/Volumes/SeagateBackupPlusDrive/reuriverdata/lists/successfull/' + filenamewanted + '.txt'
        with open(filepath, "w") as f:
            for chunk in grouper(1, array):
                f.write(" ".join(str(x) for x in chunk) + "\n")
    elif (choice == 'F'):
        filepath = '/Volumes/SeagateBackupPlusDrive/reuriverdata/lists/failed/' + filenamewanted + '.txt'
        with open(filepath, "w") as f:
            for chunk in grouper(1, array):
                f.write(" ".join(str(x) for x in chunk) + "\n")
    elif (choice == 'Statecodes'): # This is the file for the urls generated by by the use of statecodes that will then be used to extract the begin and end dates.
        filepath = '/Volumes/SeagateBackupPlusDrive/reuriverdata/lists/StateCodeURLs/' + filenamewanted + '.txt'
        with open(filepath, "w") as f:
            for chunk in grouper(1, array):
                f.write(" ".join(str(x) for x in chunk) + "\n")
    elif (choice == 'SiteInfoFinal'):
        filepath = '/Volumes/SeagateBackupPlusDrive/reuriverdata/lists/' + filenamewanted + '.txt'
        with open(filepath, "w") as f:
            for chunk in grouper(1, array):
                f.write(" ".join(str(x) for x in chunk) + "\n")
                
#%%
# getsites()
#    => This function compiles all the URLs that will be used to extract site number, begin date, and end date of ever
#       site that takes continous timeseries water temperature data.
#%%
def getsites():
    urlfordates = []
    for i in range(0, len(URLs.FIPSTATECODES)):
        tempurl = 'https://waterservices.usgs.gov/nwis/site/?format=rdb&stateCd=' + URLs.FIPSTATECODES[i] + '&seriesCatalogOutput=true&outputDataTypeCd=iv&parameterCd=00010&siteType=ST&siteStatus=all&hasDataTypeCd=iv'
        urlfordates.append(tempurl)
    return urlfordates