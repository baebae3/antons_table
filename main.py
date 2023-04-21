from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import crud
import models
import schemas
from database import SessionLocal, sandbox_engine

models.Base.metadata.create_all(bind=sandbox_engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/stations/", response_model=list[schemas.StationsBase])
def read_news(db: Session = Depends(get_db)):
    stations = crud.get_stations(db)
    return stations


@app.post('/stations/create', response_model=List[schemas.StationCreate])
def add_station(station: List[schemas.StationCreate], db: Session = Depends(get_db)):
    stations = crud.create_station(db=db, station=station)
    return stations


@app.delete('/stations/{station_id}')
def delete_station(station_id: int, db: Session = Depends(get_db)):
    delete = crud.delete_station(db=db, station_id=station_id)
    return {"ok": True}


@app.put('/stations/{station_id}', response_model=schemas.StationPut)
def change_station(changed_station: schemas.StationPut, station_id: int, db: Session = Depends(get_db)):
    put = crud.change_station(db=db, station_id=station_id, changed_station=changed_station)
    return put
