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
    
    # Please note that there are more FIP codes. However, this array only has 52 due to the following not working (even when manually looked up at https://waterservices.usgs.gov/rest/Site-Test-Tool.html):
    # _______'STATE'_________________|___CODE___|
    # American Samoa                 |    AQ    |
    # Canton and Enderbury Islands   |    62    |
    # Guam                           |    GU    |
    # Johnston Atoll                 |    67    |
    # Midway Islands                 |    71    |
    # Northern Mariana Islands       |    MP    |
    # Ryukyu Islands, Southern       |    73    |
    # Swan Islands                   |    74    |
    # Trust Territories              |    75    |
    # U.S. Misc Carribean            |    76    |
    # U.S. Misc Pacific Islands      |    77    |
    # Wake Island                    |    79    |
    
wqEntire = 'https://waterdata.usgs.gov/nwis/dv?referred_module=qw&index_pmcode_00010=1&group_key=NONE&format=sitefile_output&sitefile_output_format=rdb&column_name=agency_cd&column_name=site_no&column_name=qw_begin_date&column_name=qw_end_date&range_selection=days&period=365&begin_date=2021-06-27&end_date=2022-06-26&date_format=MM-DD-YYYY&rdb_compression=file&list_of_search_criteria=realtime_parameter_selection'
