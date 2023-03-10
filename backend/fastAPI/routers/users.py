from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/users",
                   tags=["users"],
                   responses={404: { "message": "Not found" }})

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

@router.get("/")
async def users():
    return users_list

@router.get("/{id}") # Call from path /{id}
async def userById(id: int):
    return search_user(id)

@router.get("/") # Call from query /?id={id}
async def userById(id: int):
    return search_user(id)

@router.post("/", response_model=User, status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail=f"The user with id = {user.id} already exists")
    
    users_list.routerend(user)
    return user

@router.put("/")
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
            print(found)
    
    if not found:
        return { "error": f"The user {user.name} has not been updated"  }
    
    return user

@router.delete("/{id}")
async def user(id: int):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
    
    if not found:
        return { "error": f"The user {user.name} has not been deleted"  }
    




def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return { "error": f"There's not any user with id = {id}" } 

