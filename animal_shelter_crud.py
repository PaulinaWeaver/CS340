from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'paulinaWeaver'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 34752
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

# Create method to implement the C in CRUD (create).
    def create(self, data):        
        try:
            # Check if data is provided and not empty
            if data:
                # Insert the document into the animals collection
                insert_result = self.database.animals.insert_one(data)
                # Return True if the insert operation was acknowledged by MongoDB
                return insert_result.acknowledged
            else:
                # Inform the user that no data was provided to insert
                print("Nothing to save, because data parameter is empty")
                return False
        except Exception as e:
            # Catch and print any exceptions during insertion, then return False
            print(f"Error inserting document: {e}")
            return False

# Create method to implement the R in CRUD (remove).
    def read(self, query):
        try:
            # Check if query is provided and not empty
       #     if query:
      #          # If query exists, perform find() with the query filter
     #           query_result = list(self.database.animals.find(query, {"_id": False}))
    #            return query_result
   #         else:
  #              # If no query provided, return empty list
 #               print("No query provided. Returning empty list.")
#                return []
            if query is None:
                query = {}
            query_result = list(self.collection.find(query, {"_id": False}))
            return query_result
        except Exception as e:
            # Catch and print any exceptions during read operation, then return empty list
            print(f"Error reading data: {e}")
            return []

# Create method to implement the U in CRUD (update).
    def update(self, query, updated_data):
        try:
            # Check if query and new data is provided and not empty
            if query and updated_data:
                # Perform an update on all documents matching the query, setting the new data
                result = self.collection.update_many(query, {"$set": updated_data})
                # Return the number of documents modified
                return result.modified_count
            else:
                # Inform if either query or data is missing
                print("Query or update data is missing.")
                return 0
        except Exception as e:
            # Handle and log any errors during the update operation
            print(f"Error updating document: {e}")
            return 0

# Create method to implement the D in CRUD (delete).
    def delete(self, query):
        try:
            # Check if query is provided and not empty
            if query:
                # Delete all documents matching the query
                result = self.collection.delete_many(query)
                # Return the number of documents deleted
                return result.deleted_count
            else:
                # Inform if no query was provided, so nothing was deleted
                print("No query provided. Nothing deleted.")
                return 0
        except Exception as e:
            # Handle and log any errors during document deletion, return 0 to indicate completion
            print(f"Error deleting document: {e}")
            return 0