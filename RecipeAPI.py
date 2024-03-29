
# API Documentation //https://developer.edamam.com/edamam-docs-recipe-api#/
import requests
import API_key
import math
from utilities import SqlDatabase, DbConnectionError
from flask import session

'''app_id/key stored on separate .py file (API_key.py), register for recipe API (developer plan) at 
https://www.edamam.com'''
app_id = API_key.app_id
app_key = API_key.app_key


def get_random_recipe(query):
    api_endpoint = f'https://api.edamam.com/api/recipes/v2?type=public&q={query}&app_id={app_id}&app_key={app_key}&' \
                   f'random=true&field=label&field=ingredients'

    try:
        response = requests.get(api_endpoint)
        if response.status_code == 200:
            data = response.json()
            recipe_data = None
            if 'hits' in data and data['hits']:
                random_recipe = data['hits'][0]['recipe']
                recipe_data = {
                    'label': random_recipe.get('label'),
                    'ingredients': []
                }
                for item in random_recipe.get('ingredients', []):
                    quantity = item.get('quantity', 0)
                    measure = item.get('measure', '')
                    food = item.get('food', '')

                    if quantity != 0 and measure is not None and food is not None:
                        ingredient_text = f"{quantity} {'' if measure == '<unit>' else measure} {food}"
                        item['text'] = ingredient_text
                        recipe_data['ingredients'].append(item)
            return recipe_data
        else:
            return None
    except requests.RequestException as e:
        print(f"Request error: {e}")
        return None

      
def recipe_search_by_ingredient(ingredient, page=1, results=None):
    if page == 1:
        url = f'https://api.edamam.com/api/recipes/v2?type=public&q={ingredient}&app_id={app_id}&app_key={app_key}'
    else:
        # get the next page URL from session
        next_page_url = session.get('next_page_url', '')
        if not next_page_url:
            return None  # handle the case where next page URL is not available
        url = next_page_url
    response = requests.get(url)
    if response.status_code == 200:
        results = response.json()
        # store the next page URL for future use with session
        session['next_page_url'] = results["_links"]["next"]["href"]
        return results
    else:
        return None


def see_more_recipes():
    ingredient = input('Enter an ingredient: ')
    page = 1
    results = None

    while True:
        results = recipe_search_by_ingredient(ingredient, page, results)
        recipes = results.get('hits', [])

        print(f"Smart Pantry found {results['count']} recipes!")
        print(f"Displaying recipes from {results['from']} to {min(results['to'], results['count'])}: ")

        # Use enumerate to assign a value to each recipe
        for value, recipe in enumerate(recipes, 1):
            recipe_data = recipe['recipe']
            print(f"{value}. {recipe_data['label']}")
            print(recipe_data['url'])
            print()

        if results['to'] >= results['count']:
            print('That\'s all the recipes we have! Thank you for using Smart Pantry!')
            break

        more_recipes = input('Would you like to see more recipes? (yes/no) ').lower()

        while more_recipes not in {'yes', 'no'}:
            print('Invalid input. Please enter "yes" or "no".')
            more_recipes = input('Would you like to see more recipes? (yes/no) ').lower()

        if more_recipes != 'yes':
            break

        else:
            page += 1


def next_page_request(url):
    response = requests.get(url)
    data = response.json()
    return data


# FUNCTION TO CREATE SHOPPING LIST OF MISSING ITEMS
def create_shopping_list(missing_ingredients):
    # new text file
    with open('static/assets/shopping_list.txt', 'w') as file:
        for ingredient, weight in missing_ingredients:
            file.write(f' {ingredient} ({weight} g)\n')
    # Print a message to the console
    print('Your shopping list can be found here: shopping_list.txt')


def run():
    results = recipe_search_by_ingredient()
    recipes = results['hits']
    see_more = False

    print(f"Smart Pantry found {results['count']} recipes!")
    print("Here are the first 20 recipes: ")

    # adding enumerate to allow user to select which recipe they want to use
    for value, recipe in enumerate(recipes, 1):
        recipe_data = recipe["recipe"]
        print(f"{value}. {recipe_data['label']}")
        print(recipe_data["url"])
        print()

    more_recipes = input('Would you like to see more recipes? (yes/no) ').lower()

    while more_recipes not in {'yes', 'no'}:
        print('Invalid input. Please enter "yes" or "no".')
        more_recipes = input('Would you like to see more recipes? (yes/no) ').lower()

    if more_recipes == 'yes':
        see_more = True

    while see_more and results['to'] < results['count']:
        url = results['_links']['next']['href']
        results = next_page_request(url)
        if 'hits' in results:
            recipes = results['hits']

            # Use enumerate() to assign a value to each recipe
            for value, recipe in enumerate(recipes, 1):
                recipe_data = recipe['recipe']
                print(f"{value}. {recipe_data['label']}")
                print(recipe_data['url'])
                print()

        more_recipes = input('Would you like to see more recipes? (yes/no) ').lower()

        while more_recipes not in {'yes', 'no'}:
            print('Invalid input. Please enter "yes" or "no".')
            more_recipes = input('Would you like to see more recipes? (yes/no) ').lower()

        if more_recipes != 'yes':
            see_more = False

    # asking user if they want to select a recipe
    if not see_more:
        selection = int(input('Please enter a value to select a recipe: '))
        # Check if the selection is valid
        if 1 <= selection <= len(recipes):
            # Get the selected recipe data
            selected_recipe = recipes[selection - 1]['recipe']
            # Interact with the selected recipe
            print(f"You have selected: {selected_recipe['label']}")

            ingredients_and_weight = []

            for ingredient in selected_recipe['ingredients']:
                # Print the name and weight of each ingredient
                ingredients_and_weight.append((ingredient['food'], math.ceil(ingredient['weight'])))
            # check for the ingredients in stock by calling the check_stock_for_recipe function:
            missing_ingredients = check_stock_for_recipe(ingredients_and_weight)
            print(f"You need to buy the following ingredients: {missing_ingredients}")

            # Using a transaction for creating the shopping list and updating the pantry
            try:
                db = SqlDatabase('Smart_Pantry')
                db.connect()
                # Begin the transaction
                db.start_transaction()

                # Creating the shopping list
                create_shopping_list(missing_ingredients)
                print(f"Here are the full ingredients: {selected_recipe['ingredientLines']}")

                # Update the pantry
                update_pantry(ingredients_and_weight)

                # Commit the transaction if everything is successful
                db.commit()
            except Exception as e:
                # Rollback the transaction if an error occurs
                db.rollback()
                print(f"Error: {e}")
            finally:
                # Close the database connection
                db.disconnect()
        else:
            # Handle the invalid selection
            print('Invalid value. Please try again.')

    if results['to'] >= results['count']:
        print('That\'s all the recipes we have! Thank you for using Smart Pantry!')


# Adding function that takes our recipe and checks the stock in our database, returning True or False
def check_stock_for_recipe(ingredients_and_weight):
    # changing code to add in connection class from utilities
    try:
        db = SqlDatabase('Smart_Pantry')
        db.connect()
    except DbConnectionError as e:
        print(e)
        raise
    # Initialising an empty list
    missing_ingredients = []

    try:
        for ingredient, weight in ingredients_and_weight:
            # Checking the fridge, freezer, and pantry tables for the ingredient
            # Using %s as a placeholder
            query_fridge = f"SELECT * FROM Fridge WHERE IngredientName = %s AND Quantity >= %s"
            query_freezer = f"SELECT * FROM Freezer WHERE IngredientName = %s AND Quantity >= %s"
            query_pantry = f"SELECT * FROM Pantry WHERE IngredientName = %s AND Quantity >= %s"

            try:
                result_fridge = db.execute_query(query_fridge, (ingredient, weight))[0]
            except IndexError:
                result_fridge = None
            try:
                result_freezer = db.execute_query(query_freezer, (ingredient, weight))[0]
            except IndexError:
                result_freezer = None
            try:
                result_pantry = db.execute_query(query_pantry, (ingredient, weight))[0]
            except IndexError:
                result_pantry = None

            # If the ingredient is not available in any of the tables, we add it to the missing list
            if not result_fridge and not result_freezer and not result_pantry:
                missing_ingredients.append(ingredient, weight)
    finally:
        # Closing the database connection outside the loop
        db.disconnect()

    # return list of ingredients:
    return missing_ingredients

    # If all ingredients are available in sufficient quantity, return True
    # return not missing_ingredients


# adding function to update pantry
def update_pantry(ingredients_and_weight):
    try:
        db = SqlDatabase('Smart_Pantry')
        db.connect()
    except DbConnectionError as e:
        print(e)
        raise

    try:
        for ingredient, weight in ingredients_and_weight:
            # Define the storage areas to check
            storage_areas = ['Fridge', 'Freezer', 'Pantry']

            for storage_area in storage_areas:
                # Get the available quantity of the ingredient from the specific storage area
                query = f"SELECT Quantity FROM {storage_area} WHERE IngredientName = %s"
                result = db.execute_query(query, (ingredient,))

                if result:
                    # getting the quantity from the result
                    available_quantity = result[0][0]

                    # Calculate the remaining quantity after deduction - make sure it is not negative
                    remaining_quantity = max(available_quantity - weight, 0)

                    # Update the specific storage area with the remaining quantity
                    update_query = f"UPDATE {storage_area} SET Quantity = %s WHERE IngredientName = %s"
                    db.execute_query(update_query, (remaining_quantity, ingredient))

                    print(f"{ingredient} deducted from {storage_area}. Remaining quantity: {remaining_quantity}")

                    # If the update was successful, break the loop (ingredient found so update is done)
                    break

            else:
                # If ingredient wasn't found in any storage area
                print(f"{ingredient} not found in any storage area.")

        print("Pantry updated.")
    finally:
        db.disconnect()


def show_all():
        db = SqlDatabase('Smart_Pantry')
        db.connect()

        # Get all the ingredients from the database
        query = "SELECT * FROM Fridge UNION SELECT * FROM Freezer UNION SELECT * FROM Pantry"
        results = db.execute_query(query)
        db.disconnect()
        # Print the results
        return results

       
if __name__ == '__main__':
    # random_recipe()
    # run()  # we only need this part to run the sequence
    # results = recipe_search_by_ingredient()
    # recipes = results['hits']
    # recipe_data = recipes[0]["recipe"]
    # ingredients_and_weight = [(ingredient["text"], ingredient["weight"]) for ingredient in recipe_data["ingredients"]]
    #
    # if check_stock_for_recipe(ingredients_and_weight):
    #     print("You have all the ingredients needed for this recipe!")
    # else:
    #     print("Some ingredients are missing in your stock:")
    #     for ingredient, weight in missing_ingredients:
    #         print(f"{ingredient} is missing or needs {weight} grams more.")
    get_random_recipe("chicken")
