"""
SCRIPT 3
File name - report.py
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


3rd step:

Get the Computer Name, No. of client Disconnects for that computer name in that date range in descending order
i.e 1 months from 01-01-2012 to 31-01-2012

20120101.log     20120106.log     20120113.log        20120119.log        20120125.log
20120102.log     20120109.log     20120115.log        20120120.log        20120126.log
20120103.log     20120110.log     20120116.log        20120122.log        20120127.log
20120104.log     20120111.log     20120117.log        20120123.log        20120130.log
20120105.log 	 20120112.log 	  20120118.log  	  20120124.log  	  20120131.log
"""
import re
from ComputerNames import ComputerNames
from logfileName import commute_list , report

path = '/root/raintree/H--RAINTREE-PARKER94-/{}'
count = 0

def computer_disconnected(ComputerNames, commute_list, count):
    
    dicts = {}
    for i in ComputerNames:
        for j in commute_list: 
            with open(path.format(j),"rt") as f:
                for k in f:
                    x = re.findall("{}.+disconnected".format(i),k)
                    if len(x) > 0:
                        count = count + 1 
        
                dicts[i] = dicts.get(i, 0) + count
                count = 0 
    return dicts
dicts = computer_disconnected(ComputerNames, commute_list, count)
report(commute_list)
print("\nComputer Name Number of Disconnects")
dicts_sorted_keys = sorted(dicts, key=dicts.get, reverse=False)
for r in dicts_sorted_keys:
    print(r, dicts[r])
