from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from decouple import config

# Create a new client and connect to the server
client = MongoClient(config("URI"), server_api=ServerApi("1"))

# Send a ping to confirm a successful connection
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")

    database = client["appBancaria"]
    collection = database["clientes"]
except Exception as e:
    print(e)
