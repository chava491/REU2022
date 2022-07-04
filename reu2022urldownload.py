"""
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests      # Imports the requests module of Python
from HFuncs import * # Imports all of the functions I defined in HFuncs
import URLs          # Imports all the URL variables I have defiend 
import os
#%% Global Variables
BEGINDATES = []
ENDDATES = []
SITENO = []
GENERATEDURLS = []

#%% HFUNCS
# ----------This file contains all the necessary helper funcgtions made custom when needed.
# Function Table (Summaraization)
#  ______________________________________________________________________________________________
# |__________Name________|__________Format_____________________|__________Description____________|
# |                      |                                     | This will check if the url      |
# |      CheckRequest    |       CheckRequest(response)        | was used successfully to        |
# |______________________|_____________________________________|_download its entire contents____|
# |                      |                                     |                                 |
# |      URLgenerator    | URLgenerator(begin date, end date)  | This will generate a url with   |
# |______________________|_____________________________________|_the desired passed in parameters|

#%% Obtain list of all available water quality measurements stations that took/take river water temperature measurements

URL = URLs.wqEntire                       # Bring the URL over from the other file we have it saved in.
response = requests.get(URL)              # Getting the content From the Website

#%% Here we check to make sure that everything went file. Only when we know it did, will we then upload the downloaded data to a
# file on the computer.
if (CheckRequest(response.status_code) == "Success"): # Here we check that the URL was indeed valid and we got something back.)
    with open('/Users/salvadorguel/.spyder-py3/FinalProgramREU/download/AllStationsWithTemp.txt', 'wb') as f:
        f.write(response.content)
        outputfile = stripfile('/Users/salvadorguel/.spyder-py3/FinalProgramREU/download/AllStationsWithTemp.txt')
        
#%% Here we are going to be getting rid of the sites with no date columns filled in.
    with open(outputfile, "r") as temp:
        lines = temp.readlines()
    # This will go through every single line - Note: The header is ignored.
    Totallinesskipped = 0
    for l in lines[1:]:
        if (l.split()[-2] == 'USGS') or (l.split()[-2] == '--'):
            Totallinesskipped+=1
        else:
            ENDDATES.append(l.split()[-1]) # The number used is -2 because this signifies the second to last column of the text file which is the temperature values
            BEGINDATES.append(l.split()[-2])        # The number used is -5 because this signifies the third to last column of the text file which is the date values
            SITENO.append(l.split()[-3])
    #print(len(ENDDATES))
    #print(len(BEGINDATES))
    #print(len(SITENO))
    
#%% Here we now are going to generate all of the URLs that we will be using to download everything. Then we will be transfering the downloaded
# data onto a file named "middleman" that will be used as sort of a temp txt file for all the text files that will be messed with.
# Then I make sure to check that the downloaded data is not just an empty text file, due to no data being available.

failedcount = 0
failedattempts = []
successfulsites = []
rangemax = len(SITENO)

if ((len(SITENO) == len(BEGINDATES)) and (len(SITENO) == len(ENDDATES))):
    for i in range(0, rangemax):
        URL = URLgenerator(SITENO[i], BEGINDATES[i], ENDDATES[i])
        response = requests.get(URL)              # Getting the content From the Website
        #if (CheckRequest(response.status_code) == "Success"):
        fullpath = '/Users/salvadorguel/.spyder-py3/FinalProgramREU/Data/' + SITENO[i]
        middleman = '/Users/salvadorguel/.spyder-py3/FinalProgramREU/Data/middleman'
        print('---------------------------')
        print('site no   =>', SITENO[i])
        print('For i     =>', i)
        print('code      =>', response.status_code)
        with open(middleman, 'wb') as f:
            f.write(response.content)
            with open(middleman, "r") as infile:
                with open(fullpath, "w") as file:
                    for line in infile:
                        if line.startswith('USGS'):
                            file.write(line)
        # Keep tally of ll the successes and failures to make sure everything was done properly at the end through comparison of the count
        # to the actual amount of textfiles in my data folder.
        if (checkEmpty(fullpath) == False):
            GENERATEDURLS.append(URL)
            successfulsites.append(SITENO[i])
        else:
            failedattempts.append(SITENO[i])
            failedcount+=1
                
        f.close()
os.remove(middleman)

print('done!')
print("There were ", (rangemax - failedcount), " out of ", len(SITENO), " sites generated ")
print('')
print(GENERATEDURLS)
