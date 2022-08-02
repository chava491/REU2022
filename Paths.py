#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 01:15:26 2022

Author: salvadorguel
Mentor: Dr. Anthony Parolari
Date: Summer 2022
Universtiy: Marquette University
Project: Summer Research Experience for Undergraduates (REU). Focusing on Hardware, Embedded Software, and Analytics for Environment Quality Monitoring
Description: This script contains all the filepaths and parts of filepaths that are used throughout the entirety of the program to access all the saved media on the harddrive.
"""

#%%##################################################################################
# File Path for where the stripped text file containing all of the bare info        #
# conatining the initial list of site numbers based off of the URLs (the first ones #
# ever created when update archive is ran ) from the State Codes goes               #
#####################################################################################

OTUPUT_FILE_PATH = '/Volumes/SeagateBackupPlusDrive/reuriverdata/temp/stripped/tempstatecodegrab.txt'

#%%##################################################################################
# File Path for tempstatecodegrab.txt (thus this is the non-stripped one)           #
#####################################################################################

TEMP_STATE_CODE_GRABBED_PATH = '/Volumes/SeagateBackupPlusDrive/reuriverdata/temp/tempstatecodegrab.txt'

#%%##################################################################################
# File Path parts for where to save an array to a the temp folder in the reudata    #
# file. Thus, path/<filenamewanted>.txt (file looks like [#, #, ... , #])           #
#####################################################################################

PATH = '/Volumes/SeagateBackupPlusDrive/reuriverdata/temp/'

#%%##################################################################################
# File Path parts for where to save an array line by line and not just as is        #
#####################################################################################

SUCCESSFUL_PATH = '/Volumes/SeagateBackupPlusDrive/reuriverdata/lists/successful/'
SUCCESSFUL_SITES_TXT_PATH = '/Volumes/SeagateBackupPlusDrive/reuriverdata/lists/successful/successfulsites.txt'
FAILED_SITES_TXT_PATH = '/Volumes/SeagateBackupPlusDrive/reuriverdata/lists/failed/failedsites.txt'
FAILED_PATH = '/Volumes/SeagateBackupPlusDrive/reuriverdata/lists/failed/'
STATE_CODE_URLS_PATH = '/Volumes/SeagateBackupPlusDrive/reuriverdata/lists/StateCodeURLs/'

#%%##################################################################################
# File Path parts for where I save SiteInfoDraft.txt and SiteInfoFinal.txt          #
#####################################################################################

SITE_INFOS_PATH = '/Volumes/SeagateBackupPlusDrive/reuriverdata/lists/'
SITE_INFO_DRAFT_PATH = '/Volumes/SeagateBackupPlusDrive/reuriverdata/lists/SiteInfoDraft'
SITE_INFO_FINAL_PATH =  '/Volumes/SeagateBackupPlusDrive/reuriverdata/lists/SiteInfoFinal.txt'

#%%##################################################################################
# File Path part for middleman -> This file is for the inbetween to the stripped    #
# txt file that will be the raw data in the reuriverdata/data folder which is       #
# called FINAL-DATA-PATH                                                            #
#####################################################################################

MIDDLEMAN_PATH = '/Volumes/SeagateBackupPlusDrive/reuriverdata/temp/middleman'
FINAL_DATA_PATH = '/Volumes/SeagateBackupPlusDrive/reuriverdata/data/'

#%%##################################################################################
# File Path to the HeatMaps Save Location                                           #
#####################################################################################

FULL_PATH_HEATPMAP_NAME = '/Volumes/SeagateBackupPlusDrive/reuriverdata/Graphs/Heatmaps/SITE_Maximum_Temperatures_Heatmap.html'
FULL_PATH_HEATPMAP_NAME_POPUPS = '/Volumes/SeagateBackupPlusDrive/reuriverdata/Graphs/Heatmaps/SITE_Maximum_Temperatures_Heatmap_Popups.html'

#%%##################################################################################
# Full file path for the TimeSeries Grouped Bar Graph                               #
#####################################################################################

FULL_PATH_GROUPED_BAR_GRAPH ='/Volumes/SeagateBackupPlusDrive/reuriverdata/Graphs/TimeSeriesLengthsGraphGrouped'

#%%##################################################################################
# Full file path fow where all the raw data textfiles are                            #
#####################################################################################

REU_DATA_PATH = '/Volumes/SeagateBackupPlusDrive/reuriverdata/data/'
FULL_PATH_COLOR_MAP_AVERAGE = '/Volumes/SeagateBackupPlusDrive/reuriverdata/Graphs/ColorMaps/Color_Map_Averages.png'
FULL_PATH_COLOR_MAP_VARIANCES = '/Volumes/SeagateBackupPlusDrive/reuriverdata/Graphs/ColorMaps/Color_Map_Variances.png'