"""
Author: salvadorguel
Mentor: Dr. Anthony Parolari
Date: Summer 2022
Universtiy: Marquette University
Project: Summer Research Experience for Undergraduates (REU). Focusing on Hardware, Embedded Software, and Analytics for Environment Quality Monitoring
Description:
    a) This program, with the help of the following other two python code files "HFuncs.py" and "URLs.py", firstly compiles a list
       that contains the site number, begin date, and end date of sites with the paramter code 00010. This means that the site
       takes continous timeseries water data. Thus, this water data is taken at a period that is known and unchanged.
    b) Then it will save these in arrays making sure to get rid of any that dont have any of the 3 values listed above.
    c) Thus, with all this info I then generate a URL that is specific for the site and then I use said URL to download the data for that
    river's water temperature which is all looked at and made sure no waste of space is spent on empty downloaded text files. It is also
    important to note that these text files are named as the respective site number.
    

Side Note: We are using the following website: https://waterservices.usgs.gov/rest/Site-Service.html.
For more explanation on how the URLs work and are generated, visit the following website:
    https://waterservices.usgs.gov/rest/Site-Service.html
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests      # Imports the requests module of Python
from HFuncs import * # Imports all of the functions I defined in HFuncs
import os            # Imports the os module that allows us to delete contents from the disk
#%% Global Variables
BEGINDATES = []      # This array will store all the begin dates for every available site
ENDDATES = []        # This array will store all the end dates for every available site
SITENO = []          # This array will store all the site numbers with continous timeseries water temperature data
GENERATEDURLS = []   # This array stores all the individual site's url that contains all water temperature data in the range of its begin and end date

def updatedata():
    urlfordates = getsites()
    print(urlfordates)

# Now we need a way to go through all the urls and then append all the site numbers, begin dates, end dates, while making sure that the line says USGS and that the parameter code is 00010
    for i in range(0, len(urlfordates)):
        URL = urlfordates[i]
        response = requests.get(URL)                                                            # Getting content from the URL we are currently on.
        if (CheckRequest(response.status_code) == "Success"):                                   # Here we check that the URL was indeed valid and we got something back.)
            savelocation = '/Volumes/SeagateBackupPlusDrive/reuriverdata/temp/tempstatecodegrab.txt'
            with open(savelocation, 'wb') as f:
                f.write(response.content)
                outputfile = stripfile(savelocation)                            # Comment back in when not using flashdrive
            with open(outputfile, "r") as temp:
                lines = temp.readlines()
                for l in lines[1:]:
                    site_no = l.split('\t')[1] # This is saying (from left to right) we are getting the item in the second column of the current line
                    if '00010' in l:
                        print('site number => ', site_no)
                        if ((l.split('\t')[0] == 'USGS')):
                            ENDDATES.append(l.split()[-2]) # The number used is -2 because this signifies the second to last column of the text file which is the temperature values
                            BEGINDATES.append(l.split()[-3])        # The number used is -5 because this signifies the third to last column of the text file which is the date values
                            SITENO.append(site_no)
    temparray = []
    for i in range(0, len(SITENO)):
        temparray.append(SITENO[i] + ' ' + BEGINDATES[i] + ' ' + ENDDATES[i])
    savearrayline('SiteInfoFinal', temparray, 'SiteInfoFinal')
    
#Here we now are going to generate all of the URLs that we will be using to download everything. Then we will be transfering the downloaded
# data onto a file named "middleman" that will be used as sort of a temp txt file for all the text files that will be messed with.
# Then I make sure to check that the downloaded data is not just an empty text file, due to no data being available.

    failedcount = 0
    successfulcount = 0
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
            fullpath = '/Volumes/SeagateBackupPlusDrive/reuriverdata/data/' + SITENO[i] + '.txt'
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
        # Keep tally of all the successes and failures to make sure everything was done properly at the end through comparison of the count
        # to the actual amount of textfiles in my data folder.
            if (checkEmpty(fullpath) == False):
                GENERATEDURLS.append(URL)
                successfulsites.append(SITENO[i])
                successfulcount+=1
            else:
                failedattempts.append(SITENO[i])
                failedURLS.append(URL)
                failedcount+=1
            print("Successfully Downloaded ", successfulcount, " out of ", len(SITENO))
            print("Failed to Download ", failedcount)
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
###########END OF updatedata()