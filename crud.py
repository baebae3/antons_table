from fastapi import HTTPException
from sqlalchemy.orm import Session
from typing import List

import models
import schemas


def get_stations(db: Session):
    return db.query(models.Stations).all()


def create_station(db: Session, station: List[schemas.StationCreate]):
    global_arr = []
    for el in station:
        db_station = models.Stations(station=el.station, general_plan=el.general_plan, optional_plan=el.optional_plan,
                                     sum=el.general_plan + el.optional_plan)
        db.add(db_station)
        db.commit()
        global_arr.append(dict(schemas.StationsBase.from_orm(db_station)))
    return global_arr


def change_station(db: Session, station_id: int, changed_station: schemas.StationPut):
    station_model = db.query(models.Stations).filter(models.Stations.id == station_id)
    upt_station = station_model.first()
    if upt_station is None:
        raise HTTPException(
            status_code=404,
            detail=f"{station_id} : Does not exist"
        )
    updated_data = changed_station.dict(exclude_unset=True)
    station_model.filter(models.Stations.id == station_id).update(updated_data, synchronize_session=False)
    db.commit()
    db.refresh(upt_station)
    return station_model


def delete_station(db: Session, station_id: int):
    station_model = db.query(models.Stations).filter(models.Stations.id == station_id).first()
    if station_model is None:
        raise HTTPException(
            status_code=404,
            detail=f"{station_id} : Does not exist"
        )
    db.query(models.Stations).filter(models.Stations.id == station_id).delete()
    db.commit()
