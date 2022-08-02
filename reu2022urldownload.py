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
    b) Then it will save these in arrays making sure to get rid of any that dont have any of the 3 values listed above as well as the sites respective latitude and longitude.
    c) Thus, with all this info I then generate a URL that is specific for the site and then I use said URL to download the data for that
    river's water temperature which is all looked at and made sure no waste of space is spent on empty downloaded text files. It is also
    important to note that these text files are named as the respective site number.
    

Side Note: We are using the following website: https://waterservices.usgs.gov/rest/Site-Service.html.
For more explanation on how the URLs work and are generated, visit the following website:
    https://waterservices.usgs.gov/rest/Site-Service.html
    
Other helpful links:
    1) USGS Current Conditions for the Nation:
        a) https://waterdata.usgs.gov/nwis/uv?state_cd=wi&index_pmcode_00010=1&index_pmcode_00011=1&format=station_list&group_key=NONE&range_selection=days&period=7&begin_date=2022-06-07&end_date=2022-06-14&date_format=YYYY-MM-DD&rdb_compression=file&list_of_search_criteria=state_cd%2Crealtime_parameter_selection
    2) Next Generation Monitoring Location Page:
        a) https://waterdata.usgs.gov/nwis
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests             # Imports the requests module of Python
import os                   # Imports the os module that allows us to delete contents from the disk
import Paths                # Imports the Paths .py file that contains all the file paths for saving and reading from

import HFuncs as HELPER_FUNC     # Imports all of the functions I defined in HFuncs
import REU2022stats as REU_STATS # Imports all of the functions I defined in HFuncs
#%% Global Variables
BEGINDATES = []             # Begin dates for every available site
ENDDATES = []               # End dates for every available site
SITENO = []                 # Site numbers with continous timeseries water temperature data
SITE_LATITUDES = []         # Site latitudes for all respective sites
SITE_LONGITUDES = []        # Site longitudes for all respective sites
GENERATEDURLS = []          # This array stores all the individual site's url that contains all water temperature data in 
                            #   the range of its begin and end date

def updatedata():
    urlfordates = REU_STATS.getsitesboot()    # Goes to USGS website, it will also download completely new sites if they become available

# Now we need a way to go through all the urls and then append all the site numbers, begin dates, end dates, while making sure that the line says USGS and that the parameter code is 00010
    for i in range(0, len(urlfordates)):
        URL = urlfordates[i]
        response = requests.get(URL)                                            # Getting content from the URL we are currently on.
        if (HELPER_FUNC.CheckRequest(response.status_code) == "Success"):                                   # Here we check that the URL was indeed valid and we got something back.)
            with open(Paths.TEMP_STATE_CODE_GRABBED_PATH, 'wb') as f:
                f.write(response.content)
                outputfile = HELPER_FUNC.stripfile(Paths.TEMP_STATE_CODE_GRABBED_PATH)                            # Comment back in when not using flashdrive
            with open(outputfile, "r") as temp:
                lines = temp.readlines()
                for l in lines[0:]:
                    site_no = l.split('\t')[1] # This is saying (from left to right) we are getting the item in the second column of the current line
                    if '00010' in l:
                        print('Site number => ', site_no)
                        if ((l.split('\t')[0] == 'USGS')):
                            ENDDATES.append(l.split()[-2]) # The number used is -2 because this signifies the second to last column of the text file which is the temperature values
                            BEGINDATES.append(l.split()[-3])        # The number used is -5 because this signifies the third to last column of the text file which is the date values
                            SITENO.append(site_no)
                            latitude = REU_STATS.obtainlatitude(site_no)
                            longitude = REU_STATS.obtainlongitude(site_no)
                            SITE_LATITUDES.append(latitude)
                            SITE_LONGITUDES.append(longitude)
                            print('Latitude    => ', latitude)
                            print('Longitude   => ', longitude)
                            print('--------------------------')

    temparray = []
    
    for i in range(0, len(SITENO)):
        # file columns as follows: SITE NUMBER - BEGIN DATE - END DATE - DECIMAL LATITUDE - DECIMAL LONGITUDE
        temparray.append(SITENO[i] + '\t' + BEGINDATES[i] + '\t' + ENDDATES[i] + '\t' + SITE_LATITUDES[i] + '\t' + SITE_LONGITUDES[i])
    REU_STATS.savearrayline('SiteInfoDraft', temparray, 'SiteInfoDraft')
    REU_STATS.savearrayline('StateCodeURLs', urlfordates, 'StateCodeURLs'),
#Here we now are going to generate all of the URLs that we will be using to download everything. Then we will be transfering the downloaded
# data onto a file named "middleman" that will be used as sort of a temp txt file for all the text files that will be messed with.
# Then I make sure to check that the downloaded data is not just an empty text file, due to no data being available.

    failedcount = 0
    successfulcount = 0
    failedattempts = []
    successfulsites = []
    failedURLS = []
    rangemax = len(SITENO)
    temparr = []

    if ((len(SITENO) == len(BEGINDATES)) and (len(SITENO) == len(ENDDATES))):
        for i in range(0, rangemax):
            URL = REU_STATS.URLgenerator(SITENO[i], BEGINDATES[i], ENDDATES[i])
            response = requests.get(URL)              # Getting the content From the Website
            fullpath = Paths.FINAL_DATA_PATH + SITENO[i] + '.txt'
            print('--------------------------- ', )
            print('site no   =>', SITENO[i])
            print('For i     =>', i)
            print('code      =>', response.status_code)
            with open(Paths.MIDDLEMAN_PATH, 'wb') as f:
                f.write(response.content)
                with open(Paths.MIDDLEMAN_PATH, "r") as infile:
                    with open(fullpath, "w") as file:
                        for line in infile:
                            if line.startswith('USGS'):
                                file.write(line)
            f.close()
            infile.close()
            file.close()
            
        # Keep tally of all the successes and failures to make sure everything was done properly at the end through comparison of the count
        # to the actual amount of textfiles in my data folder.
            if (HELPER_FUNC.checkEmpty(fullpath) == False):
                temparr.append(SITENO[i] + '\t' + BEGINDATES[i] + '\t' + ENDDATES[i] + '\t' + SITE_LATITUDES[i] + '\t' + SITE_LONGITUDES[i])
                GENERATEDURLS.append(URL)
                successfulsites.append(SITENO[i])
                successfulcount+=1
            else:
                failedattempts.append(SITENO[i] + '\t' + BEGINDATES[i] + '\t' + ENDDATES[i] + '\t' + SITE_LATITUDES[i] + '\t' + SITE_LONGITUDES[i])
                failedURLS.append(URL)
                failedcount+=1
            print("Successfully Downloaded ", successfulcount, " out of ", len(SITENO))
            print("Failed to Download ", failedcount)
            f.close()
        
        os.remove(Paths.MIDDLEMAN_PATH)

    print('done!')
    print("There were ", (rangemax - failedcount), " out of ", len(SITENO), " sites generated ")
    print('')
    print(GENERATEDURLS)
    print('')
    print('These are all the sites that were successfully downloaded')
    print(successfulsites)
    
    REU_STATS.savearrayline('SiteInfoFinal', temparr, 'SiteInfoFinal')
    REU_STATS.savearrayline('successfulsites', successfulsites, 'S')
    REU_STATS.savearrayline('generatedurls', GENERATEDURLS, 'S')
    REU_STATS.savearrayline('failedsites', failedattempts, 'F')
    REU_STATS.savearrayline('failedurls', failedURLS, 'F')
###########END OF updatedata()
