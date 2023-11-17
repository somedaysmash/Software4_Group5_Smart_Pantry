import mysql.connector
from config import USER, PASSWORD, HOST


class DbConnectionError(Exception):
    pass

#NEW CLASS TO CONNECT TO DB
class SqlDatabase:
    def __init__(self, database):
        self.host = HOST
        self.user = USER
        self.password = PASSWORD
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
        except (NameError, ImportError, DbConnectionError, ValueError) as e:
            print(e)
            raise


    def disconnect(self):
        if self.connection:
            self.connection.close()

    def execute_query(self, query):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
        except mysql.connector.Error as e:
            raise DbConnectionError(e)

        return result

#TO CONNECT TO THE DB CREATE A NEW VARIABLE = SqlDatabase class and pass through the database. This allows us to connect to more than one database
#example:
# db = SqlDatabase('Smart_Pantry')
# db.connect()
# result = db.execute_query("SELECT * FROM fridge")
# print(result)


# new code - function to add items
def _add_item(stock_store, values):
    try:
        db = SqlDatabase('Smart_Pantry')
        db.connect()
        db.execute_query(f"INSERT INTO {stock_store} (IngredientName, TypeOfIngredient, Quantity, UnitOfMeasurement, MinimumQuantityNeeded, SellByDate) VALUES {values}")
        print(f'The following data has been added to {stock_store}: {values}')
        # Additional check for NULL or None values
        if None in values:
            raise ValueError("Values cannot be None.")
        db.connection.commit()
        print(f"Record added successfully to {stock_store}.")


    except (NameError, ImportError, DbConnectionError, ValueError) as e:
        print(e)
        raise

    finally:
        db.disconnect()



# FUNCTION TO DELETE ITEM FROM STOCK



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
    _add_item(stock_store='Pantry', values=('Tinned Tomatoes', 'Vegetable', 450, 'Grams', 450, '2025-07-30'))
    # update_inventory()
    # retrieve_stock('freezer')
