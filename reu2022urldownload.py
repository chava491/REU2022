"""
Author: salvadorguel
Mentor: Dr. Anthony Parolari
Date: Summer 2022
Universtiy: Marquette University
Project: Summer Research Experience for Undergraduates (REU). Focusing on Hardware, Embedded Software, and Analytics for Environment Quality Monitoring
Description:
    a) This program, with the help of the following other two python code files "HFuncs.py" and "URLs.py", first looks up online a list that
    gives one the site no, begin date, and end date for that respective sites water quality water temperature measurements for the existing
    range.
    b) Then it will save these in arrays making sure to get rid of any that dont have any of the 3 values listed above.
    c) Thus, with all this info I then generate a URL that is specific for the site and then I use said URL to download the data for that
    river's water temperature which is all looked at and made sure no waster of space is spent on empty downloaded text files.
    

Side Note: We are using the following website: https://waterservices.usgs.gov/rest/Site-Service.html and the following site numbers: 
https://waterdata.usgs.gov/nwis/uv?state_cd=wi&index_pmcode_00010=1&index_pmcode_00011=1&format=station_list&group_key=NONE&range_selection=days&period=7&begin_date=2022-06-07&end_date=2022-06-14&date_format=YYYY-MM-DD&rdb_compression=file&list_of_search_criteria=state_cd%2Crealtime_parameter_selection
This data will be downloaded and saved to the computer.  
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests      # Imports the requests module of Python
from HFuncs import * # Imports all of the functions I defined in HFuncs
import URLs          # Imports all the URL variables I have defiend 
import os
import numpy as npy
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
   # with open('/Users/salvadorguel/.spyder-py3/FinalProgramREU/download/AllStationsWithTemp.txt', 'wb') as f:              # Comment back in when not using flashdrive
    with open('/Volumes/SeagateBackupPlusDrive/reuriverdata/temp/AllStationsWithTemp.txt', 'wb') as f:
        f.write(response.content)
       # outputfile = stripfile('/Users/salvadorguel/.spyder-py3/FinalProgramREU/download/AllStationsWithTemp.txt')
        outputfile = stripfile('/Volumes/SeagateBackupPlusDrive/reuriverdata/temp/AllStationsWithTemp.txt')                            # Comment back in when not using flashdrive
        
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
failedURLS = []
rangemax = len(SITENO)

if ((len(SITENO) == len(BEGINDATES)) and (len(SITENO) == len(ENDDATES))):
    for i in range(0, rangemax):
        URL = URLgenerator(SITENO[i], BEGINDATES[i], ENDDATES[i])
        response = requests.get(URL)              # Getting the content From the Website
        #fullpath = '/Users/salvadorguel/.spyder-py3/FinalProgramREU/Data/' + SITENO[i]
        #middleman = '/Users/salvadorguel/.spyder-py3/FinalProgramREU/Data/middleman'
        fullpath = '/Volumes/SeagateBackupPlusDrive/reuriverdata/' + SITENO[i] + '.txt'
        middleman = '/Volumes/SeagateBackupPlusDrive/reuriverdata/temp/middleman'
        print('--------------------------- ', )
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
            failedURLS.append(URL)
            failedcount+=1
        print("Successfully Downloaded ", (rangemax - failedcount), " out of ", len(SITENO))
        f.close()
        
os.remove(middleman)

print('done!')
print("There were ", (rangemax - failedcount), " out of ", len(SITENO), " sites generated ")
print('')
print(GENERATEDURLS)
print('')
print('These are all the sites that were successfully downloaded')
print(successfulsites)

savearrayline('successfulsites', successfulsites, 'S')
savearrayline('generatedurls', GENERATEDURLS, 'S')
savearrayline('failedsites', failedattempts, 'F')
savearrayline('failedurls', failedURLS, 'F')