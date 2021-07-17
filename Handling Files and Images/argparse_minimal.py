# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 15:44:52 2021

@author: Rakesh Kumar
"""

# Import the required packages 
import argparse 
# We first create the ArgumentParser object 
# The created object 'parser' will have the necessary information 
# to parse the command-line arguments into data types. 
parser = argparse.ArgumentParser() 
# The information about program arguments is stored in 'parser' and used when parse_args() is called. 
# ArgumentParser parses arguments through the parse_args() method: 
parser.parse_args()