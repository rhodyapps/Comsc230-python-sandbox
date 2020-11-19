#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 21:09:54 2020

@author: tnewman

Description: 
    This program takes a json input file staff.json (exported from a MySql database) and 
    prints out the keys.


"""

import json, ast


# Some test json data for debugging. 
# Note JSON uses double quotes for both keys and values, ie: "type": "1"
# wheras a javascript object does not have quotes around the keys, 
#  for example:  var testObject = {one: 1,"two":2,"three":3};

input_json = """
[
    {
        "type": "1",
        "name": "name 1"
    },
    {
        "type": "2",
        "name": "name 2"
    },
    {
        "type": "1",
        "name": "name 3"
    }
]"""
# Exercise: 
# Use json-reader.py to read json files from the 'northwind' SQL database:
# Step 1: Use XAMPP to export files in JSON format from the 'northwind' database
# Step 2: Copy the downloaded files into a 'DataFiles' folder in your project
# Step 3: get the path to the DataFiles folder into your clipboard
#  paste it into the 'folderPath' variable, (remove the filename if it is at the end of the path)
# Step 4: Initialize the 'fileName' variable with the filename.
# Step 5: Run the program using VS Code 'Run File in Terminal' (right click on filename).

fileName= 'employees.json'

#folderPath = '/Users/tnewman/Documents/GitHub/RWU/Comsc230/Examples/Python/DataFiles/'
folderPath = '/Users/tomnewman/Documents/GitHub/RWU/RWU230-Projects/mongo-projects/Comsc230-python-sandbox/DataFiles'

filePath = folderPath+'/'+fileName

####  Open and read the raw data from the JSON file
        
with open(filePath, 'r') as f:      # In python we use the 'with' instruction to ensure that resources 
      str1 = f.readlines()           # are opened and closed within the context in which they are used.

      print("number of records: ", len(str1))
        
for i in range(len(str1)):
    data = ast.literal_eval(str1)
   # data = str1[i]
    print ('Retrieved',len(data),'characters')
    print(data)
    
    for key in data.keys(): print(key)
    
   

