from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from passlib.context import CryptContext
from . import models
from .database import engine
from .routers import user , station , data ,sensor ,region , balance ,discret , auth

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(data.router)
app.include_router(user.router)
app.include_router(station.router)
app.include_router(sensor.router)
app.include_router(region.router)
app.include_router(balance.router)
app.include_router(discret.router)
app.include_router(auth.router)



@app.get("/")
def root():
    return {"message": "Hello World pushing out to ubuntu"}