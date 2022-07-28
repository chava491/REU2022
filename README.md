# Anthropogenic impacts on stream temperature regimes and extremes from time-series analysis (REU PROGRAM 2022)
Authors: Salvador Guel and Dr. Anthony Parolari

Description (As of 7/27/22):
  1) The following code is able to download a tab-seperated file from the internet. It then checks to make sure that the download was correct and then saves that to a file. This file is read, but all the lines that do not matter are deleted. Thus, we read in the needed data into a seperate file to then be able to extract the data back into python as arrays and variables that can be directly refered to.
  2) Please note that the following is required for the program to work:
     
     a) connected volume (harddrive with minimum of 35 GB available)
     
  3) The following is the file structure that this program will create and fill for you
  
     a) reuriverdata
     
     b) reuriverdata/Graphs -> Contains the two graphs that show us the period length in days of all the sites. One of them is a bar graph and the other is a scatter plot; they represent the (site v site length in days) and (range of site length in days v. number of sites)
     c) reuriverdata/Graphs/Heatmaps -> This contains the heatmaps of the average, minimum, and maximum temperatures of every site. There will be two for each; one being that of just the heatmap and the second one also including the heatmap and the respective sites where they came from.
     d) reuriverdata/data -> This houses all of the raw data for each site and their temperatures. Aka the archive.
     e) reuriverdata/lists
     f) reuriverdata/lists/failed
     g) reuriverdata/lists/successful
     h) reuriverdata/temp
     i) reuriverdata/temp/stripped
