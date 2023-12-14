# FLASK AND @ROUTES GO HERE
from flask import Flask, jsonify, request, render_template, send_file, redirect, session
from utilities import update_inventory, retrieve_stock, _add_item, stock_delete, fetch_protein_data
from RecipeAPI import get_random_recipe, check_stock_for_recipe, recipe_search_by_ingredient
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
    if request.method == 'POST':
        ingredient = request.form['ingredient']
        results = recipe_search_by_ingredient(ingredient)

        if results and 'hits' in results:
            recipes = results['hits']
            return render_template('search_recipe.html', recipes=recipes)

    return render_template('search_recipe.html', recipes=None)


@app.route('/see_more_recipes', methods=['POST'])
def see_more_recipes():
    ingredient = request.form['ingredient']
    page = session.get('page_search', 1)

    # Increment the page for the "See More Recipes" button
    session['page_search'] = page + 1

    results = recipe_search_by_ingredient(ingredient, page=page)
    recipes = results.get('hits', [])

    return render_template('search_recipe.html', recipes=recipes)


app.run(port=5002, debug=True)
