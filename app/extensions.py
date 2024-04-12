import pymongo
from pymongo import MongoClient
from flask import json
import json
from bson import ObjectId

# MongoDB Atlas connection URI
uri = "mongodb+srv://dheerajsharma5869:stI9W2ko9ErVSRZp@webhooksproject.pp1efcm.mongodb.net/?retryWrites=true&w=majority&appName=WebHooksProject"
# uri = 'mongodb+srv://user:user_pin@dbcluster.frhqp.mongodb.net/?retryWrites=true&w=majority&appName=dbcluster'
# uri = 'mongodb+srv://dheerajsharma5869:stI9W2ko9ErVSRZp@dbcluster.frhqp.mongodb.net/?retryWrites=tr÷ue&w=majority&appName=dbcluster'
def add_document(data):
    try:
        # Create a MongoClient instance
        with MongoClient(uri) as client:
            # Access the database and collection
            db = client.get_database("webhooksproject")
            collection = db.get_collection("webhook")
            
            # Insert the provided data into the collection
            result = collection.insert_one(data)
            print(f"Document inserted successfully with ID: {result.inserted_id}")
            # return result.inserted_id

    except pymongo.errors.ConnectionFailure as cf_error:
        print(f"Connection to MongoDB failed: {cf_error}")

    except Exception as e:
        print(f"Error occurred: {e}")


# class CustomJSONEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, ObjectId):
#             return str(obj)
#         return json.JSONEncoder.default(self, obj)
def fetch_data():
    try:
        # Create a MongoClient instance
        with MongoClient(uri) as client:
            # Access the database and collection
            db = client.get_database("webhooksproject")
            collection = db.get_collection("webhook")
            
            # Fetch all the documents from the collection
            recent_updates = collection.find({}, {"_id": 0}).sort("_id", pymongo.DESCENDING).limit(10)

            formatted_updates = list(recent_updates)

            # Serialize the list of formatted documents to JSON
            # formatted_json = json.dumps(formatted_updates)

            print(type(formatted_updates))
            return formatted_updates, 200

    except pymongo.errors.ConnectionFailure as cf_error:
        print(f"Connection to MongoDB failed: {cf_error}")

    except Exception as e:
        print(f"Error occurred: {e}")

