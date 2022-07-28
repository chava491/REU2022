#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 22:09:09 2022

Author: salvadorguel
Mentor: Dr. Anthony Parolari
Date: Summer 2022
Universtiy: Marquette University
Project: Summer Research Experience for Undergraduates (REU). Focusing on Hardware, Embedded Software, and Analytics for Environment Quality Monitoring
Description: This script contains all the functions that goes into the SiteInfoFinal.txt in reuriverdata to give us the desired array with avilable site parameters
"""
import Paths


# Note that all these function go to the file SiteInfoFinal.txt to look up these dates. To test that everything is
# working properly run testcases

def getsites():
    sites = []
    with open(Paths.SITE_INFO_FINAL_PATH, 'r') as f:
        lines = f.readlines()
        for l in lines[0:]:
            sites.append(l.split('\t')[0])
    return sites

def getbegindates():
    begindates = []
    with open(Paths.SITE_INFO_FINAL_PATH, 'r') as f:
        lines = f.readlines()
        for l in lines[0:]:
            begindates.append(l.split('\t')[1])
    return begindates

def getenddates():
    enddates = []
    with open(Paths.SITE_INFO_FINAL_PATH, 'r') as f:
        lines = f.readlines()
        for l in lines[0:]:
            enddates.append(l.split('\t')[2])
    return enddates

def latitudes():
    latitudes = []
    with open(Paths.SITE_INFO_FINAL_PATH, 'r') as f:
        lines = f.readlines()
        for l in lines[0:]:
            latitudes.append(l.split('\t')[3])
    return latitudes

def longitudes():
    longitudes = []
    with open(Paths.SITE_INFO_FINAL_PATH, 'r') as f:
        lines = f.readlines()
        for l in lines[0:]:
            longitudes.append(l.split('\t')[4])   
    return [x[:-1] for x in longitudes] # We need to do this because this array is '#\n'. Thus, by adding the 
                                        # [x[:-1] for x in ARRAYNAME] we just keep the # and not the \n character
def getfailedsites():
    failedsites = []
    with open(Paths.FAILED_SITES_TXT_PATH, 'r') as f:
        lines = f.readlines()
        for l in lines[0:]:
            failedsites.append(l.split('\t')[0])
            #print(failedsites)
    return failedsites