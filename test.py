#!/usr/bin/python3
import ipdata_db

our_config = ipdata_db.config()
our_config.setup("127.0.0.1", 27017, "user", "pass", "SOMEKEY")

api_results = ipdata_db.searchDB("127.9.9.2", our_config)
print(api_results)



# ip_data structure:
# IP Address, Last Ban, Ban Count, City, Region, Country, Organization, Flag, Threat

what = raw_input('Press ENTER to exit')
#try:
#	mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")

