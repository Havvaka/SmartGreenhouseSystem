from connection import mqtt,create_app
from flask import json
from datetime import datetime
from design.model.plants_model import Plant
from design.api.api_air_humidity import add_air_humi
from design.api.api_air_temperature import add_air_tempe
from design.api.api_light_intensity import add_light_intens
from design.api.api_soil_moisture import add_soil_moiss

@mqtt.on_connect()
def on_connect(client,userdata,flags,rc):
    print("Bağlandı:"+str(rc))

    client.subscribe("topic")

@mqtt.on_message()
def on_message(client, userdata, msg):
  
    payload = json.loads(msg.payload)

    plantID=payload.get("plantID")
    air_hum_value=payload.get('air_hum_value')
    air_hum_time=datetime.utcnow()  

    air_temp_value=payload.get("air_temp_value")
    air_temp_time=datetime.utcnow()

    light_inten_value=payload.get("light_inten_value")
    light_inten_time=datetime.utcnow()

    soil_mois_value=payload.get("soil_mois_value")
    soil_mois_time=datetime.utcnow()

    print("on_message function is called!")
    with create_app().app_context():
        plant=Plant.get_all_plantID(plantID)

        add_air_humi(plant.plant_id,air_hum_value,air_hum_time)
        add_air_tempe(plant.plant_id,air_temp_value,air_temp_time)
        add_light_intens(plant.plant_id,light_inten_value,light_inten_time)
        add_soil_moiss(plant.plant_id,soil_mois_value,soil_mois_time)

@mqtt.on_publish()
def on_publish(client, userdata, mid):
    """
    Mqtt nin veritabanına kayıt edilip edilmediği kontrol edilir 
    mesaj yayınlanırsa termimal ekranından görüntülenmiş olur.

    """
    print("Yayınlandı.".format(mid))


    


    




  
