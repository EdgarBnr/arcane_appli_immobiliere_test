from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

if __name__ == '__main__':				#utile lorsqu'on a plusieurs applications wsgi : ce qu'on peut imaginer dans le contexte d'une application microservices
    app.run(debug=True)			#le serveur HTTP + WSGI de Flask est automatiquement lancé


app = Flask(__name__)							#notre app wsgi
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)


# Profil utilisateur

class User(db.Model):
	#enregistre les informations de l'utilisateur avec un nombre maximal d'élements.
	#L'adresse e-mail de l'utilisateur doit etre unique
    __tablename__ = 'utilisateur'
    user_firstname = db.Column(db.String(80),nullable=False)
    user_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True,nullable=False, primary_key=True)

    # trois informations : prénom / nom / email
    def __init__(self, user_fistname, user_name, email):
        self.user_firstname = user_firstname
        self.user_name = user_name
        self.email = email



# créer un nouvel utilisateur
@app.route("/user", methods=["POST"])
def add_User():
    user_firstname = request.json['user_firstname']
    user_name = request.json['user_name']
    email = request.json['email']

    new_user = User(user_firstname ,user_name, email)

    db.session.add(new_user)
    db.session.commit()

    return jsonify(new_user)		# on montre les caractéristiques du nouvel utilisateur ajouté

#  mettre à jour les informations d'un utilisateur
@app.route("/user", methods=["PUT"])
def user_update():
    user_firstname = request.json['user_firstname']
    user_name = request.json['user_name']
    email = request.json['email']

    user.user_firstname = user_firstname
    user.user_name = user_name
    user.email = email

    db.session.commit()


# supprimer un utilisateur
@app.route("/user", methods=["DELETE"])
def user_delete():
    db.session.delete(user)
    db.session.commit()
