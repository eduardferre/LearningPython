from pydantic import BaseModel

# User entity
class User(BaseModel):
    id: str | None
    username: str
    email: str