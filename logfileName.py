"""
File name - logfileName.py
Author - Bipul kumar
Email - bipulkumar@nwtime.org | bipul.opensource@gmail.com
Licensed under GPLv3 
============================
Computer Name, No. of client Disconnects for that computer name in that date range in descending order
Report will look like :
Date : 01-01-2012 to 31-01-2012

Computer Name Number of Disconnects
Person A Laptop 34
Person B Laptop 23
Computer Name Number of Drops
Person A Laptop 110


1st step:

Get the  solution for finding  given date range of log files.
i.e 1 months from 01-01-2012 to 31-01-2012

20120101.log     20120106.log     20120113.log        20120119.log        20120125.log
20120102.log     20120109.log     20120115.log        20120120.log        20120126.log
20120103.log     20120110.log     20120116.log        20120122.log        20120127.log
20120104.log     20120111.log     20120117.log        20120123.log        20120130.log
20120105.log 	 20120112.log 	  20120118.log        20120124.log  	  20120131.log
"""
import os
import re
from functools import reduce
from os import listdir
from os.path import isfile, join

# Defining the path of log files get downloaded.
path = '/root/raintree/H--RAINTREE-PARKER94-'

commute_list = [] # Defning the empty list.

def Data_cleansing(commute_list):
    return reduce(lambda x,y:x+y, list(filter(None,commute_list)))

def  get_commute_list(func, path,commute_list):
    """
    This function return commute_list(list of items) i.e log file filtered name from the specified path.
    Then call a another function Data_cleansing for detecting and correcting (or removing) corrupt or 
    inaccurate records from a given list.
    """
                    # Regular list comprehensions to list of all files in logfile_list
    logfiles_list = [ name for name in os.listdir(path) if os.path.isfile(join(path, name))]
    """
    For loop to iterate & match each line using regex expression & append into commute_list
    """
    for lines in logfiles_list:
            matched_items = re.findall("201201[0-9]{2}\.log", lines)
            commute_list.append(matched_items)      
   
    
    return  func(commute_list)
def report(x):
    x = [ i[:-4] for i in x ]
    x.sort(reverse=False)
    start = x[0]
    end = x[-1]
    print("Date : "+start[-2:]+"-"+start[-4:-2]+"-"+start[:4] + " to " + end[-2:]+"-"+end[-4:-2]+"-"+end[:4])

commute_list = get_commute_list(Data_cleansing, path, commute_list)
#commute_list
#report(commute_list)
