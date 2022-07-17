#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 01:53:36 2022

@author: salvadorguel
"""
import requests
from HFuncs import * # Imports all of the functions I defined in HFuncs
import os

SITE_INFO_PATH = '/Volumes/SeagateBackupPlusDrive/reuriverdata/lists/SiteInfoFinal.txt'
SAVE_LOCATION_LATITUDE = '/Volumes/SeagateBackupPlusDrive/reuriverdata/temp/templatitude.txt'
SAVE_LOCATION_LONGITUDE = '/Volumes/SeagateBackupPlusDrive/reuriverdata/temp/templongitude.txt'

def average2DGradient():
    #Need to check how to pass in an array as an arguement
    print("2D Gradiant Successful \n \n")

def getsites():
    sites = []
    with open(SITE_INFO_PATH, 'r') as f:
        lines = f.readlines()
        for l in lines[1:]:
            sites.append(l.split()[1])
    return sites

def getbegindates():
    begindates = []
    with open(SITE_INFO_PATH, 'r') as f:
        lines = f.readlines()
        for l in lines[1:]:
            begindates.append(l.split()[1])
    return begindates
      
def getenddates():
    enddates = []
    with open(SITE_INFO_PATH, 'r') as f:
        lines = f.readlines()
        for l in lines[1:]:
            enddates.append(l.split()[1])
    return enddates

def obtainlatitude(siteno):
    urla = 'https://waterdata.usgs.gov/nwis/uv?referred_module=qw&search_site_no='
    # sitno goes here (aka when URL is put together)
    urlb = '&search_site_no_match_type=exact&index_pmcode_00010=1&index_pmcode_91110=1&index_pmcode_91111=1&group_key=NONE&format=sitefile_output&sitefile_output_format=rdb&column_name=agency_cd&column_name=dec_lat_va&column_name=dec_long_va&range_selection=days&period=7&rdb_compression=file&list_of_search_criteria=search_site_no%2Crealtime_parameter_selection'
    URL = urla + siteno + urlb
    response = requests.get(URL)     # Getting content from the URL we are currently on.
    if (CheckRequest(response.status_code) == "Success"):                                   # Here we check that the URL was indeed valid and we got something back.)
        with open(SAVE_LOCATION_LATITUDE, 'wb') as f:
               f.write(response.content)
        with open(SAVE_LOCATION_LATITUDE, "r") as temp:
            lines = temp.readlines()
            for l in lines[1:]:
                if (l.startswith('USGS')):
                    latitude = l.split()[1]
    return latitude
            
def obtainlongitude(siteno):
    urla = 'https://waterdata.usgs.gov/nwis/uv?referred_module=qw&search_site_no='
    # sitno goes here (aka when URL is put together)
    urlb = '&search_site_no_match_type=exact&index_pmcode_00010=1&index_pmcode_91110=1&index_pmcode_91111=1&group_key=NONE&format=sitefile_output&sitefile_output_format=rdb&column_name=agency_cd&column_name=dec_lat_va&column_name=dec_long_va&range_selection=days&period=7&rdb_compression=file&list_of_search_criteria=search_site_no%2Crealtime_parameter_selection'
    URL = urla + siteno + urlb
    response = requests.get(URL)  # Getting content from the URL we are currently on.
    if (CheckRequest(response.status_code) == "Success"):                                   # Here we check that the URL was indeed valid and we got something back.)
        with open(SAVE_LOCATION_LONGITUDE, 'wb') as f:
            f.write(response.content)
        with open(SAVE_LOCATION_LONGITUDE, "r") as temp:
            lines = temp.readlines()
            for l in lines[1:]:
                if (l.startswith('USGS')):
                    longitude = l.split('\t')[2] # This is saying (from left to right) we are getting the item in the 3rd column of the current line     
    return longitude
