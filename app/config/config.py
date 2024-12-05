from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()


def get_mongo_client():
    """
    Returns a MongoClient instance.
    """

    uri = os.environ.get("MONGODB_URI")
    client = MongoClient(uri, server_api=ServerApi('1'))
    return client
