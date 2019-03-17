import ipdata

titties = "tits"

def searchDB(MongoConfig, IP):
	print("Searching local MongoDB")

#mongodb stuff
	
def searchAPI(config, IP):
	print("Searching API with config: " + str(config.API_KEY))

def retrieve(config, IP):
	print("Searching DB, then API, returning the IP record.")

class config():
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