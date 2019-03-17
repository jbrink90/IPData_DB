#!/usr/bin/python3
#import ipdata_db
import ipdata_db

ipdata_config = ipdata_db.config()
ipdata_config.setup("127.0.0.1", 27017, "", "", "SOMEKEY")

ipdata_db.search(ipdata_config, "192.168.1.1")



# ip_data structure:
# IP Address, Last Ban, Ban Count, City, Region, Country, Organization, Flag, Threat

input('Press ENTER to exit')
#try:
#	mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
	
