from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional

from sqlalchemy import func
# from sqlalchemy.sql.functions import func
from .. import models, schemas, oauth2
from ..database import get_db


router = APIRouter(
    prefix="/balance",
    tags=['Balance']
)


@router.get("/")
def get_balance(db:Session = Depends(get_db)):
    balance = db.query(models.Balans).all()
    return {"message": balance}

