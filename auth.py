from fastapi import APIRouter


router = APIRouter(
    prefix="/auth",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


def user_exists(username, password):
    response = USERS.find_one(
        {
            "username": username,
            "password": password
        }
    )

    if response == "None":
        print({"user_exists": False}) ; return {"user_exists": False}
    print({"user_exists": True}) ; return {"user_exists": True}




@router.post("/account/auth/create")
async def accountCreate(username:str, password:str):
    if user_exists(username, password) == False:
        response = USERS.insert_one(
            {
                "username": username,
                "password": password,
            }
        )
        print({"acknowledged":response.acknowledged})
        return {"data": response}



@router.get("/account/auth/login")
async def accountLogin(username:str, password:str):
    return user_exists(username, password)
    
        