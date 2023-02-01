from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# User entity
class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int
    url: str

users_list = [User(id=1, name="Eduard", surname="Ferre", age=22, url="https://github.com/eduardferre"),
              User(id=2, name="Aleix", surname="Ferre", age=27, url="https://github.com/aleixferre"),
              User(id=3, name="Lluis", surname="Ferre", age=58, url="https://github.com/lluisferre")]

@app.get("/users")
async def users():
    return users_list

@app.get("/user/{id}") # Call from path /{id}
async def userById(id: int):
    return search_user(id)

@app.get("/user/") # Call from query /?id={id}
async def userById(id: int):
    return search_user(id)

@app.post("/user/")
async def user(user: User):
    if type(search_user(user.id)) == User:
        return { "error": f"The user {user.name} already exists"}
    else:
        users_list.append(user)
        return "200 OK"
'''
@app.put("/user/")
async def user(user: User):
'''




def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return { "error": f"There's not any user with id = {id}" } 

