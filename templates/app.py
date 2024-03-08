from connection import create_app
from connection.initialize import createdb
from design.api.api_plants import apiPlants
from flask_cors import CORS
from mqtt.mqtt_connection import on_connect,on_message,on_publish

app=create_app()
CORS(app)
createdb(app)

app.register_blueprint(apiPlants)


if __name__=="__main__":
   
    app.run(debug=True)