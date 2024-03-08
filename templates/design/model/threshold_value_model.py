from connection import db
from sqlalchemy import ForeignKey
from dataclasses import dataclass


@dataclass

class THRESHOLD_VALUE(db.Model):

    __tablename__="Threshold Value"

    thres_id=db.Column(db.Integer,primary_key=True)
    plant_id=db.Column(db.Integer,ForeignKey("Plant.plant_id"))

    air_hum_min=db.Column(db.String(20))
    air_hum_max=db.Column(db.String(20))

    air_temp_min=db.Column(db.String(20))
    air_temp_max=db.Column(db.String(20))

    light_inten_min=db.Column(db.String(20))
    light_inten_max=db.Column(db.String(20))

    soil_mois_min=db.Column(db.String(20))
    soil_mois_max=db.Column(db.String(20))


    def __init__(self,thres_id,plant_id,air_hum_min,air_hum_max,air_temp_min,
                 air_temp_max,light_inten_min,light_inten_max,soil_mois_min,soil_mois_max):
        
        self.thres_id=thres_id
        self.plant_id=plant_id

        self.air_hum_min=air_hum_min
        self.air_hum_max=air_hum_max

        self.air_temp_min=air_temp_min
        self.air_temp_max=air_temp_max

        self.light_inten_min=light_inten_min
        self.light_inten_max=light_inten_max

        self.soil_mois_min=soil_mois_min
        self.soil_mois_max=soil_mois_max

    @classmethod


    def add_alarmlog(cls,plant_id,air_hum_min,air_hum_max,air_temp_min,
                     air_temp_max,light_inten_min,light_inten_max,soil_mois_min,soil_mois_max):


        thres=cls(None,plant_id,air_hum_min,air_hum_max,air_temp_min,air_temp_max,
                  light_inten_min,light_inten_max,soil_mois_min,soil_mois_max)
        db.session.add(thres)
        db.session.commit()

    @classmethod

    def update_alarmlog(cls,plant_id,air_hum_min,air_hum_max,air_temp_min,
                     air_temp_max,light_inten_min,light_inten_max,soil_mois_min,soil_mois_max):
        alarm=cls.quer.filter_by(plant_id=plant_id)

        alarm.air_hum_min=air_hum_min
        alarm.air_hum_max=air_hum_max

        alarm.air_temp_min=air_temp_min
        alarm.air_temp_max=air_temp_max

        alarm.light_inten_min=light_inten_min
        alarm.light_inten_max=light_inten_max

        alarm.soil_mois_min=soil_mois_min
        alarm.soil_mois_max=soil_mois_max

        db.session.commit()

    @classmethod

    def get_alarmlog_id(cls,plant_id):
       

        
       return cls.gurey.filter_by(plant_id=plant_id).first()
    
    @classmethod
    def get_all_alarmlog(cls):


        return cls.query.all()


       
















    
