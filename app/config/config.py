from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
load_dotenv()

uri = "mongodb+srv://negisinghajayus:Firstapp@pymongo.3xdtt.mongodb.net/?retryWrites=true&w=majority&appName=Pymongo"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
  client.admin.command('ping')
  print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
  print(e)


def get_mongo_client():
    """
    Returns a MongoClient instance.
    """

    return client
