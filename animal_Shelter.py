from pymongo import MongoClient
from bson.objectid import ObjectId
import json

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:52951' % (username, password))
        self.database = self.client['AAC']

    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary            
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
# THIS IS A READ METHOD
    def read(self, data):
        if data is not None:
            data = self.database.animals.find(data,{"_id":False}) # data should be dictionary   
            return data
        else:
            raise Exception("nothing to read, hint is empty")

    # this method is used to delete animal from the db
    def delete(self, animal):
        if animal is not None:
            data = self.read(animal) # find animal
            if data is None:
            
                return self.database.animals.delete_many(animal)  # data from directory
        else:
            raise Exception("Error")
            
    # used for updating animal
    def update(self, criteria,newData):
        if criteria is not None and newData is not None:
            self.database.animals.update_many(criteria,{'$set':newData}) 
            self.read(newData)
            
        else:
            raise Exception("Error")
 
                

                
