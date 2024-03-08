from flask import Blueprint,jsonify,request
from design.model.plants_model import Plant
from design.model.threshold_value_model import THRESHOLD_VALUE

apiPlants=Blueprint("apiPlants",__name__,url_prefix="/api/Plants")


@apiPlants.route("/addPlant",methods=["GET"])
def add_Plants():
    try:
        plant_name=request.json["plant_name"]
        plantID=request.json["plantID"]
        air_hum_min=request.json["air_hum_min"]
        air_hum_max=request.json["air_hum_max"]

        air_temp_min=request.json["air_temp_min"]
        air_temp_max=request.json["air_temp_max"]

        light_inten_min=request.json["light_inten_min"]
        light_inten_max=request.json["light_inten_max"]

        soil_mois_min=request.json["soil_mois_min"]
        soil_mois_max=request.json["soil_mois_max"]

        Plant.add_plant(plant_name,plantID)
        plant=Plant.get_filter_by_plant_name(plant_name)
        THRESHOLD_VALUE.add_alarmlog(plant.plant_id,air_hum_min,air_hum_max,air_temp_min,air_temp_max,
                                     light_inten_min,light_inten_max,soil_mois_min,soil_mois_max)
        return jsonify({"success":True,"message":"plant added successfully.."})
    except Exception as e:
        print("error:",e)
        return jsonify({"success":False,"message":"there is an er"})

        
# apiDevice=Blueprint("apiDevice",__name__,url_prefix="/api/device")
# @apiDevice.route("/allDevice",methods=["GET"])
# @apiDevice.route("/addDevice",methods=["GET"])
# def add_Device():
#     try:
#         """
#         Yeni cihaz ve eşik sıcaklık ekleme işlemi yapılır.
#         :param devicename:Eklenen cihazın adı.
#         :pram devID:Eklenen cihazın cihaz id'si.
#         :param devthreshtemp:Eklenecek cihaza ait eşik sıcaklık derecesi.

#         """
#         devicename=request.json["deviceName"]
#         devID=request.json["deviceId"]
#         devthreshtemp=request.json["devthreshtemp"]

#         Device.add_device(devicename,devID)
#         device=Device.get_device_by_DevID(devID)
#         AlarmLog.addalarmslog(device.deviceid,devthreshtemp)
#         return jsonify({"success":True,"message":"Device name added successfully.."})
    
#     except Exception as e:
#         return jsonify({"success":False,"message":"there is an error"})