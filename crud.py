from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from chemicals.classes.household_chemicals import HouseholdChemicals

import os
import json
import copy

with open('secret.json') as f:
    SECRET = json.load(f)

SQLALCHEMY_TRACK_MODIFICATIONS = False
DB_URI = "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["port"],
    db=SECRET["db"]
)

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class SmartChemical(HouseholdChemicals, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    producer = db.Column(db.String(32), unique=False)
    price_in_uah = db.Column(db.Integer, unique=False)
    weight_in_grams = db.Column(db.Integer, unique=False)
    solubility_in_percent = db.Column(db.Integer, unique=False)
    type_chemical = db.Column(db.String(32), unique=False)

    def __init__(self, producer=None, price_in_uah=None, weight_in_grams=None, solubility_in_percent=None,
                 type_chemical=None):
        super().__init__(producer, price_in_uah, weight_in_grams, solubility_in_percent,
                         type_chemical)


class SmartChemicalSchema(ma.Schema):
    class Meta:
        fields = ('producer', 'price_in_uah', 'weight_in_grams', 'solubility_in_percent',
                  'type_chemical')


smart_chemical_schema = SmartChemicalSchema()
smart_chemicals_schema = SmartChemicalSchema(many=True)


@app.route("/chemical", methods=["POST"])
def create_smart_chemical():
    chemical = SmartChemical(request.json['producer'],
                             request.json['price_in_uah'],
                             request.json['weight_in_grams'],
                             request.json['solubility_in_percent'],
                             request.json['type_chemical']
                             )
    db.session.add(chemical)
    db.session.commit()
    return smart_chemical_schema.jsonify(chemical)


@app.route("/chemical", methods=["GET"])
def get_chemicals():
    all_chemicals = SmartChemical.query.all()
    result = smart_chemicals_schema.dump(all_chemicals)
    return jsonify({'chemicals': result})


@app.route("/chemical/<id>", methods=["GET"])
def get_chemical_by_id(id):
    chemical = SmartChemical.query.get(id)
    if not chemical:
        abort(404)
    return smart_chemical_schema.jsonify(chemical)


@app.route("/chemical/<id>", methods=["PUT"])
def update_chemical(id):
    chemical = SmartChemical.query.get(id)
    if not chemical:
        abort(404)
    old_chemical = copy.deepcopy(chemical)
    chemical.producer = request.json['producer']
    chemical.price_in_uah = request.json['price_in_uah']
    chemical.weight_in_grams = request.json['weight_in_grams']
    chemical.solubility_in_percent = request.json['solubility_in_percent']
    chemical.type_chemical = request.json['type_chemical']
    db.session.commit()
    return smart_chemical_schema.jsonify(chemical)


@app.route("/chemical/<id>", methods=["DELETE"])
def delete_chemical(id):
    chemical = SmartChemical.query.get(id)
    if not chemical:
        abort(404)
    db.session.delete(chemical)
    db.session.commit()
    return smart_chemical_schema.jsonify(chemical)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='0.0.0.0')
