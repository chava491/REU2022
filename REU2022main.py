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

print(SITE_NOS[0])
print(SITE_BEGIN_DATES[0])
print(SITE_END_DATES[0])
print(SITE_LATITUDES[0])
print(SITE_LONGITUDES[0])

while False:
    print('Please note updating the archived data may take a while')
    print('Options:')
    print('0: Update Data')
    print('1: MAPPED 2D GRADIENT')
    print('2: TBD')
    choice = input("What would you like to do? \n")
    
    if (choice == '0'):
        verificated = False
        
        while (verificated == False):
            choicev = input("Are you sure? [y/n] \n")
            
            if (choicev == 'y'):
                data.updatedata()
                verificated = True
            elif (choicev == 'n'):
                print('-------- Session end -------- \n \n')
                verificated = True
            else:
                print('Invalid Option. Try Again')
    elif (choice == '1'):
        statsreu.average2DGradient()
    elif (choice == '2'):
        print('TBD')
    else:
        print('Invalid Option. Try Again')
        
