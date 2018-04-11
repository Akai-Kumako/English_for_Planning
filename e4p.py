# English for Planning

import json
from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING

client = MongoClient("localhost", 27017)

db = client.planner
co = db.e4p_collection

with open("schedule.json", "r") as f:
  for i in f:
    a = json.loads(i)
    co.insert_many(json.loads(i))

co.create_index([("Id", ASCENDING)])
co.create_index([("Japanese", ASCENDING)])
co.create_index([("English", ASCENDING)])
co.create_index([("Category", ASCENDING)])
