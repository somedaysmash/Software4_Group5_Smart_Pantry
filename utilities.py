# FUNCTIONS GO IN THIS FILE

import mysql.connector
from config import USER, PASSWORD, HOST

class DbConnectionError(Exception):
    pass

def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx

def test_connection():
    contents = []
    try:
        db_name = 'Smart_Pantry'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor(buffered=True)
        print(f'Connected to DB: {db_name}')

        query = """
        DESCRIBE freezer;
        """
        print(query)
        cur.execute(query)

        result = cur.fetchall()
        contents = result
        print(contents)

        cur.close()


    except (NameError, ImportError, DbConnectionError) as e:

        print(e)

        raise

    finally:
        if db_connection:
            db_connection.close()
            print('DB connection is closed')



# FUNCTION TO ADD ITEM TO STOCK
def add_item_fridge(_IngredientName, _TypeOfIngredient, _Quantity, _UnitofMeasurement, _MinimumQuantityNeeded, _SellByDate):
    try:
        db_name = 'Smart_Pantry'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f'Connected to DB: {db_name}')

        query = "INSERT INTO fridge (IngredientName, TypeOfIngredient, Quantity, UnitOfMeasurement, MinimumQuantityNeeded, SellByDate) VALUES (%s, %s, %s, %s, %s, %s)"
        val = _IngredientName, _TypeOfIngredient, _Quantity, _UnitofMeasurement, _MinimumQuantityNeeded, _SellByDate
        print(query, val)
        cur.execute(query, val)
        db_connection.commit()
        cur.close()

    except (NameError, ImportError, DbConnectionError) as e:

        print(e)

        raise

    finally:
        if db_connection:
            db_connection.close()
            print('DB connection is closed')

def add_item_freezer(_IngredientName, _TypeOfIngredient, _Quantity, _UnitofMeasurement, _MinimumQuantityNeeded, _SellByDate):
    try:
        db_name = 'Smart_Pantry'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f'Connected to DB: {db_name}')

        query = "INSERT INTO freezer (IngredientName, TypeOfIngredient, Quantity, UnitOfMeasurement, MinimumQuantityNeeded, SellByDate) VALUES (%s, %s, %s, %s, %s, %s)"
        val = _IngredientName, _TypeOfIngredient, _Quantity, _UnitofMeasurement, _MinimumQuantityNeeded, _SellByDate
        print(query, val)
        cur.execute(query, val)
        db_connection.commit()
        cur.close()

    except (NameError, ImportError, DbConnectionError) as e:

        print(e)

        raise

    finally:
        if db_connection:
            db_connection.close()
            print('DB connection is closed')

def add_item_pantry(_IngredientName, _TypeOfIngredient, _Quantity, _UnitofMeasurement, _MinimumQuantityNeeded, _SellByDate):
    try:
        db_name = 'Smart_Pantry'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f'Connected to DB: {db_name}')

        query = "INSERT INTO pantry (IngredientName, TypeOfIngredient, Quantity, UnitOfMeasurement, MinimumQuantityNeeded, SellByDate) VALUES (%s, %s, %s, %s, %s, %s)"
        val = _IngredientName, _TypeOfIngredient, _Quantity, _UnitofMeasurement, _MinimumQuantityNeeded, _SellByDate
        print(query, val)
        cur.execute(query, val)
        db_connection.commit()
        cur.close()

    except (NameError, ImportError, DbConnectionError) as e:

        print(e)

        raise

    finally:
        if db_connection:
            db_connection.close()
            print('DB connection is closed')

# FUNCTION TO DELETE ITEM FROM STOCK



# FUNCTION TO UPDATE ITEM IN STOCK


if __name__ == '__main__':
    test_connection()
    #add_item_fridge('Feta Cheese', 'Dairy', 200.0, 'Grams', 0.0, '2023-12-31')
    #add_item_freezer('Diced Onion', 'Vegetable', 500.0, 'Grams', 150.0, '2024-10-31')
    #add_item_pantry('Paprika', 'Spices/Seasonings', 100.0, 'Grams', 0.25, '2025-08-31')