
# API Documentation //https://developer.edamam.com/edamam-docs-recipe-api#/
import requests
from pprintpp import pprint as pp
import csv
import API_key

'''app_id/key stored on separate .py file (API_key.py), register for recipe API (developer plan) at 
https://www.edamam.com'''
app_id = API_key.app_id
app_key = API_key.app_key

'''At least 1 query parameter must be used according to the API documentation, nothing is returned 
otherwise, I've used protein type for user input but I can change this to something else. 
For a random choice, I can write a list of proteins and use random.choice(list) to make it random 
without user input '''


def random_recipe():
    query = input("Please enter chosen ingredient..")

    random_url=(f'https://api.edamam.com/api/recipes/v2?type=public&app_id={app_id}&app_key={app_key}&q={query}&/random=true&field=label&field=ingredients&field=totalWeight')

    response = requests.get(random_url)
    # Will use url/ params instead of very long URL
    # response = requests.get(url=random_url, params=payload)
    # print(response.status_code)

    # will sort this into try/ except blocks with better error handling

    if response.status_code == 200:
        data = response.json()
        # print(type(data))
        # pp(data)
    elif response.status_code != 200:
        print("An error occurred")
    # quit()

    # To access recipe name, ingredients and weight from data
    try:
        refine_label = data['hits'][1]['recipe']['label']
        # To access ingredients and weights (grams to 2d.p.) from data
        refine_ingredient_weight = data['hits'][1]['recipe']['ingredients']
        text = [dictionary["text"] for dictionary in refine_ingredient_weight]
        weight = [dictionary["weight"] for dictionary in refine_ingredient_weight]
        weight_rounded = [round(n, 2) for n in weight]
    except IndexError:
        print("Please enter ingredient name")
    except NameError:
        print("Please try again")

    # A zipped list of ingredients as keys, and weights as values
    try:
        ingredients_and_weight= zip(text, weight_rounded)
        ingredient_list= list(ingredients_and_weight)
        dict_of_weights= dict((x,y) for x,y in ingredient_list)
        pp(dict_of_weights)
    except NameError:
        print("Please try again")


    # CSV file - ingredient items/ weights
    aheader = ["Item", "Weight"]
    with open('random_recipe.csv', 'w', newline='') as csv_file:
       file = csv.writer(csv_file)
       file.writerow([refine_label])
       file.writerow(aheader)
       file.writerows(ingredient_list)

    # Text File - Shopping list
    with open('random_recipe.txt','w') as txt_file:
        txt_file.write(f"Shopping List for {refine_label} "+'\n')
        for key, value in dict_of_weights.items():
            txt_file.write(f"[] {key} ({value}g) \n")


def recipe_search_by_ingredient():
    ingredient = input("Enter an ingredient: ")
    url = f'https://api.edamam.com/api/recipes/v2?type=public&q={ingredient}&app_id={app_id}&app_key={app_key}'

    response = requests.get(url)
    data = response.json()
    return data


def next_page_request(url):
    response = requests.get(url)
    data = response.json()
    return data


def run() -> None:
    results = recipe_search_by_ingredient()
    recipes = results['hits']
    see_more = False

    print(f"Smart Pantry found {results['count']} recipes!")
    print("Here are the first 20 recipes: ")
    for recipe in recipes:
        recipe_data = recipe["recipe"]
        print(recipe_data["label"])
        print(recipe_data["url"])
        print()

    more_recipes = input('Would you like to see more recipes? (yes/no) ').lower()
    if more_recipes == 'yes':
        see_more = True

    while see_more and results['to'] < results['count']:
        url = results['_links']['next']['href']
        results = next_page_request(url)
        recipes = results['hits']
        for recipe in recipes:
            recipe_data = recipe['recipe']
            print(recipe_data['label'])
            print(recipe_data['url'])
            print()

        more_recipes = input('Would you like to see more recipes? (yes/no) ').lower()
        if more_recipes != 'yes':
            see_more = False

    if not see_more:
        print('Thank you for using Smart Pantry!')

    if results['to'] >= results['count']:
        print('That\'s all the recipes we have! Thank you for using Smart Pantry!')


run()

if __name__ == '__main__':
    # random_recipe()
    recipe_search_by_ingredient()
