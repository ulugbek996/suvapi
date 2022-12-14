from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional

from sqlalchemy import func
# from sqlalchemy.sql.functions import func
from .. import models, schemas, oauth2
from ..database import get_db


router = APIRouter(
    prefix="/sensor",
    tags=['Sensor']
)


@router.get("/")
def get_sensor(db:Session = Depends(get_db)):
    sensor = db.query(models.Sensor).all()
    return {"message": sensor}


