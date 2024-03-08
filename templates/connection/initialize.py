# from connection.bond import db
# from flask import current_app

# from connection import create_app

# def createdb():
#     db.create_all(app=create_app())

from connection import db
def createdb(app):
    
    with app.app_context():
        db.create_all()

   
   
 