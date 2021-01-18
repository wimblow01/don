import pymongo
from flask import Flask
from pprint import pprint



class Connexion:

    @classmethod
    def connect(cls):
        cls.user = "Wimblow"
        cls.password = "Leboutdumonde47"
        cls.database = "Dons"
        return pymongo.MongoClient(f"mongodb+srv://{cls.user}:{cls.password}@clusterwim.bhpor.mongodb.net/{cls.database}?retryWrites=true&w=majority")


    @classmethod
    def open_db(cls):
        cls.client = cls.connect()
        cls.don = cls.client.Dons.don


    @classmethod
    def close_db(cls):
        cls.client.close()


    @classmethod
    def compteur(cls):
        cls.open_db()
        compte = list(cls.don.aggregate([{ "$group": { "_id" : "null", "sum" : { "$sum": "$don" } } }]))
        cls.close_db()
        return compte[0]

    @classmethod
    def leonardo(cls):
        cls.open_db()
        leo = list(cls.don.find({"name":"Dicaprio"}, {'name': 1, 'fname':1, 'don':1, '_id':0}))
        cls.close_db()
        return leo[0]

    @classmethod
    def brad(cls):
        cls.open_db()
        brad = list(cls.don.find({"name":"Pitt"}, {'name': 1, 'fname':1, 'don':1, '_id':0}))
        cls.close_db()
        return brad[0]

    @classmethod
    def donator(cls):
        cls.open_db()

        count = list(cls.don.aggregate([
            {"$group": {"_id": {"name":"$name", "fname":"$fname"}, "sum" : { "$sum": "$don" }}},
            {"$sort": {"sum": -1}}
            ]))
        cls.close_db()
        return count

