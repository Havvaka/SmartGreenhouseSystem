from dataclasses import dataclass
from sqlalchemy import ForeignKey
from datetime import datetime,timedelta

from connection import db


@dataclass 
class AİR_TEMP(db.Model):

    __tablename__="Air Temperature"
    air_temp_id=db.Column(db.Integer,primary_key=True)

    plant_id=db.Column(db.Integer,ForeignKey("Plant.plant_id"))
    air_temp_value=db.Column(db.String(10))
    air_temp_time=db.Column(db.DateTime,default=datetime.utcnow)

    def __init__(self,air_temp_id,plant_id,air_temp_value,air_temp_time):
        self.air_temp_id=air_temp_id
        self.plant_id=plant_id
        self.air_temp_value=air_temp_value
        self.air_temp_time=air_temp_time

    @classmethod

    def add_air_temp(cls,plant_id,air_temp_value,air_temp_time):

        air_temp=cls(None,plant_id,air_temp_value,air_temp_time)

        db.session.add(air_temp)
        db.session.commit()


    @classmethod

    def get_air_temp_today(cls,plant_id):

        today=datetime.utcnow().date()
        yesterday=today-timedelta(day=1)

        temp=cls.query.filter_by(cls.plant_id==plant_id,cls.air_temp_time.between(yesterday,today)).all()

        return temp



   

