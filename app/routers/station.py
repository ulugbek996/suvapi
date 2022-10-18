from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional
import datetime
from sqlalchemy import func
# from sqlalchemy.sql.functions import func
from .. import models, schemas, oauth2
from ..database import get_db


router = APIRouter(
    prefix="/station",
    tags=['Station']
)



@router.get("/" ,response_model=List[schemas.StationOut])
def get_stations(db:Session = Depends(get_db)):
    station = db.query(models.Station).all()
    return station


@router.post("/",status_code=status.HTTP_201_CREATED)
def station_create(station: schemas.StationCreate,db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    new_station = models.Station(owner_id=current_user.id, **station.dict())
    db.add(new_station)
    db.commit()
    db.refresh(new_station)
    return {"data": "new_station"}



@router.put("/{code}")
def update_station(code:str , update_station: schemas.StationUpdate,db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
    station_query = db.query(models.Station).filter(models.Station.code == code)
    update_station_dic = update_station.dict()
    update_station_dic["edit_id"] = current_user.id
    update_station_dic["update_at"] = datetime.datetime.now()
    station_query.update(update_station_dic, synchronize_session=False)
    db.commit()
    return station_query.first()


@router.delete("/{id}")
def delete_station(id: int ,db:Session = Depends(get_db)):
    station_query = db.query(models.Station).filter(models.Station.id == id)
    station = station_query.first()
    station_query.delete(synchronize_session=False)
    db.commit()
    return "ok"
