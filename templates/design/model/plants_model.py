from dataclasses import dataclass
from connection import db

@dataclass
class Plant(db.Model):
    __tablename__="Plant"
    plant_id=db.Column(db.Integer,primary_key=True)
    plant_name=db.Column(db.String(180))
    plantID=db.Column(db.String(180))

    def __init__(self,plant_id,plant_name,plantID):
        self.plant_id=plant_id
        self.plant_name=plant_name
        self.plantID=plantID

    @classmethod
    def add_plant(cls,plant_name,plantID):
        plant=cls(None,plant_name,plantID)
        db.session.add(plant)
        db.session.commit()

    @classmethod
    def get_plant_by_id(cls,plant_id):
        plant=cls.query.filter_by(plant_id=plant_id).first()

        return plant
    @classmethod
    def get_all_plant(cls):
        return cls.query.all()
    
    @classmethod
    def get_filter_by_plant_name(cls,plant_name):

        return cls.query.filter_by(plant_name=plant_name).first()
    
    @classmethod
    def update_plant(cls,plant_id,plant_name,plantID):
        plant=cls.query.filter_by(plant_id=plant_id).first()

        plant.plant_name=plant_name
        plant.plantID=plantID


        db.session.commit()

    @classmethod
    def delete_plant(cls,plant_id):
        plant=cls.query.filter_by(plant_id=plant_id).first()

        db.session.delete(plant)
        db.session.commit()

    @classmethod
    def get_all_plantID(cls,plantID):

        return cls.query.filter_by(plantID=plantID).first()
    

        



