import mysql.connector
from config import USER, PASSWORD, HOST
from tkinter import Tk, StringVar, Radiobutton, Button


class DbConnectionError(Exception):
    pass


# NEW CLASS TO CONNECT TO DB
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

    def execute_query(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            result = cursor.fetchall()
            cursor.close()
        except mysql.connector.Error as e:
            raise DbConnectionError(e)

        return result

# TO CONNECT TO THE DB CREATE A NEW VARIABLE = SqlDatabase class and pass through the database.
# This allows us to connect to more than one database
# example:
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

# REDUNDANT FUNCTION TO ADD ITEM TO STOCK
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
# Vanessa edited Karen's code to add Class DB connection plus edited the function to be a class
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


# to call the class StockDelete you need to create an object of the class. You also need to pass the same arguments to the run statement
stock_delete = StockDelete("Freezer", "Diced Onion")


# LAUREN-A FUNCTION TO UPDATE ITEM IN STOCK
# Vanessa has edited to add class connection
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
        result = db.execute_query(query)
        return result

    except Exception as e:
        raise DbConnectionError(f'Failed to show inventory: {e}')

    finally:
        db.disconnect()


# Lauren S - creating a function to select protein data from DB
def fetch_protein_data(ingredient):
    try:
        # Connect to DB
        db = SqlDatabase('Smart_Pantry')
        db.connect()

        # Execute the query to select protein data
        query = (
            f"SELECT IngredientName, Quantity, UnitOfMeasurement "
            f"FROM Pantry WHERE IngredientName = '{ingredient}' "
            f"UNION "
            f"SELECT IngredientName, Quantity, UnitOfMeasurement "
            f"FROM Fridge WHERE IngredientName = '{ingredient}' "
            f"UNION "
            f"SELECT IngredientName, Quantity, UnitOfMeasurement "
            f"FROM Freezer WHERE IngredientName = '{ingredient}'"
        )
        db.execute_query(query)

        result = db.execute_query(query)
        for row in result:
            print(row)
            print("\n")
        return result

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


def low_stock():
    shoppinglist = []
    try:
        db = SqlDatabase('Smart_Pantry')
        db.connect()

        query = (
            f"SELECT IngredientName, Quantity, UnitOfMeasurement "
            f"FROM Pantry "
            f"WHERE Quantity < '100.0' "
            f"UNION ALL "
            f"SELECT IngredientName, Quantity, UnitOfMeasurement "
            f"FROM Fridge "
            f"WHERE Quantity < '100.0' "
            f"UNION ALL "
            f"SELECT IngredientName, Quantity, UnitOfMeasurement "
            f"FROM Freezer "
            f"WHERE Quantity < '100.0' ")
        db.execute_query(query)

        result = db.execute_query(query)
        # result = cur.fetchall()
        for row in result:
            print(row)
            print("\n")

            add_to_list = input(f"Would you like to add {row} to your shopping list? (yes/no): ")

            if add_to_list.lower() == 'yes':
                print(f"Adding {row} to your shopping list")
                shoppinglist.append(row)
            else:
                print(f"{row} has not been added to your shopping list")
                print("-------")

        print("Your shopping list: ")
        for item in shoppinglist:
            print(item)

    except Exception as e:
        raise DbConnectionError(f'Failed to update inventory: {e}')

    finally:
        db.disconnect()


# Lauren S: Generate shopping list, including low-stock, with the option to add/modify items:
class ShoppingList:
    def __init__(self):
        self.items = {}
        self.connection = None

    def connect_to_database(self, host, user, password, database):
        try:
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            # Handle the error as needed

    def populate_from_database(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "SELECT IngredientName, Quantity FROM Fridge UNION SELECT IngredientName, Quantity FROM Freezer UNION SELECT IngredientName, Quantity FROM Pantry")
            inventory_data = cursor.fetchall()
            for item, quantity in inventory_data:
                self.add_item(item, quantity)
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            # Handle the error as needed
        finally:
            cursor.close()

    def add_item(self, item, quantity):
        if item in self.items:
            self.items[item] += quantity
        else:
            self.items[item] = quantity

    def display_list(self):
        print('Shopping List:')
        for item, quantity in self.items.items():
            print(f'{item}: {quantity}')

    def check_low_stock(self):
        print('Low-stock items:')
        for item, quantity in self.items.items():
            if quantity < 5:  # Adjust the threshold as needed
                print(f'{item}: {quantity}')

    def user_add_item(self):
        while True:
            user_input = input('Do you want to add an item to the list? (yes/no): ')
            if user_input.lower() == 'yes':
                item_to_add = input('Enter the item you want to add: ')
                quantity_to_add = int(input('Enter the quantity: '))
                self.add_item(item_to_add, quantity_to_add)
            else:
                break


# Example usage:
shopping_list = ShoppingList()

# Populate shopping list from the database
# shopping_list.populate_from_database()

# Display initial shopping list
shopping_list.display_list()

# Check and display low-stock items
shopping_list.check_low_stock()

# Allow the user to add items
shopping_list.user_add_item()

# Display the final shopping list
shopping_list.display_list()



# Function outside of Class:
# Lauren S: User prompt for low-stock items
def populate_from_database(self):
    try:
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT IngredientName, Quantity FROM Fridge UNION SELECT IngredientName, Quantity FROM Freezer UNION SELECT IngredientName, Quantity FROM Pantry")
        inventory_data = cursor.fetchall()
        for item, quantity in inventory_data:
            self.add_item(item, quantity)
            if quantity <= 5:  # Set a threshold for low stock
                user_input = input(f"{item} is low in stock. Do you want to add it to the shopping list? (yes/no): ")
                if user_input.lower() == 'yes':
                    shopping_quantity = int(input(f"Enter the quantity of {item} to add to the shopping list: "))
                    self.add_item(item, shopping_quantity)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        # Handle the error as needed
    finally:
        cursor.close()



if __name__ == '__main__':
    # test_connection()
    # _add_item(stock_store='Fridge', values=('Beef', 'Protein', 2000, 'Grams', 450, '2025-07-30'))
    # update_inventory()
    # retrieve_stock(input("Which store do you want to see? Freezer, Fridge or Pantry?").lower())
    # stock_delete.delete_item("Freezer", "Diced Onion")
    # fetch_protein_data(ingredient='Rice')
    low_stock()
