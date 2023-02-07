from pydantic import BaseModel
from typing import Optional

# User entity
class User(BaseModel):
    id: str
    username: str
    email: str