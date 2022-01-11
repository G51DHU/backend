from fastapi import FastAPI
from pymongo import MongoClient
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, Text
import bson.json_util as bson_json_util

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "https://localhost:3000",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


SERVER = MongoClient("localhost",27017)

DB_NAME = SERVER["titanic-fitness"]

# All collections put into a single dictionary, to make it more descriptive. 
COLLECTION = { 
    "users" : DB_NAME["users"], 
    "all-workouts" : DB_NAME["all-workouts"]
}

###########       auth funcs        ###############
def userAleadyExists(username, password):
    response = str(COLLECTION["users"].find_one(
        {
            "username": username,
            "password": password
        }
    ))
    if response == "None":
        print({"user_already_exists": False}) ; return False
    print({"user_already_exists": True}) ; return True

#####################################################
#
#               /account/auth/
#
#####################################################
@app.post("/account/auth/create")
async def accountCreate(username:str, password:str):
    user_already_exists = userAleadyExists(username, password)

    if user_already_exists == False:
        COLLECTION["users"].insert_one(
            {
                "username": username,
                "password": password,
            }
        )
        return [
            {"POST request Acknowledged": True}, 
            {"Response":"201"}, 
            {"Response reason": "Account created"}]
    else:
        return [
            {"POST request Acknowledged": True},
            {"Response":"409"},
            {"Response reason": "Acount already exists"}
        ]


class login_model(BaseModel):
    username: Text
    password: Text

@app.post("/account/auth/login")
async def accountLogin(user_details: login_model):
    return userAleadyExists(user_details.username, user_details.password)

###########       workouts funcs        ###############


def getAllWorkouts():
    all_workouts = [COLLECTION["all-workouts"].find({}), "Found"]
    for workout in all_workouts:
        yield workout

#####################################################
#
#       /account/workouts
#
#####################################################

@app.get("/account/workouts")
async def getWorkouts(id:str):
    all_workouts = getAllWorkouts()
    if all_workouts[1] == "Found":
        return [
            {"GET request Acknowledged": True}, 
            {"Response":"200"}, 
            {"Response reason": "Workout found"},
        ]
    else:
        return [
            {"POST request Acknowledged": True},
            {"Response":"404"},
            {"Response reason": "Workout not found"}
        ]

