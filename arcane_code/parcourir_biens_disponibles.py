

class Users_biens(db.Model):
    __tablename__ = 'Users_biens'
    ville = db.Column(db.String(15), primary_key=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

#biens_ville = session.query(Users_biens).filter(ville)
biens_ville = session.query(Users_biens).get()

@app.route("/liste_biens", methods=["GET"])
def parcourir():
    #biens_ville = session.query(Users_biens).get(ville)  # la methode get() retourne la primary key. Selon la ville demandée on aura donc que les biens de la ville demandée
    return(session.query(new_bien).get(ville))
