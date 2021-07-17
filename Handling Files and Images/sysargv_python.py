# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 15:35:10 2021

@author: Rakesh Kumar
"""

import sys

# We will print some information in connection with sys.argv to see how it works: 
print("The name of the script being processed is: '{}'".format(sys.argv[0])) 
print("The number of arguments of the script is: '{}'".format(len(sys.argv))) 
print("The arguments of the script are: '{}'".format(str(sys.argv)))