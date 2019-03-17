#!/usr/bin/python3
import ipdata_db

our_config = ipdata_db.config("127.0.0.1", 27017, "", "", "fail2ban_gui", "ip_data", "f69b1b9f98221cac40792d3521b92b4a67d1c340d53ad8a085b2511b")
api_results = ipdata_db.retrieve("201.239.58.78", our_config)
print(api_results)

what = input('Press ENTER to exit')
#try:
#	mongoClient = pymongo.MongoClient("mongodb://localhost:27017/")

