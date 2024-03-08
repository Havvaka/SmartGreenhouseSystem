from dataclasses import dataclass
from sqlalchemy import ForeignKey
from datetime import datetime,timedelta

from connection import db


@dataclass 
class AİR_HUM(db.Model):

    __tablename__="Air Humidity"
    air_hum_id=db.Column(db.Integer,primary_key=True)

    plant_id=db.Column(db.Integer,ForeignKey("Plant.plant_id"))
    air_hum_value=db.Column(db.String(20))
    air_hum_time=db.Column(db.DateTime,default=datetime.utcnow)

    def __init__(self,air_hum_id,plant_id,air_hum_value,air_hum_time):

        self.air_hum_id=air_hum_id
        self.plant_id=plant_id
        self.air_hum_value=air_hum_value
        self.air_hum_time=air_hum_time


    @classmethod

    def add_air_hum(cls,plant_id,air_hum_value,air_hum_time):

        plant=cls(None,plant_id,air_hum_value,air_hum_time)

        db.session.add(plant)
        db.session.commit()
    

    @classmethod

    def get_air_hum_today(cls,plant_id):

        today=datetime.utcnow().date()
        yesterday=today-timedelta(day=1)
        hum=cls.query.filter_by(cls.plant_id==plant_id,cls.air_hum_time.between(yesterday,today)).all()

        return hum







