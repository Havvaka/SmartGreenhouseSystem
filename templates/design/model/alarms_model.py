from connection import db
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func
from dataclasses import dataclass

@dataclass

class ALARMS(db.Model):
    __tablename__="Alarms"
    alarm_id=db.Column(db.Integer,primary_key=True)
    plant_id=db.Column(db.Integer,ForeignKey("Plant.plant_id"))
    light_alarm=db.Column(db.String(50))
    soil_alarm=db.Column(db.String(50))
    air_temp_alarm=db.Column(db.String(50))
    air_hum_alarm=db.Column(db.String(50))
    alarm_time=db.Column(db.TIMESTAMP, default=func.now())
    alarm_type=db.Column(db.String(180))
    state=db.Column(db.String(50),nullable=False)


    def __init__(self,alarm_id,plant_id,light_alarm,soil_alarm,air_temp_alarm,air_hum_alarm,alarm_type,alarm_time,state):
        self.alarm_id=alarm_id
        self.plant_id=plant_id
        self.light_alarm=light_alarm
        self.soil_alarm=soil_alarm
        self.air_temp_alarm=air_temp_alarm
        self.air_hum_alarm=air_hum_alarm
        self.alarm_type=alarm_type
        self.alarm_time=alarm_time
        self.state=state

    @classmethod

    def add_alarm(cls,plant_id,light_alarm,soil_alarm,air_temp_alarm,air_hum_alarm,alarm_type,alarm_time,state):

        alarm=cls(None,plant_id,light_alarm,soil_alarm,air_temp_alarm,air_hum_alarm,alarm_type,alarm_time,state)

        db.session.add(alarm)
        db.session.commit()


    





