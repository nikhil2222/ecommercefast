import os
from dotenv import load_dotenv

load_dotenv()
config = os.environ


DB_USERNAME = config.get("MONGO_USERNAME", "")
DB_PASSWORD = config.get("MONGO_PASSWORD", "")
DB_HOST = config.get("MONGO_DB_HOST", "mongo")
DB_PORT = config.get("MONGO_DB_PORT", 27017)
DB_NAME = config.get("MONGO_DB_NAME", "ecommerce")

MONGO_URI = f"mongodb+srv://{DB_USERNAME}:{DB_PASSWORD}@nkproject.uwv9d4w.mongodb.net/{DB_NAME}?retryWrites=true&w=majority"

config["DB_NAME"] = DB_NAME
config["MONGO_URI"] = MONGO_URI