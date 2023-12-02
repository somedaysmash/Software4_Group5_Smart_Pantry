# FLASK AND @ROUTES GO HERE
from flask import Flask, jsonify, request, render_template
from utilities import update_inventory, retrieve_stock, SqlDatabase, _add_item, stock_delete
from config import *
from RecipeAPI import get_random_recipe
from pprintpp import pprint as pp
import random

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/kitchen')
def fridge():
    fridge = retrieve_stock("Fridge")
    pantry = retrieve_stock("Pantry")
    freezer = retrieve_stock("Freezer")
    return render_template('kitchen.html', fridge=fridge, pantry=pantry, freezer=freezer)


# Anna fetching recipe name and ingredients
@app.route('/ingredient', methods=('GET', 'POST'))
def ingredient():
    recipe = ""
   
    if request.method == 'POST':
        query = request.form['query']
        # Call the function to get the data
        data = get_random_recipe(query)
        if data:
            recipe = random.choice(data['hits'])['recipe']
    return render_template('ingredient.html', recipe=recipe)


@app.route('/add_item_fridge', methods=['PUT'])
def new_item_fridge():
    new_fridge_stock = request.get_json()
    _add_item(
        _IngredientName=new_fridge_stock['_IngredientName'],
        _TypeOfIngredient=new_fridge_stock['_TypeOfIngredient'],
        _Quantity=new_fridge_stock['_Quantity'],
        _UnitofMeasurement=new_fridge_stock['_UnitofMeasurement'],
        _MinimumQuantityNeeded=new_fridge_stock['_MinimumQuantityNeeded'],
        _SellByDate=new_fridge_stock['_SellByDate']
    )
    return new_fridge_stock


@app.route('/update/fridge', methods=['PUT'])
def update_fridge_stock():
    successful = update_inventory()
    if successful:
        return jsonify({"message": f"Fridge ingredient has been updated."})
    else:
        return jsonify({"error": f"Failed to update fridge ingredient."})


@app.route('/delete/<stock_store>/<item_name>', methods=['DELETE'])
def delete_item_from_stock(stock_store, item_name):
    try:
        stock_delete(stock_store, item_name)
        return jsonify({"message": f"{item_name} successfully deleted from {stock_store}."})
    except:
        return jsonify({"error": f"Failed to delete {item_name} from {stock_store}."})

app.run(port=5002, debug=True)