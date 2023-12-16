# FLASK AND @ROUTES GO HERE
from flask import Flask, jsonify, request, render_template, send_file, session, redirect, url_for
from utilities import update_inventory, retrieve_stock, _add_item, stock_delete, fetch_protein_data, fetch_out_of_date,\
    fetch_expiring_ingredient_data
from RecipeAPI import get_random_recipe, check_stock_for_recipe, recipe_search_by_ingredient, update_pantry
from API_key import secret_key

app = Flask(__name__)
app.secret_key = secret_key


@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/kitchen', methods=['GET', 'POST'])
def kitchen():
    if request.method == 'POST':

        _add_item(
            request.form['stock_store'],
            (request.form['itemName'], request.form['typeOfIngredient'], request.form['quantity'],
                request.form['unitOfMeasurement'], request.form['minQuantity'], request.form['sellByDate'])
        )
    # Retrieve updated stock data after the addition
    fridge = retrieve_stock("Fridge")
    pantry = retrieve_stock("Pantry")
    freezer = retrieve_stock("Freezer")
    return render_template('kitchen.html', fridge=fridge, pantry=pantry, freezer=freezer)


# Anna fetching recipe name and ingredients
@app.route('/ingredient', methods=('GET', 'POST'))
def ingredient():
    if request.method == 'GET':
        proteins = fetch_protein_data()
        return render_template('ingredient.html', recipe={}, proteins=proteins)

    if request.method == 'POST':
        query = request.form['query']
        # Call the function to get the data
        recipe = get_random_recipe(query)
        return render_template('ingredient.html', recipe=recipe, proteins=[])


# @app.route('/add_item_fridge', methods=['PUT'])
# def new_item_fridge():
#     new_fridge_stock = request.get_json()
#     _add_item(
#         stock_store='fridge',
#         values=(
#             new_fridge_stock['IngredientName'],
#             new_fridge_stock['TypeOfIngredient'],
#             new_fridge_stock['Quantity'],
#             new_fridge_stock['UnitOfMeasurement'],
#             new_fridge_stock['MinimumQuantityNeeded'],
#             new_fridge_stock['SellByDate']
#         )
#     )
#     return new_fridge_stock
#
#
# @app.route('/add_item_freezer', methods=['PUT'])
# def new_item_freezer():
#     new_freezer_stock = request.get_json()
#     _add_item(
#         stock_store='freezer',
#         values=(
#             new_freezer_stock['IngredientName'],
#             new_freezer_stock['TypeOfIngredient'],
#             new_freezer_stock['Quantity'],
#             new_freezer_stock['UnitOfMeasurement'],
#             new_freezer_stock['MinimumQuantityNeeded'],
#             new_freezer_stock['SellByDate']
#         )
#     )
#     return new_freezer_stock
#
#
# @app.route('/add_item_pantry', methods=['PUT'])
# def new_item_pantry():
#     new_pantry_stock = request.get_json()
#     _add_item(
#         stock_store='pantry',
#         values=(
#             new_pantry_stock['IngredientName'],
#             new_pantry_stock['TypeOfIngredient'],
#             new_pantry_stock['Quantity'],
#             new_pantry_stock['UnitOfMeasurement'],
#             new_pantry_stock['MinimumQuantityNeeded'],
#             new_pantry_stock['SellByDate']
#         )
#     )
#     return new_pantry_stock


@app.route('/update_stock', methods=['GET', 'POST'])
def update_inventory_route():
    if request.method == 'POST':
        storage_update = request.form['storage_update']
        column_update = request.form['column_update']
        data_id = request.form['data_id']
        new_value = request.form['new_value']

        update_inventory(storage_update, column_update, data_id, new_value)

        return redirect(url_for('kitchen'))

    return render_template('update_stock.html')


@app.route('/delete/<stock_store>/<item_name>', methods=['DELETE'])
def delete_item_from_stock(stock_store, item_name):
    try:
        stock_delete(stock_store, item_name)
        return jsonify({"message": f"{item_name} successfully deleted from {stock_store}."})
    except:
        return jsonify({"error": f"Failed to delete {item_name} from {stock_store}."})


@app.route('/generate_shopping_list')
def generate_shopping_list():
    ingredients_and_weight = [('ingredient1', 100), ('ingredient2', 200), ('ingredient3', 150)]
    missing_ingredients = check_stock_for_recipe(ingredients_and_weight)
    # Create a shopping list text file with missing ingredients
    with open("static/assets/shopping_list.txt", "w") as shoppinglist:
        for ingredient, weight in missing_ingredients:
            shoppinglist.write(f"{weight}, {ingredient}\n")
    return "Shopping list generated successfully!"


@app.route('/shopping')
def upload_shoppinglist():
    with open("static/assets/shopping_list.txt", "r") as shoppinglist:
        content = shoppinglist.readlines()
    print(content)
    return render_template("shoppinglist.html", text=content)


# New routes to download shopping list file.
@app.route('/return_file')
def file_downloads():
    return send_file('static/assets/shopping_list.txt', as_attachment=True)


@app.route('/search_recipe', methods=['GET', 'POST'])
def search_recipe():
    session['page_search'] = 1 # Reset page count for a new search
    if request.method == 'POST':
        ingredient = request.form['ingredient']
        session['ingredient'] = ingredient  # Store ingredient in session
        results = recipe_search_by_ingredient(ingredient)

        if results and 'hits' in results:
            recipes = results['hits']
            return render_template('search_recipe.html', recipes=recipes)

    return render_template('search_recipe.html', recipes=None)


@app.route('/see_more_recipes', methods=['POST'])
def see_more_recipes():
    ingredient = session.get('ingredient')  # Retrieve ingredient from session
    page = session.get('page_search', 1)

    # Increment the page for the "See More Recipes" button
    page += 1
    session['page_search'] = page

    results = recipe_search_by_ingredient(ingredient, page=page)
    recipes = results.get('hits', [])

    if not recipes:
        session['page_search'] = 1

    return render_template('search_recipe.html', recipes=recipes, page=page)


@app.route('/out_of_date_ingredients', methods=['GET', 'POST'])
def out_of_date_ingredients():
    out_of_date_data = fetch_out_of_date()
    expiring_data = fetch_expiring_ingredient_data()
    if request.method == 'POST':
        out_of_date_data = fetch_out_of_date()
        expiring_data = fetch_expiring_ingredient_data()
    return render_template('out_of_date_ingredients.html', out_of_date=out_of_date_data, expiring_data=expiring_data)


@app.route('/add_stock', methods=['GET'])
def add_stock():
    return render_template('add_stock.html')


@app.route('/add_stock', methods=['POST'])
def add_stock_submit():
    stock_store = request.form['stock_store']
    item_name = request.form['itemName']
    type_of_ingredient = request.form['typeOfIngredient']
    quantity = request.form['quantity']
    unit_of_measurement = request.form['unitOfMeasurement']
    min_quantity = request.form['minQuantity']
    sell_by_date = request.form['sellByDate']

    _add_item(stock_store, (item_name, type_of_ingredient, quantity, unit_of_measurement, min_quantity, sell_by_date))

    # Redirect back to original page (kitchen page) after form submission
    return redirect(url_for('kitchen'))


app.run(port=5002, debug=True)
