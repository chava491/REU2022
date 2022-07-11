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