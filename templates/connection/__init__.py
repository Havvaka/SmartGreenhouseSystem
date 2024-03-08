from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mqtt import Mqtt

mqtt=Mqtt()
db=SQLAlchemy()
def create_app():
    app=Flask(__name__)
    #app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgre:postgre@localhost:5432/connection'
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///C:/Users/Havva/Desktop/smart_greenhouse_system/templates/connection/connection.db'
    app.config['MQTT_BROKER_URL']= "127.0.0.1"
    app.config['MQTT_BROKER_PORT'] = 1883             # Broker bağlağlantı noktası
    app.config['MQTT_KEEPALIVE'] = 60
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY']='secret!'
    print(db.session) 
    

    db.init_app(app)
    mqtt.init_app(app)

    return app