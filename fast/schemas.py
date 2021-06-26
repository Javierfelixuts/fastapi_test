from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

#Item
class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
        
#User 
class UserBase(BaseModel):
    email: str
    usr_username : str


class UserCreate(UserBase):
    password: str
    

class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True
