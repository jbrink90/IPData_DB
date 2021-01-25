
# IPData_DB
A Python package used to store a local cache of IP address entries in a Mongo database to prevent overextending your monthly IPData.co API quota. **Note**: This program was written to fit the developer's needs at the moment, but could be easily customized to store more in-depth information into MongoDB.

### Using IPData_DB
#### Downloading and installing the package
From your Python project directory, execute: `wget https://github.com/TheConsciousness/IPData_DB/archive/master.zip` Once downloaded, unzip the package: `unzip master.zip` Once 
unzipped, we'll copy the package folder we need into our project directory: `cp IPData_DB-master/ipdata_db/ -r .` And then delete the leftover GitHub zip and folder: `rm -rf 
IPData_DB-master/ master.zip`

#### Importing the package
`import ipdata_db`

#### Creating a configuration
`our_config = ipdata_db.config("mongodb_ip_address", mongodb_port, "mongodb_username", "mongodb_password", "mongodb_db_name", "mongodb_collection_name", "ipdata.co_api_key")`

#### Querying an IP Address
`api_results = ipdata_db.retrieve("201.239.58.78", our_config)`
