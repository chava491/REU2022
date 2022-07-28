#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: salvadorguel
Mentor: Dr. Anthony Parolari
Date: Summer 2022
Universtiy: Marquette University
Project: Summer Research Experience for Undergraduates (REU). Focusing on Hardware, Embedded Software, and Analytics for Environment Quality Monitoring
Description:
    a) This program, is simply a URL that displays all of the sites with their begin and end dates that measure temperature.
    
Side Note:
    wqEntire = url that displays all of the sites with their begin and end dates that measure temperature.
"""

FIPSTATECODES = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
    
    # Please note that there are more FIP codes. However, this array only has 52 due to the following not working 
    #   (even when manually looked up at https://waterservices.usgs.gov/rest/Site-Test-Tool.html):
    #  ________________________________________
    # |_______'STATE'_________________|__CODE__|
    # |American Samoa_________________|___AQ___|
    # |Canton and Enderbury Islands___|___62___|
    # |Guam___________________________|___GU___|
    # |Johnston Atoll_________________|___67___|
    # |Midway Islands_________________|___71___|
    # |Northern Mariana Islands_______|___MP___|
    # |Ryukyu Islands, Southern_______|___73___|
    # |Swan Islands___________________|___74___|
    # |Trust Territories______________|___75___|
    # |U.S. Misc Carribean____________|___76___|
    # |U.S. Misc Pacific Islands______|___77___|
    # |Wake Island____________________|___79___|
    
"""
The following will be a list of all URLs that must be changed if USGS changes its URL structure.
"""

# 1) HFUNCS.py ####################################################################
###################################################################################
# URL parts for site download for the first time that has all the temperatures ####
###################################################################################

URL_A = 'https://nwis.waterdata.usgs.gov/nwis/uv?cb_00010=on&format=rdb&site_no='  #1st part
# SITENO is 2nd part
URL_B = '&period=&begin_date=' # 3rd part  
# BEGINDATE is the 3rd part
URL_C = '&end_date='
#ENDDATE is the 5th part

#####################################################################################
# URL parts for when we compile the initial URLs made of State Codes to get all the #
# sites that are available. The 00010 paramter sites will get filtered out due to   #
# those being the continuous timeseries of water temperature (the ones we want).    #
#####################################################################################

GET_SITES_BOOT_URLA = 'https://waterservices.usgs.gov/nwis/site/?format=rdb&stateCd='
GET_SITES_BOOT_URLC = '&seriesCatalogOutput=true&outputDataTypeCd=iv&parameterCd=00010&siteType=ST&siteStatus=all&hasDataTypeCd=iv'