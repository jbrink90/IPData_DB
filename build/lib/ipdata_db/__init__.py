import requests
from requests import exceptions
import json
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from pymongo.errors import OperationFailure

def searchDB(IP, configuration):
	url = str(configuration.MONGO_URL)
	port = str(configuration.MONGO_PORT)
	user = str(configuration.MONGO_USER)
	passwd = str(configuration.MONGO_PASS)
	db = str(configuration.MONGO_DB)
	collection = str(configuration.MONGO_COLLECTION)

	mongoClient = ""
	mongo_db = ""

	try:
		mongoClient = MongoClient("mongodb://" + url + ":" + port + "/", username=user, password=passwd)
		mongo_db = mongoClient[db]
		if (user):
			mongo_db.authenticate(user, passwd)
			
		if (collection not in mongo_db.list_collection_names()):
			debug("Could not find " + collection + " in " + db)
			return False
		
		collection_ips = mongo_db[collection]
		data_count = collection_ips.count({"_id":IP})
		
		if (data_count < 1):
			debug(IP + " not found in IPDB")
			return False
		if (data_count > 1):
			debug(str(data_count) + " records found. Only returning one.")
		
		data_found = collection_ips.find_one({"_id":IP})
		
		mongoClient.close()
		return data_found
		
	except ConnectionFailure:
		debug("ConnectionFailure!")
		return False
	except OperationFailure:
		debug("Authentication failed.")
		return False
	except:
		debug("Could not connect to " + url)
		return False

def searchAPI(IP, configuration):
	try:
		request_url = "https://api.ipdata.co/"+str(IP)+"?api-key="+configuration.API_KEY
		api_request = requests.get(request_url)
	except Timeout:
		debug("Timeout reached while making API call")
		return False
	except ConnectionError:
		debug("ConnectionError thrown while making API call")
		return False
	except:
		debug("Other error while making API call")
		return False
	
	if ('application/json' in str(api_request.headers.get('content-type'))):
		mongoClient = MongoClient("mongodb://" + str(configuration.MONGO_URL) + ":" + str(configuration.MONGO_PORT) + "/", username=str(configuration.MONGO_USER), password=str(configuration.MONGO_PASS))
		mongo_db = mongoClient[str(configuration.MONGO_DB)]
		
		if (configuration.MONGO_USER):
			mongo_db.authenticate(str(configuration.MONGO_USER), str(configuration.MONGO_PASS))
		
		collection_ips = mongo_db[str(configuration.MONGO_COLLECTION)]
		data_count = collection_ips.count({"_id":str(IP)})
		
		if (data_count < 1):
			# Add it to IPDB
			row = {
				"_id": IP,
				"ipdata": api_request.json()
			}
			try:
				collection_ips.insert_one(row)
			except ConnectionFailure:
				debug("Connection failure while storing IP data in IPDB.")
				return False
			except OperationFailure:
				debug("Authentication failure while storing IP data in IPDDB.")
				return False
			except:
				debug("Could not connect to MongoDB")
				return False
			
		return api_request.json()
	else:
		return api_request.text()
	
	return False
		

def retrieve(IP, configuration):
	info("Searching DB, then API, returning the IP record.")
	
	url = str(configuration.MONGO_URL)
	port = str(configuration.MONGO_PORT)
	user = str(configuration.MONGO_USER)
	passwd = str(configuration.MONGO_PASS)
	db = str(configuration.MONGO_DB)
	collection = str(configuration.MONGO_COLLECTION)

	mongoClient = ""
	mongo_db = ""

	try:
		mongoClient = MongoClient("mongodb://" + url + ":" + port + "/", username=user, password=passwd)
		mongo_db = mongoClient[db]
		if (user):
			mongo_db.authenticate(user, passwd)
		
		collection_ips = mongo_db[collection]
		data_count = collection_ips.count({"_id":IP})
		data_found = False
		
		
		
		if (data_count < 1):
			debug(IP + " not found in IPDB")
			# search the API
			data_found = searchAPI(IP, configuration)
			
		elif (data_count > 1):
			debug(str(data_count) + " records found. Only returning one.")
			data_found = collection_ips.find_one({"_id":IP})
		
		elif (data_count == 1):
			info("(retrieve) successful)
			data_found = collection_ips.find_one({"_id":IP})
		
		mongoClient.close()
		return data_found
		
	except ConnectionFailure:
		debug("ConnectionFailure!")
		return False
	except OperationFailure:
		debug("Authentication failed.")
		return False
	except:
		debug("Could not connect to " + url)
		return False

class config:
	MONGO_URL = ""
	MONGO_PORT = ""
	MONGO_USER = ""
	MONGO_PASS = ""
	MONGO_DB = ""
	MONGO_COLLECTION = ""
	API_KEY = ""
	DEBUG = ""

	def __init__(self, mongo_url, mongo_port, mongo_user, mongo_passwd, mongo_db, mongo_collection, ipdata_api_key, debug=False):
		self.MONGO_URL = mongo_url
		self.MONGO_PORT = mongo_port
		self.MONGO_USER = mongo_user
		self.MONGO_PASS = mongo_passwd
		self.MONGO_DB = mongo_db
		self.MONGO_COLLECTION = mongo_collection
		self.API_KEY = ipdata_api_key
		self.DEBUG = debug