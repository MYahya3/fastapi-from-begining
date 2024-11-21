from fastapi import FastAPI
from enum import Enum

# Instantiate FastAPI app
app = FastAPI()

# We give command in terminal
#uvicorn main:app
# main --> For script name and app for calling our app (These can be any name e.g. testing:new_app)
# Two flags to care about
# --port to set any port e.g. 5000 or 8020 etc
# --reload To relead file automatically whenever some change happen in file


## FastAPI have auto documenation when we give command e.g localhost:5000/docs
## FastAPI go through routes in a sequence of list and it initiate the first route that matched
##  e.g, In users/{user_id :} and users/me both end is string, So it will  run users/{user_id} even i give localhost:5000/users/me
## Because users/me comes after the 1st in sequence, So i rearrange it


# Set up Route
@app.get("/", description= "This is my first route 13/Nov/2024")
async def root():
    return {"message", "Welcome to Pakistan"}


@app.post("/")
async  def post():
    return {"message" : "This is message from Yahya"}

@app.put("/")
async def put():
    return {"message": "This is auto reply"}

# To give some parameter / to call some function and get output
@app.get("/users")
async def list_users():
    return {"message": "This is List of users"}


@app.get("/users/me")
async def get_current_user():
    return {"Message": "This is current user"}


@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {"user_id": user_id}


### To pass any furthers parameters or wish to have multiple choice for same function
class FoodEnum(str, Enum):
    fruits = "fruits"
    vegetables = "vegetables"
    dairy = "dairy"


@app.get("/foods/{food_name}")
async def get_food(food_name: FoodEnum):
    if food_name == FoodEnum.vegetables:
        return {"food_name": food_name, "message": "You are healthy"}

    if food_name.value == "fruits":
        return {"food_name": food_name, "message":"You are still healthy"}

    return {"food_name": food_name, "message": "Dairy is your global choice"}


## Query Parameters ##
fake_db = [{"item_name": "chair"}, {"item_name": "table"}, {"item_name": "book"}]

@app.get("/items")
async def list_items(skip: int = 0, limit: int = 10):
    return fake_db[skip: skip + limit]
