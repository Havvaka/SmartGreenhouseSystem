from dataclasses import dataclass
from connection import db
from sqlalchemy import ForeignKey,DateTime
from datetime import datetime,timedelta


@dataclass

class SOİL_MOİS(db.Model):

    __tablename__="Soil Moisture"

    soil_mois_id=db.Column(db.Integer,primary_key=True)
    plant_id=db.Column(db.Integer,ForeignKey("Plant.plant_id"))
    soil_mois_value=db.Column(db.String(180))
    soil_mois_time=db.Column(db.DateTime,default=datetime.utcnow)
    

    def __init__(self,soil_mois_id,plant_id,soil_mois_value,soil_mois_time):
        self.soil_mois_id=soil_mois_id
        self.plant_id=plant_id
        self.soil_mois_value=soil_mois_value

    @classmethod
    def add_soil_mois(cls,plant_id,soil_mois_value,soil_mois_time):
        moil=cls(None,plant_id,soil_mois_value,soil_mois_time)

        db.session.add(moil)
        db.session.commit()


    @classmethod
    def get_all_soilmois(cls):

        return cls.query.all()


    @classmethod

    def get_mois_today(cls,plant_id):
        try:

            today=datetime.utcnow().date()
            yesterday=today-timedelta(day=1)
            mois=cls.query.filter_by(cls.plant_id==plant_id,cls.soil_mois_time.between(yesterday,today).all())
            return mois
        
        except Exception as e:
            print("error",e)



        





    
