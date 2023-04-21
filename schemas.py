from pydantic import BaseModel
from typing import Optional


class StationsBase(BaseModel):
    id: int
    station: str
    general_plan: int
    optional_plan: int
    sum: int

    class Config:
        orm_mode = True


class StationCreate(BaseModel):
    station: Optional[str]
    general_plan: Optional[int]
    optional_plan: Optional[int]
    sum: Optional[int]

    class Config:
        orm_mode = True


class StationDelete(BaseModel):
    id: int


class StationPut(BaseModel):
    station: Optional[str]
    general_plan: Optional[int]
    optional_plan: Optional[int]
    sum: Optional[int]

    class Config:
        orm_mode = True

