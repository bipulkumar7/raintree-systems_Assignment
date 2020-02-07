"""
File name - ComputerNames.py
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


2nd step:

Get the  computer names from   given date range of log files.
i.e 1 months from 01-01-2012 to 31-01-2012

20120101.log     20120106.log     20120113.log        20120119.log        20120125.log
20120102.log     20120109.log     20120115.log        20120120.log        20120126.log
20120103.log     20120110.log     20120116.log        20120122.log        20120127.log
20120104.log     20120111.log     20120117.log        20120123.log        20120130.log
20120105.log 	 20120112.log 	  20120118.log  	  20120124.log  	  20120131.log
"""
import re
from functools import reduce
from logfileName import commute_list

ComputerNames = []
path = '/root/raintree/H--RAINTREE-PARKER94-/{}'

def open_file(i,ComputerNames):
    """
    This method opens all the list of files and match every line with regex & then create a list.
    After that it call another function get_computers_name using a list as parameter.
    """
    with open(path.format(i),"rt") as f:
    
        for i in f:
            x = re.findall("e\:[A-Z0-9-]+", i)
            ComputerNames.append(x)
    
        ComputerNames = reduce(lambda x,y:x+y, list(filter(None,ComputerNames)))
    
    return get_computers_name(ComputerNames)

def get_computers_name(x):
    """
    This method sort the list of computer names and then return the list of it.
    """
    list2 = lambda x:list(set(x))
    x = list2(x)
    
    return x

def Data_cleansing(x):
     return lambda x: x[2:]  

def findingComputersNames():
    """
    This function call commute_list of logfileName.py module, then call nested function open_file
    and iterate using return values by calling Data_clransing function
    """
    for i in commute_list:
        x = open_file(i,ComputerNames)

        y = x
    ComputerNames.clear()
    for i in y:
        x = Data_cleansing(i)
        ComputerNames.append(x(i))
    return ComputerNames

ComputerNames = findingComputersNames()
#print(ComputerNames)
