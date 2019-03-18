#!/usr/bin/python3
import datetime
import pymongo
from ipdata import ipdata

# ip_data structure:
# IP Address, Last Ban, Ban Count, City, Region, Country, Organization, Flag, Threat

def search(IPAddress):
	print("Searching for " + str(IPAddress) +"")


#try:
#	mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
	
