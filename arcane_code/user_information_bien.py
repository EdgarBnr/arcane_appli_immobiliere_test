from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

if __name__ == '__main__':				#utile lorsqu'on a plusieurs applications wsgi : ce qu'on peut imaginer dans le contexte d'une application microservices
    app.run(debug=True)					#le serveur HTTP + WSGI de Flask est automatiquement lancé


basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)



class Bien(db.Model):
	#enregistre les informations concernant le bien. On adapte la quantité autorisée de caractères en fonction de la place estimée pour la variable
    __tablename__ = 'bien_utilisateur'
    nom = db.Column(db.String(140), nullable=False)
    rooms = db.Column(db.Integer,nullable=False)
    proprietaire = db.Column(db.String(50), nullable=False)
    type_de_bien = db.Column(db.String(100), nullable=False)
    caracteristiques = db.Column(db.String(700), nullable=False)

    ville = db.Column(db.String(700), nullable=False)



    def __init__(self, user_fistname, user_name, email):
        self.nom = nom
        self.rooms = rooms
        self.proprietaire = proprietaire
        self.type_de_bien = type_de_bien
        self.caracteristiques = caracteristiques
        self.ville = ville

# crée un nouveau bien pour l'utilisateur
@app.route("/bien", methods=["POST"])
def add_User():
    nom = request.json['nom']
    rooms = request.json['rooms']
    proprietaire = request.json['proprietaire']
    type_de_bien = request.json['type_de_bien']
    caracteristiques = request.json['caracteristiques']
    ville = request.json['ville']

    new_bien = Bien(nom ,rooms, proprietaire, type_de_bien, caracteristiques, ville)

    db.session.add(new_bien)
    db.session.commit()

    return jsonify(new_bien)			# on montre le bien ajouté en réponse à l'utilisateur


#  mettre à jour les informations du bien de l'utilisateur
@app.route("/bien", methods=["PUT"])
def user_update():
    nom = request.json['nom']
    rooms = request.json['rooms']
    proprietaire = request.json['proprietaire']
    type_de_bien = request.json['type_de_bien']
    caracteristiques = request.json['caracteristiques']
    ville = request.json['ville']

    # on update les champs suivants dans la table sql
    bien.nom = nom
    bien.rooms = rooms
    bien.proprietaire = proprietaire
    bien.type_de_bien = type_de_bien
    bien.caracteristiques = caracteristiques
    bien.ville = ville

    db.session.commit()



# supprimer un utilisateur
@app.route("/bien", methods=["DELETE"])
def user_delete():
    db.session.delete(bien)
    db.session.commit()
