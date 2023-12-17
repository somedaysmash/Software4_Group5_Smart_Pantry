# FLASK AND @ROUTES GO HERE
from flask import Flask, request, render_template, send_file, session, redirect, url_for
from utilities import update_inventory_record, retrieve_stock, _add_item, StockDelete, fetch_protein_data, fetch_out_of_date, \
    fetch_expiring_ingredient_data, low_stock, metrify
from RecipeAPI import get_random_recipe, check_stock_for_recipe, recipe_search_by_ingredient, show_all
from API_key import *

app = Flask(__name__)
app.secret_key = app_key


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
        all_stock = show_all()
        recipe_shopping = []
        enough_stock = []
        for ingredient in recipe['ingredients']:
            for item in all_stock:
                if item[1].upper() == ingredient['food'].upper() and metrify(ingredient['measure'], item[4], ingredient['quantity']) < item[3]:
                    enough_stock.append(ingredient)
        for ingredient in recipe['ingredients']:
            if ingredient not in enough_stock:
                recipe_shopping.append(
                    (ingredient['food'], ingredient['quantity'], ingredient['measure']))
        return render_template('ingredient.html', recipe=recipe, proteins=[], stock=recipe_shopping)

@app.route('/update_stock', methods=['GET', 'POST'])
def update_inventory():
    if request.method == 'POST':
        storage_update = request.form['storage_update']
        column_update = request.form['column_update']
        data_id = request.form['data_id']
        new_value = request.form['new_value']

        update_inventory_record(storage_update, column_update.lower(), data_id, new_value)

        return redirect(url_for('kitchen'))

    return render_template('update_stock.html')



@app.route('/delete_stock', methods=['GET', 'POST'])
def delete_item_from_stock():
    if request.method == 'POST':
        stock_store = request.form['stock_store']
        item_name = request.form['item_name']

        stock_delete = StockDelete(stock_store, item_name)
        stock_delete.delete_item(stock_store, item_name)

        return redirect(url_for('kitchen'))

    return render_template('delete_stock.html')



@app.route('/generate_shopping_list')
def generate_shopping_list():
    ingredients_and_weight = [
        ('ingredient1', 100), ('ingredient2', 200), ('ingredient3', 150)]
    missing_ingredients = check_stock_for_recipe(ingredients_and_weight)
    # Create a shopping list text file with missing ingredients
    with open("static/assets/shopping_list.txt", "w") as shoppinglist:
        for ingredient, weight in missing_ingredients:
            shoppinglist.write(f"{weight}, {ingredient}\n")
    return "Shopping list generated successfully!"


@app.route('/shopping')
def upload_shoppinglist():
    low_stock()
    with open('static/assets/list_of_low_stock.txt', 'r') as file:
        slist = file.readlines()
        return render_template('shoppinglist.html', line=slist)


# low_stock_items.write(result)
# @app.route('/return_file')
# def file_downloads():
#     return send_file('static/assets/list_of_low_stock.txt')


@app.route('/search_recipe', methods=['GET', 'POST'])
def search_recipe():
    # Reset page count for a new search
    session['page_search'] = 1
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

    _add_item(stock_store, (item_name, type_of_ingredient, quantity,
              unit_of_measurement, min_quantity, sell_by_date))

    # Redirect back to original page (kitchen page) after form submission
    return redirect(url_for('kitchen'))


app.run(port=5002, debug=True)
