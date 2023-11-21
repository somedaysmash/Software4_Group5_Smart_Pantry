import mysql.connector
from config import USER, PASSWORD, HOST
from tkinter import Tk, StringVar, Radiobutton, Button


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

## REDUNDANT FUNCTION TO ADD ITEM TO STOCK
# def add_item_fridge(_IngredientName, _TypeOfIngredient, _Quantity, _UnitofMeasurement, _MinimumQuantityNeeded, _SellByDate):
#     try:
#         db_name = 'Smart_Pantry'
#         db_connection = _connect_to_db(db_name)
#         cur = db_connection.cursor()
#         print(f'Connected to DB: {db_name}')

#         query = "INSERT INTO fridge (IngredientName, TypeOfIngredient, Quantity, UnitOfMeasurement, MinimumQuantityNeeded, SellByDate) VALUES (%s, %s, %s, %s, %s, %s)"
#         val = _IngredientName, _TypeOfIngredient, _Quantity, _UnitofMeasurement, _MinimumQuantityNeeded, _SellByDate
#         print(query, val)
#         cur.execute(query, val)
#         db_connection.commit()
#         cur.close()

#     except (NameError, ImportError, DbConnectionError) as e:

#         print(e)

#         raise

#     finally:
#         if db_connection:
#             db_connection.close()
#             print('DB connection is closed')

# def add_item_freezer(_IngredientName, _TypeOfIngredient, _Quantity, _UnitofMeasurement, _MinimumQuantityNeeded, _SellByDate):
#     try:
#         db_name = 'Smart_Pantry'
#         db_connection = _connect_to_db(db_name)
#         cur = db_connection.cursor()
#         print(f'Connected to DB: {db_name}')

#         query = "INSERT INTO freezer (IngredientName, TypeOfIngredient, Quantity, UnitOfMeasurement, MinimumQuantityNeeded, SellByDate) VALUES (%s, %s, %s, %s, %s, %s)"
#         val = _IngredientName, _TypeOfIngredient, _Quantity, _UnitofMeasurement, _MinimumQuantityNeeded, _SellByDate
#         print(query, val)
#         cur.execute(query, val)
#         db_connection.commit()
#         cur.close()

#     except (NameError, ImportError, DbConnectionError) as e:

#         print(e)

#         raise

#     finally:
#         if db_connection:
#             db_connection.close()
#             print('DB connection is closed')

# def add_item_pantry(_IngredientName, _TypeOfIngredient, _Quantity, _UnitofMeasurement, _MinimumQuantityNeeded, _SellByDate):
#     try:
#         db_name = 'Smart_Pantry'
#         db_connection = _connect_to_db(db_name)
#         cur = db_connection.cursor()
#         print(f'Connected to DB: {db_name}')

#         query = "INSERT INTO pantry (IngredientName, TypeOfIngredient, Quantity, UnitOfMeasurement, MinimumQuantityNeeded, SellByDate) VALUES (%s, %s, %s, %s, %s, %s)"
#         val = _IngredientName, _TypeOfIngredient, _Quantity, _UnitofMeasurement, _MinimumQuantityNeeded, _SellByDate
#         print(query, val)
#         cur.execute(query, val)
#         db_connection.commit()
#         cur.close()

#     except (NameError, ImportError, DbConnectionError) as e:

#         print(e)

#         raise

#     finally:
#         if db_connection:
#             db_connection.close()
#             print('DB connection is closed')



# Karen added FUNCTION TO DELETE ITEM FROM STOCK
#Vanessa edited Karen's code to add Class DB connection plus edited the function to be a class
class StockDelete:
    def __init__(self, stock_store, item_name):
        self.stock_store = stock_store
        self.item_name = item_name

    def delete_item(self, stock_store, item_name):
        try:
            db = SqlDatabase('Smart_Pantry')
            db.connect()
            print(f'Connected to DB: {db}')

            query = f"DELETE FROM {stock_store} WHERE IngredientName = '{item_name}'"
            print(f'Deleting item : {item_name} from {stock_store}')

            db.execute_query(query)
            db.connection.commit()
            print(f"Item : {item_name} deleted from {stock_store}.")

        except (NameError, ImportError, DbConnectionError) as e:
            print(e)
            raise

        finally:
            db.disconnect()

#to call the class StockDelete you need to create an object of the class. You also need to pass the same arguments to the run statement
stock_delete = StockDelete("Freezer", "Diced Onion")



# LAUREN-A FUNCTION TO UPDATE ITEM IN STOCK
#Vanessa has edited to add class connection
def update_inventory():
    try:
        db = SqlDatabase('Smart_Pantry')
        db.connect()

        # Retrieve input from user
        storage_update = input("Which stock store would you like to update? \n - Fridge \n - Freezer \n - Pantry \n : ").lower()
        column_update = input("Which column of data would you like to update? \n - Ingredient name \n - Type of ingredient \n - Quantity \n - Sell by date \n : ").lower()
        data_id = int(input("Please enter the ingredient ID: "))
        new_value = input(f"Enter the new value for the {column_update}: ")

        # Define SQL update query
        update_query = ""

        if column_update == 'ingredient name':
            update_query = f"UPDATE {storage_update} SET IngredientName = {new_value} WHERE ID = {data_id}"
        elif column_update == 'quantity':
            new_value = int(new_value)
            update_query = f"UPDATE {storage_update} SET Quantity = {new_value} WHERE ID = {data_id}"
        elif column_update == 'type of ingredient':
            update_query = f"UPDATE {storage_update} SET TypeOfIngredient = {new_value} WHERE ID = {data_id}"
        elif column_update == 'sell by date':
            new_value = int(new_value)
            update_query = f"UPDATE {storage_update} SET SellByDate = {new_value} WHERE ID = {data_id}"
        else:
            print("Invalid input.")


        # Execute the SQL update query
        db.execute_query(update_query)

        # Commit the changes to the database
        db.connection.commit()
        print("Record Updated successfully ")

    except Exception as e:
        raise DbConnectionError("Failed to update inventory: {e}")

    finally:
        db.disconnect()


# LaurenA adding function to view all stock
# Anna editing the below for Flask to parse
def retrieve_stock(stock_store):
    try:
        db = SqlDatabase('Smart_Pantry')
        db.connect()

        query = f"""SELECT IngredientName, format(Quantity, 0), UnitOfMeasurement FROM {stock_store}"""

        # Execute the SQL update query
        db.execute_query(query)

        print(f'This is the current stock you have in your {stock_store}: ')

        result = db.execute_query(query)
        for row in result:
            print(row)
            print("\n")
        return result

    except Exception as e:
        raise DbConnectionError(f'Failed to update inventory: {e}')

    finally:
        db.disconnect()


# Lauren S - creating a function to select protein data from DB
def fetch_protein_data():
    try:
        # Connect to DB
        db = SqlDatabase('Smart_Pantry')
        db.connect()

        # Execute the query to select protein data
        query = "SELECT protein_name FROM protein_table"
        protein_data = db.execute_query(query)

        # Create a Tkinter window
        root = Tk()
        root.title("Select Protein: ")

        # Store the protein variable
        selected_protein = StringVar()

        def save_selection():
            nonlocal selected_protein
            selected_protein_value = selected_protein.get()
            print(f"Selected protein: {selected_protein_value}")

        for protein in protein_data:
            Radiobutton(root, text=protein[0], variable=selected_protein, value=protein[0]).pack()

        Button(root, text="Save Selection", command=save_selection).pack()

        root.mainloop()

    except Exception as e:
        print(f"An error has occurred: {e}")

    finally:
        db.disconnect()


if __name__ == '__main__':
    # test_connection()
    # _add_item()
    # update_inventory()
    # retrieve_stock(input("Which store do you want to see? Freezer, Fridge or Pantry?").lower())
    # stock_delete.delete_item("Freezer", "Diced Onion")
    fetch_protein_data()