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