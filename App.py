# FLASK AND @ROUTES GO HERE

from flask import Flask, jsonify, request
from utilities_test import add_item_fridge, add_item_freezer, add_item_pantry

app = Flask(__name__)

@app.route('/')
def welcome():
    return '''<h1>Welcome to Smart Pantry</h1>'''

@app.route('/add_item_fridge', methods=['PUT'])
def new_item_fridge():
    new_fridge_stock = request.get_json()
    add_item_fridge(
        _IngredientName=new_fridge_stock['_IngredientName'],
        _TypeOfIngredient=new_fridge_stock['_TypeOfIngredient'],
        _Quantity=new_fridge_stock['_Quantity'],
        _UnitofMeasurement=new_fridge_stock['_UnitofMeasurement'],
        _MinimumQuantityNeeded=new_fridge_stock['_MinimumQuantityNeeded'],
        _SellByDate=new_fridge_stock['_SellByDate']
    )
    return new_fridge_stock


if __name__ == '__main__':
    app.run(debug=True)