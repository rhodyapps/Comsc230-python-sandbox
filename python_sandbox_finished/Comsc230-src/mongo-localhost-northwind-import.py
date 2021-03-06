import json, os, sys, pymongo

from pymongo import MongoClient 

# Making Connection 
myclient = MongoClient("mongodb://localhost:27017/") 

# database 
db = myclient["northwind"] 

# Path to data file
fileName= 'employees.json'
folderPath = os.getcwd()
print("folderPath: ", folderPath) # print path for debugging

filePath = folderPath+'/DataFiles/'+fileName

# Created or Switched to collection 

Collection = db["employees"] 

# Loading or Opening the json file 
with open(filePath) as file: 
	file_data = json.load(file) 
	
# Inserting the loaded data in the Collection 
# if JSON contains data more than one entry 
# insert_many is used else inser_one is used 
if isinstance(file_data, list): 
	Collection.insert_many(file_data) 
else: 
	Collection.insert_one(file_data) 
