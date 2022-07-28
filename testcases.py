#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 03:22:17 2022

Author: salvadorguel
Mentor: Dr. Anthony Parolari
Date: Summer 2022
Universtiy: Marquette University
Project: Summer Research Experience for Undergraduates (REU). Focusing on Hardware, Embedded Software, and Analytics for Environment Quality Monitoring
Description: This script will contain all of my test functions that I will use to debug the code as well as all the test functions that check the path of the files to make
sure that everythig exists and if not then it will either ask you to update the archive or to just reformat all the SiteFinalInfo.txt to reflect the files that are actually 
located on the harddrive and available for us to use.
"""

import Paths
import os.path

import ObtainInfoFromArchive as OIFA

# Test that the master list (SiteInfoFinal.txt) is actually accurate and that all of the data text files for these exist
def TestAllFilesListedAreDownloaded():
    SITES_FROM_ARCHIVE_SITE_INFO_FINAL = OIFA.getsites()
    failed_sites = OIFA.getfailedsites()
    
    print('')
    print('1) All Sites That Failed To Download ==> '  , len(failed_sites))
    print('')
    print("2) Test To See If All Files Data Text Files Are Present")
    if (len(os.listdir(Paths.FINAL_DATA_PATH)) == len(SITES_FROM_ARCHIVE_SITE_INFO_FINAL)):
        print('==> All File Are Accounted For.')
    else:
        print("Number of files physically available ==> ", len(os.listdir(Paths.FINAL_DATA_PATH)))
        print("Number of files in sites list        ==> ", len(SITES_FROM_ARCHIVE_SITE_INFO_FINAL))
        print('')
    
    