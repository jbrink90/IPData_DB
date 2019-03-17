




url = ""
port = ""
user = ""
passwd = ""
api_key = ""

def setup(mongo_url, mongo_port, mongo_user, mongo_passwd, ipdata_api_key):
	url = mongo_url
	port = mongo_port
	user = mongo_user
	passwd = mongo_passwd
	api_key = ipdata_api_key

def list():
	print("url = '" + str(url) + "'")
	print("port = '" + str(port) + "'")
	print("user = '" + str(user) + "'")
	print("passwd = '" + str(passwd) + "'")
	print("api_key = '" + str(api_key) + "'")