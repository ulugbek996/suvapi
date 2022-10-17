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



@router.get("/")
def get_stations(db:Session = Depends(get_db)):
    station = db.query(models.Station).all()
    return {"message": station}


@router.post("/",status_code=status.HTTP_201_CREATED)
def station_create(station: schemas.StationCreate,db: Session = Depends(get_db)):

    new_station = models.Station(**station.dict())
    db.add(new_station)
    db.commit()
    db.refresh(new_station)
    return {"data": "new_station"}



@router.put("/{code}")
def update_station(code:str , update_station: schemas.StationUpdate,db: Session = Depends(get_db)):
    station_query = db.query(models.Station).filter(models.Station.code == code)
    station_query.update(update_station.dict(), synchronize_session=False)
    db.commit()
    return station_query.first()


@router.delete("/{id}")
def delete_station(id: int ,db:Session = Depends(get_db)):
    station_query = db.query(models.Station).filter(models.Station.id == id)
    station = station_query.first()
    station_query.delete(synchronize_session=False)
    db.commit()
    return "ok"
