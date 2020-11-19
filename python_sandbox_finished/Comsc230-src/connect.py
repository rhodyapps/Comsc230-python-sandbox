def connect_atlas(db):
    from pymongo import MongoClient
    client = MongoClient(db)
    return client