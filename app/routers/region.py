from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List, Optional

from sqlalchemy import func
# from sqlalchemy.sql.functions import func
from .. import models, schemas, oauth2
from ..database import get_db


router = APIRouter(
    prefix="/region",
    tags=['Region']
)


@router.get("/")
def get_region(db:Session = Depends(get_db)):
    region = db.query(models.Region).all()
    return {"message": region}
