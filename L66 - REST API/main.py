import flask
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
KEY = "TopSecretAPIKey"


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route("/random", methods=['GET'])
def get_random_cafe():
    all_cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all", methods=['GET'])
def all_cafe():
    all_cafes = db.session.query(Cafe).all()
    cafes = [cafe.to_dict() for cafe in all_cafes]
    return jsonify(cafes=cafes)


@app.route("/search", methods=['GET'])
def cafe_search():
    location = request.args.get('loc')
    all_cafes = db.session.query(Cafe).all()
    cafes = [cafe.to_dict() for cafe in all_cafes if cafe.location == location]
    if len(cafes) == 0:
        return jsonify(errors={"Not Found": "Sorry we don't have a shop at this location"})
    else:
        return jsonify(cafes=cafes)


## HTTP POST - Create Record

@app.route("/add", methods=['POST'])
def add_cafe():
    new_cafe = Cafe(
        name=request.args.get("name"),
        map_url=request.args.get("map_url"),
        img_url=request.args.get("img_url"),
        location=request.args.get("location"),
        has_sockets=bool(request.args.get("has_sockets")),
        has_toilet=int(request.args.get("has_toilet")),
        has_wifi=bool(request.args.get("has_wifi")),
        can_take_calls=bool(request.args.get("can_take_calls")),
        seats=request.args.get("seats"),
        coffee_price=request.args.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


# HTTP PUT/PATCH - Update Record


@app.route("/update-price/<int:id>", methods=["PATCH"])
def update_price(id):
    all_cafes = db.session.query(Cafe).all()
    for cafe in all_cafes:
        if int(cafe.id) == int(id):
            cafe.coffee_price = request.args.get("new_price")
            db.session.commit()
            return jsonify(response={"success": "Successfully updated the price."})
    return jsonify(response={"Error": "Check your id and try again"})


## HTTP DELETE - Delete Record


@app.route("/delete/<int:cafe_id>", methods=['DELETE'])
def delete_cafe(cafe_id):
    api_key = request.args.get("api-key")
    cafe = db.session.query(Cafe).get(cafe_id)
    if api_key != KEY:
        return jsonify(response={"Error": "Sorry! That's not allowed. Make sure you have the correct key"})
    elif cafe:
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully deleted the cafe."})
    else:
        return jsonify(response={"Error": "Sorry! That cafe doesn't exist. Make sure you have the correct id"})


if __name__ == '__main__':
    app.run(debug=True)
