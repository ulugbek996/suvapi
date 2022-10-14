from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional

from sqlalchemy import func
# from sqlalchemy.sql.functions import func
from .. import models, schemas, oauth2
from ..database import get_db


router = APIRouter(
    prefix="/station",
    tags=['Station']
)

@router.post("/",status_code=status.HTTP_201_CREATED)

def station_create(station: schemas.StationCreate,db: Session = Depends(get_db)):

    new_station = models.Station(**station.dict())
    db.add(new_station)
    db.commit()
    db.refresh(new_station)

    return {"data": "new_station"}
