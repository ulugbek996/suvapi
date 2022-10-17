from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

from pydantic.types import conint




class DataOut(BaseModel):
    level : float
    flow : float
    corec : int
    timedata: str

    class Config:
        orm_mode = True

class StationCreate(BaseModel):
    name: str
    owner_id: int
    region_id: int
    tashkilot_id: int
    district_id: int
    sensor_id: int
    simcard: str
    code: str
    update_at: str

class StationOut(BaseModel):
    id : int
    name: str
    owner_id: str
    edit_id: str
    region_id: str
    tashkilot_id: str
    district_id: str
    sensor_id: str
    simcard: str
    code: str
    update_at: str
    created_at : str

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    first_name: str
    last_name:str
    email: str
    login: str
    password:str

class UserOut(BaseModel):
    id:int
    first_name: str
    last_name:str
    email: str
    login: str

    class Config:
        orm_mode = True

class StationUpdate(BaseModel):
    name: str
    edit_id: int
    region_id: int
    tashkilot_id: int
    district_id: int
    sensor_id: int
    simcard: str
    code: str
    update_at: str

class UserLogin(BaseModel):
    login: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str



class TokenData(BaseModel):
    id: Optional[str] = None