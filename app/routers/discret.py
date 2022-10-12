from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional

from sqlalchemy import func
# from sqlalchemy.sql.functions import func
from .. import models, schemas, oauth2
from ..database import get_db


router = APIRouter(
    prefix="/discret",
    tags=['Discret']
)


@router.get("/")
def get_discret(db:Session = Depends(get_db)):
    discret = db.query(models.District).all()
    return {"message": discret}

@router.get("/{id}")
def get_discretid(id: int, db:Session = Depends(get_db)):
    discret = db.query(models.District).filter(models.District.region_id == id).all()
    return {"message": discret}

