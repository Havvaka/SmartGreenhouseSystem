from dataclasses import dataclass
from datetime import datetime,timedelta
from sqlalchemy import ForeignKey
from connection import db


@dataclass
class LİGHT_İNTENSİTY(db.Model):

    __tablename__="Light Intensity"

    light_inten_id=db.Column(db.Integer,primary_key=True)

    plant_id=db.Column(db.Integer,ForeignKey("Plant.plant_id"))
    light_inten_value=db.Column(db.String(10))
    light_inten_time=db.Column(db.DateTime,default=datetime.utcnow)

    def __init__(self,light_inten_id,plant_id,light_inten_value,light_inten_time):

        self.light_inten_id=light_inten_id
        self.plant_id=plant_id
        self.light_inten_value=light_inten_value
        self.light_inten_time=light_inten_time

    @classmethod
    def add_light_inten(cls,plant_id,light_inten_value,light_inten_time):

        light_inten=cls(None,plant_id,light_inten_value,light_inten_time)

        db.session.add(light_inten)

        db.session.commit()

    @classmethod

    def get_light_inten(cls,plant_id):
        try:

            today=datetime.utcnow().date()
            yesterday=today-timedelta(day=1)
            light=cls.query.filter_by(cls.plant_id==plant_id,cls.light_inten_time.between(yesterday,today).all())
            return light
        
        except Exception as e:
            print("error",e)

    




