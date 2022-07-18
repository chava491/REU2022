#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 16:22:51 2022

@author: salvadorguel
"""

import reu2022urldownload as data
import REU2022stats as statsreu
# Global Variables
SITE_NOS = statsreu.getsites()
SITE_BEGIN_DATES = statsreu.getbegindates()
SITE_END_DATES = statsreu.getenddates()
SITE_LATITUDES = statsreu.latitudes()
SITE_LONGITUDES = statsreu.longitudes()

while True:
    print('Please note updating the archived data may take a while')
    print('Options:')
    print('0: Update Data')
    print('1: Graph Lengths Of Timeseries Data')
    print('2: MAPPED 2D GRADIENT')
    print('3: TBD')
    choice = input("What would you like to do? \n")
    
    if (choice == '0'):
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
        no_days_array = statsreu.graphlengthsoftimeseries(SITE_BEGIN_DATES, SITE_END_DATES)
    elif (choice == '2'):
        statsreu.average2DGradient()
    elif (choice == '3'):
        print('TBD')
    else:
        print('Invalid Option. Try Again')
        
