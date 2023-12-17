import mysql.connector
from config import *


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


def metrify(input_unit, output_unit, amount):
    ''' Converts the input unit to the output unit, based on the amount of the input unit.

    :param input_unit: str: The unit of measurement of the input amount.
    :param output_unit: str: The unit of measurement to convert to.
    :param amount: int or float: The amount of the input unit to convert.

    :return: float: The amount of the output unit after conversion.

    :raise:
        ValueError: If the input unit is not a valid unit of measurement.
        ValueError: If the output unit is not a valid unit of measurement.
        ValueError: If the amount is not a positive number.
    '''

    # Define a dictionary of units and their conversion factors
    units = {
        'g': 1,
        'grams': 1,
        'kg': 1000,
        'oz': 28.3495,
        'lb': 453.592,
        'ml': 1,
        'mls': 1,
        'mililiters': 1,
        'liters': 1000,
        'l': 1000,
        'fl oz': 29.5735,
        'pt': 473.176,
        'qt': 946.353,
        'gal': 3785.41,
        'teaspoon': 5,
        'tablespoon': 15,
        'cup': 240,
        'stick': 110
    }

    # Check if the input unit is a valid unit of measurement
    if input_unit not in units or output_unit not in units:
        return amount

    # Convert the amount to grams or milliliters
    amount_in_g_or_ml = amount * units[input_unit]
    # Convert the amount from grams or milliliters to the output unit
    amount_in_output_unit = amount_in_g_or_ml / units[output_unit]

    return amount_in_output_unit

