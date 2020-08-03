import json
import pymongo
import pprint

connection_string = "mongodb+srv://admin08345:GWSgnYU4pu7zs2S@cluster0.xjgrr.mongodb.net/activitydashboard?retryWrites=true&w=majority"

with pymongo.MongoClient(connection_string) as client:
    db = client["activitydashboard"]
    coll_activity = db["activities"]

    cursor_activity = coll_activity.aggregate([
        {"$unwind": "$courses"},
    ])

    data_activity = list(coll_activity.find({}))
    pprint.pprint(data_activity)
