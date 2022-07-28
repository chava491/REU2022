#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 16:22:51 2022

Author: salvadorguel
Mentor: Dr. Anthony Parolari
Date: Summer 2022
Universtiy: Marquette University
Project: Summer Research Experience for Undergraduates (REU). Focusing on Hardware, Embedded Software, and Analytics for Environment Quality Monitoring
Description: This script is what will be run. It will give you available options. Please note that it is designed to work with a commented volume such as a usb drive with
at least 35 GB on it available for this program to use.
"""

import testcases

import reu2022urldownload as data
import REU2022stats as statsreu
import ObtainInfoFromArchive as OIFA
import numpy as npy

# Global Variables 
# Note: That from here to mark 1AE
SITE_NOS = OIFA.getsites()
SITE_BEGIN_DATES = OIFA.getbegindates()
SITE_END_DATES = OIFA.getenddates()
SITE_LATITUDES = OIFA.latitudes()
SITE_LONGITUDES = OIFA.longitudes()
# 1AE: Comment out to run option 0 if running for the first time

while True:
    print('----------------------------------------------------------')
    print('Please note updating the archived data may take a while')
    print('Options:')
    print('0: Update Data')
    print('1: Graph Lengths Of Timeseries Data')
    print('2: Generate 2D Heat Maps')
    print('TC: Run Testcases and Checks ')
    print('e: Exit')
    choice = input("What would you like to do? \n")
    
    if (choice == '0'):
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        verificated = False
        
        while (verificated == False):
            choicev = input("Are you sure? [y/n] \n")
            
            if ((choicev == 'y') or (choice == 'Y')):
                data.updatedata()
                verificated = True
            elif (choicev == 'n' or (choice == 'N')):
                print('-------- Session end -------- \n \n')
                verificated = True
            else:
                print('Invalid Option. Try Again')
    elif (choice == '1'):
        verification = False
        while (verification == False):
            period = input('What Period Would you like to view these graphs in? \n')
            if(period.isnumeric()):
                period = int(period) #Must convert period input from string to integer
                no_days_array = statsreu.graphlengthsoftimeseries(SITE_BEGIN_DATES, SITE_END_DATES)
                statsreu.graphlengthsofgroupedtimeseries(SITE_BEGIN_DATES, SITE_END_DATES, period)
                verification = True
            else:
                print('Invalid Option. Try Again')
        # The above line will graph the lengths of each site's days of operation.
        # One point for each site
        
        # The above line will graph the lengths of each site's days grouped in 100s
        # points for each threshhold of 100.
    elif (choice == '2'):
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        # Convert String arrays to float arrays to not have to worry about it later (Except SITE_NOS)
        array_to_float = npy.array(SITE_LATITUDES)
        array_to_float_2 = npy.array(SITE_LONGITUDES)
        SITE_LATITUDES_AS_FLOATS = array_to_float.astype(float)
        SITE_LONGITUDES_AS_FLOATS = array_to_float_2.astype(float)
        # Call to function that will do all the work to produce the heat map we desire
        statsreu.average2DGradient(SITE_LATITUDES_AS_FLOATS, SITE_LONGITUDES_AS_FLOATS)
    elif (choice == 'TC'):
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        testcases.TestAllFilesListedAreDownloaded()()
    elif ((choice == 'e') or (choice == 'E')):
        break
    else:
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        print('Invalid Option. Try Again')