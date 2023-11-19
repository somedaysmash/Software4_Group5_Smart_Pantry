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


# new code
def close_connection(connection):
    if connection:
        connection.close()
        print('DB connection is closed')


# new code
def execute_query(cur, query, values=None):
    cur.execute(query, values)


def test_connection():
    try:
        db_name = 'Smart_Pantry'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor(buffered=True)
        print(f'Connected to DB: {db_name}')

        query = """
        DESCRIBE freezer;
        """
        print(query)
        execute_query(cur, query, None)

        result = cur.fetchall()
        print(result)

    except (NameError, ImportError, DbConnectionError) as e:
        print(e)
        raise

    finally:
        close_connection(db_connection)


class DbConnectionError(Exception):
    pass


# new code - function to add items
def _add_item(stock_store, values):
    try:
        db_name = 'Smart_Pantry'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f'Connected to DB: {db_name}')

        query = f"INSERT INTO {stock_store} (IngredientName, TypeOfIngredient, Quantity, UnitOfMeasurement, MinimumQuantityNeeded, SellByDate) VALUES (%s, %s, %s, %s, %s, %s)"
        print(f'The following data has been added to {stock_store}: {values}')
        # Additional check for NULL or None values
        if None in values:
            raise ValueError("Values cannot be None.")

        execute_query(cur, query, values)
        db_connection.commit()
        print(f"Record added successfully to {stock_store}.")

    except (NameError, ImportError, DbConnectionError, ValueError) as e:
        print(e)
        raise

    finally:
        close_connection(db_connection)


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

def delete_item(stock_store, item_name):
    try:
        db_name = 'Smart_Pantry'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print(f'Connected to DB: {db_name}')

        query = f"DELETE FROM {stock_store} WHERE IngredientName = %s"
        print(f'Deleting item with ID {item_name} from {stock_store}')

        execute_query(cur, query, (item_name,))
        db_connection.commit()
        print(f"Item with ID {item_name} deleted from {stock_store}.")

    except (NameError, ImportError, DbConnectionError) as e:
        print(e)
        raise

    finally:
        close_connection(db_connection)



# LAUREN-A FUNCTION TO UPDATE ITEM IN STOCK
def update_inventory():
    try:
        db_name = 'smart_pantry'
        conn = _connect_to_db(db_name)
        cur = conn.cursor()

        # Retrieve input from user
        storage_update = input("Which stock store would you like to update? \n - Fridge \n - Freezer \n - Pantry \n : ").lower()
        column_update = input("Which column of data would you like to update? \n - Ingredient name \n - Type of ingredient \n - Quantity \n - Sell by date \n : ").lower()
        data_id = int(input("Please enter the ingredient ID: "))
        new_value = input(f"Enter the new value for the {column_update}: ")

        # Define SQL update query
        update_query = ""

        if column_update == 'ingredient name':
            update_query = f"UPDATE {storage_update} SET IngredientName = %s WHERE ID = %s"
        elif column_update == 'quantity':
            new_value = int(new_value)
            update_query = f"UPDATE {storage_update} SET Quantity = %s WHERE ID = %s"
        elif column_update == 'type of ingredient':
            update_query = f"UPDATE {storage_update} SET TypeOfIngredient = %s WHERE ID = %s"
        elif column_update == 'sell by date':
            new_value = int(new_value)
            update_query = f"UPDATE {storage_update} SET SellByDate = %s WHERE ID = %s"
        else:
            print("Invalid input.")

        # Execute the SQL update query
        execute_query(cur, update_query, (new_value, data_id))

        # Commit the changes to the database
        conn.commit()
        print("Record Updated successfully ")

    except Exception as e:
        raise DbConnectionError("Failed to update inventory: {e}")
    finally:
        close_connection(conn)


# LaurenA adding function to view all stock
def retrieve_stock(stock_store):
    try:
        db_name = 'smart_pantry'
        conn = _connect_to_db(db_name)
        cur = conn.cursor()

        query = f"""SELECT IngredientName, Quantity, UnitOfMeasurement FROM {stock_store}"""

        # Execute the SQL update query
        execute_query(cur, query)

        result = cur.fetchall()
        print(f'This is the current stock you have in your {stock_store}: ')
        for row in result:
            print(row)
            print("\n")

    except Exception as e:
        raise DbConnectionError(f'Failed to update inventory: {e}')
    finally:
        close_connection(conn)


if __name__ == '__main__':
    # test_connection()
    _add_item(stock_store='freezer', values=('Diced Onion', 'Vegetable', 500.0, 'Grams', 150.0, '2024-10-31'))
    # update_inventory()
    # retrieve_stock('freezer')
