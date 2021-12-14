from fastapi import FastAPI
from pymongo import MongoClient

import json
import auth


app = FastAPI()

app.include_router(auth.accountCreate)


SERVER = MongoClient("localhost",27017)


DB_NAME = SERVER["titanic-fitness"]
USERS = DB_NAME["users"]


