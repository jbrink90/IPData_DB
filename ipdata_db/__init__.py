import ipdata
import pymongo

def searchDB(IP, configuration):
	url = str(configuration.MONGO_URL)
	port = str(configuration.MONGO_PORT)
	user = str(configuration.MONGO_USER)
	passwd = str(configuration.MONGO_PASS)

	login_string = user + ":" + passwd + "@"

	if (len(login_string) == 2):
		login_string = ""

	try:
		mongoClient = pymongo.MongoClient("mongodb://" + login_string + url + ":" + port+ "/")
		print("Mongo client connected!")
	except ConnectionFailure:
		print("ConnectionFailure!")
	except:
		raise Exception("Could not connect to " + url)
		
	mongoClient.close()

def searchAPI(IP, configuration):
	return ("Searching API with config: " + str(configuration.API_KEY))

def retrieve(IP, configuration):
	print("Searching DB, then API, returning the IP record.")

class config:
	MONGO_URL = ""
	MONGO_PORT = ""
	MONGO_USER = ""
	MONGO_PASS = ""
	API_KEY = ""

	def __init__(self):
		print("Config alive")
		
	def setup(self, mongo_url, mongo_port, mongo_user, mongo_passwd, ipdata_api_key):
		self.MONGO_URL = mongo_url
		self.MONGO_PORT = mongo_port
		self.MONGO_USER = mongo_user
		self.MONGO_PASS = mongo_passwd
		self.API_KEY = ipdata_api_key
		print("Config setup")