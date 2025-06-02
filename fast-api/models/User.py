from enum import Enum
from typing import Optional
from pydantic import BaseModel
from uuid import UUID, uuid4

class Gender(str, Enum):
    male = "male"
    female = "female"
    
class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"
class User(BaseModel):
    id: Optional[UUID] = uuid4()
    first_name: str
    middle_name: Optional[str]
    last_name: str
    gender: Gender
    roles: list[Role]
    
class UserUpdate(BaseModel):
    first_name: Optional[str]
    middle_name: Optional[str]
    last_name: Optional[str]
    gender: Optional[Gender]
    roles: Optional[list[Role]]