from design.model.threshold_value_model import THRESHOLD_VALUE
from design.model.alarms_model import ALARMS



def check_value(value,thresh_min,thresh_max):

    if thresh_min<= value:
        ALARMS.add_alarm()
        
    


        
# def alarm_query(plant_id,air_hum_value,air_temp_value,light_inten_value,soil_mois_value):

#     all_threshold=THRESHOLD_VALUE.get_alarmlog_id(plant_id)
    
#     air_hum_thresh_min=int(all_threshold.air_hum_min)
#     air_hum_thresh_max=int(all_threshold.air_hum_max)

#     air_temp_thresh_min=int(all_threshold.air_temp_min)
#     air_temp_thresh_max=int(all_threshold.air_temp_max)

#     light_inten_thresh_min=int(all_threshold.light_inten_min)
#     light_inten_thresh_max=int(all_threshold.light_inten_max)

#     soil_mois_thresh_min=int(all_threshold.soil_mois_min)
#     soil_mois_thresh_max=int(all_threshold.soil_mois_max)
    
#     alarmlar={}
    
#     if air_hum_value<=air_hum_thresh_min:
#         alarmlar["air_hum_value"]=True
#     elif air_hum_value>=air_hum_thresh_max:
#         hum_alarm=True

#     if air_temp_value<=air_temp_thresh_min:
#         temp_alarm=True
#     elif air_temp_value>=air_temp_thresh_max:
#         temp_alarm=True

#     if light_inten_value<= light_inten_thresh_min:
#         light_alarm=True

#     elif

#     if   





    




