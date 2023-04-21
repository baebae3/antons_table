from sqlalchemy import Column, Integer, String

from database import Base


class Stations(Base):
    __tablename__ = 'Test2'
    id = Column(Integer, primary_key=True)
    station = Column(String, nullable=True)
    general_plan = Column(Integer, nullable=True)
    optional_plan = Column(Integer, nullable=True)
    sum = Column(Integer, nullable=True)

