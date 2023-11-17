# POST PUT GET DELETE JSON REQUESTS GO HERE

import requests
import json



# POST REQUEST (ADD)

def add_stock_item_fridge(IngredientName, TypeOfIngredient, Quantity, UnitOfMeasurement, MinimumQuantityNeeded, SellByDate):
    new_fridge_stock = {
        "_IngredientName": IngredientName,
        "_TypeOfIngredient":TypeOfIngredient,
        "_Quantity":Quantity,
        "_UnitofMeasurement":UnitOfMeasurement,
        "_MinimumQuantityNeeded":MinimumQuantityNeeded,
        "_SellByDate":SellByDate
    }

    try:
        result = requests.put(
            'http://127.0.0.1:5000/add_item_fridge',
            headers={'content-type': 'application/json'},
            data=json.dumps(new_fridge_stock)
        )
        result.raise_for_status()  # raise an exception if the status code is not 200
        print(result)
        return result.json()
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", repr(errh))  # print the HTTP error
    except requests.exceptions.ConnectionError as errc:
        print("Connection Error:", repr(errc))  # print the connection error
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", repr(errt))  # print the timeout error
    except requests.exceptions.RequestException as err:
        print("Other Error:", repr(err))  # print any other error


def run_fridge():
    add_to_fridge = input('Would you like to add stock to your fridge? Y/N')
    add_item = add_to_fridge.lower() == 'y'


    if add_item:
        IngredientName = input('What is the item name?')
        TypeOfIngredient = input ('What type is this? Dairy, Protein, Vegetable, etc')
        Quantity = input('What quantity are you adding?')
        UnitOfMeasurement = input ('What is the unit of measurement for the quantity?')
        MinimumQuantityNeeded = input("What's the minimum quanity of this you want to hold in stock?")
        SellByDate = input ("What is the sell by date? Enter in format YYY-MM-DD")
        add_stock_item_fridge(IngredientName, TypeOfIngredient, Quantity, UnitOfMeasurement, MinimumQuantityNeeded, SellByDate)
        print("We have added your item")

    print('See you soon!')



# PUT REQUEST (UPDATE)
def update_fridge():
    url = f'http://127.0.0.1:5000/update/fridge'
    response = requests.put(url)
    print(response)
    if response.status_code == 201:
        print(response.json())
    else:
        print(f"Failed to update fridge ingredient.")




# DELETE REQUEST (REMOVE) -Karen

def delete_stock_item_by_name():
    try:
        stock_store = input("Enter the stock store (fridge, freezer, pantry) from which you want to delete an item: ")
        item_name = input(f"Enter the name of the item you want to delete from {stock_store}: ")

        url = f'http://127.0.0.1:5000/delete/{stock_store}/{item_name}'
        response = requests.delete(url)

        if response.status_code == 200:
            print(response.json())
        else:
            print(f"Failed to delete {item_name} from {stock_store}.")

    except requests.exceptions.RequestException as err:
        print("Error:", repr(err))




if __name__ == "__main__":
    # run_fridge()
    # update_fridge()
    delete_stock_item_by_name()