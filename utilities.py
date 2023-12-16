import mysql.connector
from datetime import datetime
from config import *
from tkinter import Tk, StringVar, Radiobutton, Button


class DbConnectionError(Exception):
    pass


class DbQueryError(Exception):
    def __init__(self, message, query, params):
        super().__init__(message)
        self.query = query
        self.params = params

    def __str__(self):
        return (f"{self.message}\nQuery: {self.query}\nParams: {self.params}")


# NEW CLASS TO CONNECT TO DB
class SqlDatabase:
    def __init__(self, database):
        assert database, "Database name cannot be None"
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

    def commit(self):
        if not self.connection:
             raise DbConnectionError("Connection is not established")
        try:
             self.connection.commit()
        except mysql.connector.Error as e:
            print(f"Error committing transaction: {e}")
            raise

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def execute_query(self, query, params=None):
        if not self.connection:
            raise DbConnectionError("Connection is not established")
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            result = cursor.fetchall()
            cursor.close()
        except mysql.connector.Error as e:
            raise DbQueryError(str(e), query, params)
            print(e)
            quit(1)
        return result

    def start_transaction(self):
        if not self.connection:
            raise DbConnectionError("Connection is not established")
        try:
            self.connection.start_transaction()
        except mysql.connector.Error as e:
            print(f"Error starting transaction: {e}")
            raise

    def rollback(self):
        if not self.connection:
            raise DbConnectionError("Connection is not established")
        try:
            self.connection.rollback()
        except mysql.connector.Error as e:
            print(f"Error rolling back transaction: {e}")
            raise

# TO CONNECT TO THE DB CREATE A NEW VARIABLE = SqlDatabase class and pass through the database.
# This allows us to connect to more than one database
# example:
# db = SqlDatabase('Smart_Pantry')
# db.connect()
# result = db.execute_query("SELECT * FROM fridge")
# print(result)


def assert_sell_by_date(sell_by_date):
    # Check that the sell by date is a string
    assert isinstance(sell_by_date, str), "Sell by date must be a string"
    # Check that the sell by date matches the format YYYY-MM-DD
    try:
        datetime.strptime(sell_by_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Sell by date must be in the format YYYY-MM-DD")


def _add_item(stock_store, values):
    """
    Insert a new item into the specified table in the Smart_Pantry database.

    :param stock_store: The name of the table to insert into. Must be one of Fridge, Freezer, or Pantry.
    :param values: A tuple or list of values to insert. Must match the column names and types of the table.
    """

    # Check that the table name is valid
    # assert stock_store in ["Fridge", "Freezer", "Pantry"], "Invalid table name"
    try:
        # Create and connect to the database object
        db = SqlDatabase('Smart_Pantry')
        db.connect()

        # Check that the values are a tuple or list
        # if not isinstance(values, (tuple, list)):
        # raise TypeError("Values must be a tuple or list")

        # Execute the insert query with the given values
        db.execute_query(query=
            f"INSERT INTO {stock_store} (IngredientName, TypeOfIngredient, Quantity, UnitofMeasurement, MinimumQuantityNeeded, SellByDate) VALUES {values}") #removed unitofmeasurement

        # Commit the changes to the database
        db.connection.commit()
        print(f"Record added successfully to {stock_store}.")

    except (NameError, ImportError, DbConnectionError, ValueError, TypeError, DbQueryError) as e:
        print(e)
        # Reraise the exception to the user
        raise

    finally:
        # Close the database connection
        db.disconnect()


class StockDelete:
    """
    A class to delete an item from a specified table in the Smart_Pantry database.
    """
    def __init__(self, stock_store, item_name):
        """
        Initialize the class with the table name and the item name.

        :param stock_store: The name of the table to delete from. Must be either Fridge, Freezer, or Pantry.
        :param item_name: The name of the item to delete. Must not be None or empty.
        """
        self.stock_store = stock_store
        self.item_name = item_name

    def delete_item(self, stock_store, item_name):
        # Check that the table name is valid
        assert stock_store in ["fridge", "freezer", "pantry"], "Invalid table name"
        # assert stock_store in ["Fridge", "Freezer", "Pantry"], "Invalid table name"
        # Check the item name is not none or empty
        assert item_name, "Item name cannot be None or empty"

        try:
            # Create and connect to db object
            db = SqlDatabase('Smart_Pantry')
            db.connect()
            cursor = db.connection.cursor()
            print(f'Connected to DB: {db}')

            # Construct and execute the delete query with given table and item name
            query = f"DELETE FROM {stock_store} WHERE IngredientName = %s"
            print(f'Deleting item : {item_name} from {stock_store}')

            cursor.execute(query, (self.item_name,))
            # Check that the deletion was successful
            if cursor.rowcount == 0:
                raise DbQueryError("No such item in the table", query, None)

            # Check the connection object is not none
            assert db.connection, "Connection not established"
            # Save changes to the database
            db.connection.commit()
            print(f"Item : {item_name} deleted from {stock_store}.")

        except (NameError, ImportError, DbConnectionError, DbQueryError) as e:
            # Handle any errors that might occur during the database operation
            # NameError: The SqlDatabase class is not defined or imported
            # ImportError: The mysql.connector module is not installed or imported
            # DbConnectionError: The database connection failed or was interrupted
            # DbQueryError: The query is not supported or compatible with the table schema
            print(e)
            # Reraise the exception to the caller
            raise
        finally:
            cursor.close()
            # Close the database connection
            db.disconnect()


# to call the class StockDelete you need to create an object of the class.
# You also need to pass the same arguments to the run statement
stock_delete = StockDelete("freezer", "Diced Onion")


def update_inventory_record(storage_update, column_update, data_id, new_value):
    """
    Update a record in the Smart_Pantry database based on user input.

    :param: None
    :return: None
    """
    try:
        db = SqlDatabase('Smart_Pantry')
        db.connect()

        # Retrieve input from user
        # storage_update = input("Which stock store would you like to update? \n - Fridge \n - Freezer \n - Pantry \n : ")\
        #     .lower()
        # Check table name is valid
        assert storage_update in ["Fridge", "Freezer", "Pantry"], "Invalid table name"
        # assert storage_update in ["Fridge", "Freezer", "Pantry"], "Invalid table name"
        # column_update = input("Which column of data would you like to update? \n - Ingredient name \n "
        #                       "- Type of ingredient \n - Quantity \n - Sell by date \n : ").lower()
        # Check column name is valid
        assert column_update in ["ingredient name", "type of ingredient", "quantity", "sell by date"], \
            "Invalid column name"
        # data_id_input = input("Please enter the ingredient ID: ")
        # Check the data ID is valid and exists in the table
        try:
            data_id = int(data_id)
            result = db.execute_query(f"SELECT * FROM {storage_update} WHERE ID = {data_id}")
            if not result:
                # db.execute_query(f"SELECT * FROM {storage_update} WHERE ID = {data_id}")
                # if db.connection.rowcount == 0:
                raise ValueError("No such ID in the table")
        except ValueError:
            raise ValueError("ID must be an integer")
        except Exception as e:
            raise ValueError(f"An error occurred: {str(e)}")
        # new_value = input(f"Enter the new value for the {column_update}: ")

        # Define SQL update query
        update_query = ""

        if column_update == 'ingredient name':
            # Check that the new value is a string
            assert isinstance(new_value, str), "New value must be a string"
            # Update the ingredient name with the new value
            update_query = f"UPDATE {storage_update} SET IngredientName = %s WHERE ID = %s"
            db.execute_query(update_query, (new_value, data_id))
        elif column_update == 'quantity':
            new_value = int(new_value)
            # Check that the new value is an integer
            assert isinstance(new_value, int), "New value must be an integer"
            # Update the quantity with the new value
            update_query = f"UPDATE {storage_update} SET Quantity = %s WHERE ID = %s"
            db.execute_query(update_query, (new_value, data_id))
        elif column_update == 'type of ingredient':
            # Check that the new value is a string
            assert isinstance(new_value, str), "New value must be a string"
            # Update the type of ingredient with the new value
            update_query = f"UPDATE {storage_update} SET TypeOfIngredient = %s WHERE ID = %s"
            db.execute_query(update_query, (new_value, data_id))
        elif column_update == 'sell by date':
            # Check that the new value is a valid date in the format YYYY-MM-DD
            assert_sell_by_date(new_value)
            new_value = int(new_value)
            # Update the sell by date with the new value
            update_query = f"UPDATE {storage_update} SET SellByDate = %s WHERE ID = %s"
            db.execute_query(update_query, (new_value, data_id))
        else:
            raise ValueError("Invalid input.")

        # Commit the changes to the database
        db.connection.commit()
        print("Record Updated successfully ")

    except Exception as e:
        raise DbConnectionError(f"Failed to update inventory: {e}")

    finally:
        # Close the database connection
        db.disconnect()


def retrieve_stock(stock_store):
    """
    Retrieve stock information from a specific table in the Smart_Pantry database.

    :param stock_store: The name of the table to retrieve from. Must be either Fridge, Freezer, or Pantry.
    :return: A list of tuples containing ingredient name and quantity for each item in the table.
    """
    # Check that the table name is valid
    # assert stock_store in ["fridge", "freezer", "pantry"], "Invalid table name"
    try:
        # Create a connection to the database
        db = SqlDatabase('Smart_Pantry')
        db.connect()

        # Define SQL query to select relevant columns from table
        query = f"""SELECT IngredientName, format(Quantity, 0), UnitOfMeasurement FROM {stock_store}"""

        # Execute the SQL update query and store result
        try:
            db.execute_query(query)
            result = db.execute_query(query)
            print(result)

        except mysql.connector.Error as e:
            # Handle errors that may occur during query execution
            raise DbQueryError(str(e), query, None)

    except Exception as e:
        # Handle any errors that might occur in db connection
        raise DbConnectionError(f'Failed to show inventory: {e}')

    finally:
        # Close database connection
        db.disconnect()
    return result


def fetch_protein_data():
    '''Fetches the protein data from the database and displays it in a Tkinter window.

    :return: list: A list of tuples containing the ingredient name, quantity, and sell by date.

    :raise: 
        DbQueryError: If the ingredient is not found in the database.
        tkinter.TclError: If there is an error with the Tkinter window.
        Exception: If there is any other error.
    '''

    try:
        # Connect to DB
        db = SqlDatabase('Smart_Pantry')
        db.connect()
        protein_data = ()
        # Execute the query to select protein data
        query = ("SELECT ingredientname, quantity, sellbydate FROM proteinview ORDER BY sellbydate;"
        )
        # Execute the query and store the result
        protein_data = db.execute_query(query)
        if not protein_data:
            # Raise a custom exception if no protein found
            raise DbQueryError("No protein in the database", query, None)
        # Print each row of the result
        for row in protein_data:
            print(row)
            print("\n")
        return protein_data 

    finally:
        # Disconnect from the database
        db.disconnect()


def low_stock():
    '''Checks the quantity of ingredients in the database and creates a shopping list based on user input.
    This function connects to the Smart_Pantry database and queries the Pantry, Fridge, and Freezer tables
    to find the ingredients that have a quantity less than 100.0.
    It then prints the result and asks the user if they want to add any of the ingredients to their shopping list.
    It finally prints the shopping list and disconnects from the database.

    :return: list: A list of tuples containing the ingredient name, quantity,
    and unit of measurement that the user added to their shopping list.

    :raise: DbConnectionError: If there is an error in connecting to or disconnecting from the database.
        DbQueryError: If the query result is empty, meaning that there are no ingredients with low stock.
        ValueError: If the user enters an invalid input, such as something other than 'yes' or 'no'.
    '''
    # Creating a new variable to store the shopping list
    shoppinglist = []
    try:
        # Connect to DB
        db = SqlDatabase('Smart_Pantry')
        db.connect()

        # setting up the query to select ingredients with low quantity from different tables
        query = (
            f"SELECT IngredientName, Quantity "
            f"FROM Pantry "
            f"WHERE Quantity < 100.0 "
            f"UNION ALL "
            f"SELECT IngredientName, Quantity "
            f"FROM Fridge "
            f"WHERE Quantity < 100.0 "
            f"UNION ALL "
            f"SELECT IngredientName, Quantity "
            f"FROM Freezer "
            f"WHERE Quantity < 100.0 ")
        # Executing the query
        result = db.execute_query(query)

        try:
            if not result:
                # Raise an exception if the query result is empty
                raise DbQueryError(
                    "No such ingredient in the database", query, None)
        except DbQueryError as e:
            # Print the exception message and inform the user that they have enough stock
            print(e)
            print("You have enough stock of all ingredients")

        for row in result:
            # Print each row of the result
            print(row)
            print("\n")
            # Assert that the row variable is a tuple
            assert isinstance(row, tuple), "Row must be a tuple"

            try:
                # Ask the user if they want to add the ingredient to the shopping list
                add_to_list = input(f"Would you like to add {row} to your shopping list? (yes/no): ").lower()
                if add_to_list not in ("yes", "no", "Yes", "No"):
                    # add_to_list = input(f"Would you like to add {row} to your shopping list? (yes/no): ")
                    # Raise a ValueError if the user input is invalid
                    raise ValueError("Invalid input")
            except ValueError as e:
                # Print the exception message and ask the user to enter a valid input
                print(e)
                print("Please enter yes or no)")

            if add_to_list.lower() == 'yes':
                # Add the ingredient to the shopping list and print a confirmation message
                print(f"Adding {row} to your shopping list")
                shoppinglist.append(row)

            else:
                # Print a message that the ingredient is not added to the shopping list
                print(f"{row} has not been added to your shopping list")
                print("-------")

        # Print the final shopping list
        print("Your shopping list: ")
        for item in shoppinglist:
            print(item)
        # Assert that the item variable is a tuple
        # assert isinstance(item, tuple), "Item must be a tuple"
        # Assert that the shoppinglist variable is a list
        # assert isinstance(shoppinglist, list), "Shopping list must be a list"

    except Exception as e:
        # Raise a custom exception if there is an error in connecting to or disconnecting from the database
        raise DbConnectionError(f'Failed to update inventory: {e}')

    finally:
        # Disconnect from the database
        db.disconnect()

    return shoppinglist


# Lauren S: Generate shopping list, including low-stock, with the option to add/modify items:
class ShoppingList:
    def __init__(self):
        self.items = {}
        self.connection = None

    def populate_from_database(self):
        '''
        Populates the inventory with the data from the database.
        This method connects to the Smart_Pantry database and executes a query
        to select the ingredient name and quantity from the Fridge, Freezer, and Pantry tables.
        It then loops through the query result and calls the add_item method to add each item
        and quantity to the inventory. It also handles any errors or exceptions that might
        occur during the database connection, query execution, or data validation.

        :raise:
            mysql.connector.Error: If there is a problem with the database connection or query execution.
            ValueError: If the data fetched from the database is not valid or compatible with the add_item method.
        '''
        try:
            # Connect to DB
            db = SqlDatabase('Smart_Pantry')
            db.connect()
            query = ("SELECT IngredientName, Quantity FROM Fridge UNION SELECT IngredientName, Quantity FROM Freezer "
                     "UNION SELECT IngredientName, Quantity FROM Pantry")
            # Fetch the query result as a list of tuples
            result = db.execute_query(query)
            inventory_data = result
            try:
                # Loop through the result and add each item and quantity to the inventory
                for item, quantity in inventory_data:
                    self.add_item(item, quantity)
            except ValueError as e:
                # Print the error message if the data is invalid
                print(f"Invalid data: {e}")
        except mysql.connector.Error as err:
            # Print the error message if there is a problem with the database connection or query execution
            print(f"Error: {err}")
            # Handle the error as needed
        finally:
            # Close the cursor object
            db.disconnect()

    def add_item(self, item, quantity):
        '''
        Adds an item and its quantity to the inventory.
        This method takes an item name and a quantity as parameters
        and updates the items dictionary attribute of the object.
        It also checks and asserts some conditions on the parameters,
        such as the item name being a string, the quantity being a positive number,
        and the item not already existing in the inventory.
        :param: item (str): The name of the item to be added.
            quantity (int or float): The quantity of the item to be added.

        :raise: AssertionError: If the item name is not a string,
        the quantity is not a positive number,
        or the item already exists in the inventory.
        '''
        # Assert that the item parameter is a string
        # assert isinstance(item, str), "Item must be a string"
        # # Assert that the quantity parameter is a positive number
        # assert isinstance(
        # quantity, (int, float)) and quantity < 0, "Quantity must be a positive number"
        if item in self.items:
            self.items[item] += quantity
        else:
            # Assert that the item is not already in the inventory dictionary
            # assert item not in self.items, "Item already exists in the inventory"
            self.items[item] = quantity

    def display_list(self):
        '''
        Prints the shopping list of items and quantities.
        This method loops through the items dictionary attribute of the object
        and prints each item name and quantity in a formatted string.
        It also prints a header for the shopping list before the loop.
        '''
        # Print a header for the shopping list
        print('Shopping List:')
        # Loop through the items dictionary and print each item and quantity
        for item, quantity in self.items.items():
            print(f'{item}: {quantity}')

    def check_low_stock(self):
        '''
        Prints the items and quantities that are below a certain threshold.
        This method loops through the items dictionary attribute of the object
        and checks if the quantity of each item is less than 5.
        If so, it prints the item name and quantity in a formatted string.
        The threshold value can be adjusted as needed.
        '''
        print('Low-stock items:')
        for item, quantity in self.items.items():
            # Check if the quantity is below the threshold set
            if quantity < 5:  # Adjust the threshold as needed
                # Print the item name and quantity
                print(f'{item}: {quantity}')

    def user_add_item(self):
        '''
        Asks the user if they want to add an item and quantity to the inventory.
        This method loops until the user decides to stop adding items.
        It prompts the user to enter an item name and quantity, and validates the input.
        If the input is valid, it calls the add_item method to update the inventory.
        If the input is invalid, it raises a ValueError and asks the user to enter a valid input.
        '''
        # Loop until the user decides to stop adding items
        while True:
            # Ask the user if they want to add an item to the list
            user_input = input(
                'Do you want to add an item to the list? (yes/no): ')
            if user_input.lower() == 'yes':
                try:
                    # Get the item name from the user
                    item_to_add = input('Enter the item you want to add: ')
                    # Check if the item name is empty
                    if not item_to_add:
                        # Raise ValueError if the item name is empty
                        raise ValueError("Item name cannot be empty")
                    quantity_to_add = int(input('Enter the quantity: '))
                    # Check if the quantity is negative
                    if quantity_to_add < 0:
                        raise ValueError("Quantity cannot be negative")
                    # Add the item to the inventory
                    self.add_item(item_to_add, quantity_to_add)
                except ValueError as e:
                    # Print the error message if the user input is invalid
                    print(f"Invalid input: {e}")
                    print("Please enter a valid item name and quantity")
            else:
                # Break the loop if the user does not want to add more items
                break

'''
# Example usage:
shopping_list = ShoppingList()

# Populate shopping list from the database
# shopping_list.populate_from_database()

# Display initial shopping list
shopping_list.display_list()

# Check and display low-stock items
shopping_list.check_low_stock()

# Allow the user to add items
# shopping_list.user_add_item()

# Display the final shopping list
shopping_list.display_list()
'''


# Function outside of Class:
# Lauren S: User prompt for low-stock items
def populate_from_database(self):
    '''
    Populates the inventory and the shopping list with the data from the database.
    This method connects to the Smart_Pantry database and executes a query to select the
    ingredient name and quantity from the Fridge, Freezer, and Pantry tables.
    It then loops through the query result and calls the add_item method to add each item
    and quantity to the inventory. It also checks if the quantity of each item is below a
    certain threshold (5 by default) and asks the user if they want to add the item to the shopping list.
    If the user agrees, it prompts the user to enter the quantity of the item to add to
    the shopping list and calls the add_item method again.
    It also handles any errors or exceptions that might occur during the database connection,
    query execution, or user input.

    :raise:
        mysql.connector.Error: If there is a problem with the database connection or query execution.
        ValueError: If the user input is not valid or compatible with the add_item method.
    '''
    try:
        # Create a cursor object to execute queries
        cursor = self.connection.cursor()
        # Execute a query to select the ingredient name and quantity from different tables
        cursor.execute(
            "SELECT IngredientName, Quantity FROM Fridge UNION SELECT IngredientName, Quantity FROM Freezer UNION "
            "SELECT IngredientName, Quantity FROM Pantry")
        # Fetch the query result as a list of tuples
        inventory_data = cursor.fetchall()
        # Loop through the result and add each item and quantity to the inventory
        for item, quantity in inventory_data:
            self.add_item(item, quantity)
            # Check if the quantity is below the threshold set
            if quantity <= 5:  # Set a threshold for low stock
                # Ask the user if they want to add the item to the shopping list
                user_input = input(
                    f"{item} is low in stock. Do you want to add it to the shopping list? (yes/no): ")
                if user_input.lower() == 'yes':
                    # Get the quantity of the item to add to the shopping list from the user
                    shopping_quantity = int(
                        input(f"Enter the quantity of {item} to add to the shopping list: "))
                    # Add the item and quantity to the shopping list
                    self.add_item(item, shopping_quantity)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        # Handle the error as needed
    finally:
        cursor.close()


def fetch_out_of_date():
    '''Fetches the data from the database where ingredient is passed sellbydate, according to today's date.

    :return: list: A list of tuples containing the ingredient name, quantity, and sell by date.

    :raise:
        DbQueryError: If the ingredient is not found in the database.
        Exception: If there is any other error.
    '''

    try:
        # Connect to DB
        db = SqlDatabase('Smart_Pantry')
        db.connect()
        OOD_data = ()
        # Execute the query to select out of date ingredients
        query = ("SELECT ingredientname, quantity, sellbydate FROM ExpiredIngredients ORDER BY sellbydate;"
        )
        # Execute the query and store the result
        OOD_data = db.execute_query(query)
        if not OOD_data:
            # Raise a custom exception if no protein found
            raise DbQueryError("No rotting food in the kitchen, hurrah!", query, None)
        # Print each row of the result
        for row in OOD_data:
            print(row)
            print("\n")
        return OOD_data

    finally:
        # Disconnect from the database
        db.disconnect()


def fetch_expiring_ingredient_data():
    '''Fetches the data from the database where ingredients sellbydate is today or in the next two days,
    according to today's date.

    :return: list: A list of tuples containing the ingredient name, quantity, and sell by date.

    :raise:
        DbQueryError: If the ingredient is not found in the database.
        Exception: If there is any other error.
    '''

    try:
        # Connect to DB
        db = SqlDatabase('Smart_Pantry')
        db.connect()
        expiring_data = ()
        # Execute the query to select out of date ingredients
        query = ("SELECT ingredientname, quantity, sellbydate FROM ExpiringIngredients ORDER BY sellbydate;"
        )
        # Execute the query and store the result
        expiring_data = db.execute_query(query)
        if not expiring_data:
            # Raise a custom exception if no protein found
            raise DbQueryError("No items found that expire within the next few days", query, None)
        # Print each row of the result
        for row in expiring_data:
            print(row)
            print("\n")
        return expiring_data

    finally:
        # Disconnect from the database
        db.disconnect()


if __name__ == '__main__':
    # _add_item(stock_store='Fridge', values=('Beef', 'Protein', 2000, 'Grams', 450, '2025-07-30'))
    # update_inventory()
    # retrieve_stock(input("Which store do you want to see? Freezer, Fridge or Pantry?").lower())
    # stock_delete.delete_item("Freezer", "Diced Onion")
    # fetch_protein_data()
    shopping_list = ShoppingList()
    # ShoppingList.add_item()
    # fetch_out_of_date()
    # fetch_expiring_ingredient_data()
    # low_stock()
