from flask import Flask, request, jsonify, abort
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from classes import abstract_household_chemicals
from classes.abstract_household_chemicals import AbstractHouseholdChemicals
import os
import json
import copy


with open('secret.json') as f:
    SECRET = json.load(f)

SQLALCHEMY_TRACK_MODIFICATIONS = False
DB_URI= "mysql+mysqlconnector://{user}:{password}@{host}:{port}/{db}".format(
    user=SECRET["user"],
    password=SECRET["password"],
    host=SECRET["host"],
    port=SECRET["PORT"],
    db=SECRET["db"]
)
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
db = SQLAlchemy(app)
ma = Marshmallow(app)

class SmartAbstractHouseholdChemicals(AbstractHouseholdChemicals, db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    producer = db.Column(db.String(30), unique=False)
    price_in_uah = db.Column(db.Integer, unique=False)
    weight_in_grams = db.Column(db.Integer, unique=False)
    solubility_in_percent = db.Column(db.Integer, unique=False)
    type_chemical = db.Column(db.String(35), unique=False)
    detergent_type = db.Column(db.Enum, unique=False)
    #ще два поля додумати

def __init__(self, producer=None, price_in_uah=None, weight_in_grams=None, solubility_in_percent=None,
                 type_chemical=None, detergent_type=None):
    super().__init__(producer, price_in_uah, weight_in_grams, solubility_in_percent,
                 type_chemical, detergent_type)
    #е 2 поля

class SmartAbstractHouseholdChemicalsSchema(ma.Schema):
    class Meta:
        fields = ('producer', 'price_in_uah', 'weight_in_grams', 'solubility_in_percent',
                 'type_chemical', 'detergent_type')#ще додати 2

smart_abstract_household_chemical_schema = SmartAbstractHouseholdChemicalsSchema()
smart_abstract_household_chemicals_schema = SmartAbstractHouseholdChemicalsSchema(many=True)

@app.route("/smart_abstract_household_chemicals", method=["POST"])
def add_smart_abstract_household_chemicals():
    smart_abstract_household_chemicals = SmartAbstractHouseholdChemicals( request.json['producer'],
                                                               request.json['price_in_uah'],
                                                               request.json['weight_in_grams'],
                                                               request.json['solubility_in_percent'],
                                                               request.json['type_chemical'],
                                                               request.json['detergent_type'])
    db.session.add(smart_abstract_household_chemicals)
    db.session.commit()
    return smart_abstract_household_chemicals_schema.jsonify(abstract_household_chemicals)


@app.route("/abstract_household_chemicals", methods=["GET"])
def get_smart_abstract_household_chemicals():
    all_smart_abstract_household_chemicals = SmartAbstractHouseholdChemicals.query.all()
    result = smart_abstract_household_chemicals = SmartAbstractHouseholdChemicals.dump(all_smart_abstract_household_chemicals)
    return jsonify({'smart_abstract_household_chemicals': result})

@app.route("/abstract_household_chemicals/<id>", methods=["GET"])
def smart_abstract_household_chemicals(id):
    smart_abstract_household_chemicals = SmartAbstractHouseholdChemicals.query.get(id)
    if not smart_abstract_household_chemicals:
        abort(404)
    return smart_abstract_household_chemicals_schema.jsonify(abstract_household_chemicals)

@app.route("/abstract_household_chemicals/<id>", methods=["PUT"])
def smart_abstract_household_chemicals_update(id):
    smart_abstract_household_chemicals = SmartAbstractHouseholdChemicals.query.get(id)
    if not smart_abstract_household_chemicals:
        abort(404)
    old_smart_abstract_household_chemicals = copy.deepcopy(smart_abstract_household_chemicals)
    smart_abstract_household_chemicals #mistake


@app.route("/abstract_household_chemicals/<id>", methods=["DELETE"])
def smart_abstract_household_chemicals_delete(id):
    smart_abstract_household_chemicals = SmartAbstractHouseholdChemicals.query.get(id)
    if not smart_abstract_household_chemicals:
        abort(404)
    db.session.delete(smart_abstract_household_chemicals)
    db.session.commit()
    return smart_abstract_household_chemicals_schema.jsonify(smart_abstract_household_chemicals)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host='127.0.0.1')




