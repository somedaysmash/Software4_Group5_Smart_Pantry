# Lauren S: Unit Testing Foundation
import mysql.connector
import unittest
from unittest.mock import patch, MagicMock, call
from tkinter import TclError
from io import StringIO
from utilities import (
    DbConnectionError,
    DbQueryError,
    SqlDatabase,
    assert_sell_by_date,
    StockDelete,
    update_inventory,
    retrieve_stock,
    fetch_protein_data,
    low_stock,
    ShoppingList
    )


class TestDBConnection(unittest.TestCase):
    def test_instance_creation(self):
        # Test that an instance of DbConnectionError can be created
        error_instance = DbConnectionError()
        self.assertIsInstance(error_instance, DbConnectionError)

    def test_inheritance(self):
        # Test that DbConnectionError inherits from the base Exception class
        self.assertTrue(issubclass(DbConnectionError, Exception))

    def test_custom_message(self):
        # Test that a custom error message can be provided
        custom_message = "Custom error message"
        error_instance = DbConnectionError(custom_message)
        self.assertEqual(str(error_instance), custom_message)

    def test_default_message(self):
        # Test that if no custom message is provided, a default message is used
        error_instance = DbConnectionError()
        self.assertEqual(str(error_instance), "")


class TestDBQueryError(unittest.TestCase):
    class DbQueryError(Exception):
        def __init__(self, message, query, params):
            super().__init__(message)
            self.query = query
            self.params = params

    def test_db_query_error_instance(self):
        # Mock data for testing
        error_message = "An error occurred"
        query = "SELECT * FROM table WHERE id = ?"
        params = (1,)

        # Create an instance of DbQueryError
        db_query_error = self.DbQueryError(error_message, query, params)

        # Assert that the instance is created correctly
        self.assertIsInstance(db_query_error, self.DbQueryError)

        # Assert that the properties are set as expected
        self.assertEqual(db_query_error.args[0], error_message)
        self.assertEqual(db_query_error.query, query)
        self.assertEqual(db_query_error.params, params)

    def test_db_query_error_str_representation(self):
        # Mock data for testing
        error_message = "An error occurred"
        query = "SELECT * FROM table WHERE id = ?"
        params = (1,)

        # Create an instance of DbQueryError
        db_query_error = self.DbQueryError(error_message, query, params)

        # Get the string representation of DbQueryError
        error_str = str(db_query_error)

        # Assert that the string representation is formatted as expected
        expected_str = f"{error_message}\nQuery: {query}\nParams: {params}"
        self.assertEqual(error_str, expected_str)


class SetUp(unittest.TestCase):

    def setup(self):
        # Initialize a SqlDatabase instance for testing
        self.database = SqlDatabase("test_database")

    def test_init_with_valid_database_name(self):
        # Ensure that SqlDatabase initializes correctly with a valid database name
        self.assertEqual(self.database.database, "test_database")

    def test_init_with_none_database_name(self):
        # Ensure that SqlDatabase raises an AssertionError when initialized with None
        with self.assertRaises(AssertionError):
            SqlDatabase(None)

    def test_connect_successful(self):
        # Mock the mysql.connector.connect method to simulate a successful connection
        with unittest.mock.patch("mysql.connector.connect") as mock_connect:
            self.database.connect()

        # Assert that the connect method was called
        mock_connect.assert_called_once_with(
            host=self.database.host,
            user=self.database.user,
            password=self.database.password,
            database=self.database.database
        )

    def test_connect_failure(self):
        # Mock the mysql.connector.connect method to simulate a connection failure
        with unittest.mock.patch("mysql.connector.connect", side_effect=mysql.connector.Error):
            with self.assertRaises(DbConnectionError):
                self.database.connect()

    def test_disconnect(self):
        # Mock the connection.close method
        self.database.connection = MagicMock()
        self.database.disconnect()

        # Assert that the connection.close method was called
        self.database.connection.close.assert_called_once()

    def test_execute_query_successful(self):
        # Mock the cursor.execute and cursor.fetchall methods
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [("result1",), ("result2",)]

        with unittest.mock.patch.object(self.database.connection, "cursor", return_value=mock_cursor):
            result = self.database.execute_query("SELECT * FROM table")

        # Assert that the query was executed and the result was fetched
        mock_cursor.execute.assert_called_once_with("SELECT * FROM table", None)
        self.assertEqual(result, [("result1",), ("result2",)])

    def test_execute_query_failure(self):
        # Mock the cursor.execute method to simulate a query execution failure
        with unittest.mock.patch.object(self.database.connection, "cursor") as mock_cursor:
            mock_cursor.execute.side_effect = mysql.connector.Error

            with self.assertRaises(mysql.connector.Error):
                self.database.execute_query("SELECT * FROM table")


class TestAssertSellByDate(unittest.TestCase):
    def test_valid_sell_by_date(self):
        # Test with a valid sell-by date
        valid_sell_by_date = "2023-12-31"
        try:
            assert_sell_by_date(valid_sell_by_date)
        except ValueError:
            self.fail("Valid sell-by date raised a ValueError")

    def test_invalid_sell_by_date_format(self):
        # Test with an invalid sell-by date format
        invalid_sell_by_date = "31-12-2023"
        with self.assertRaises(ValueError) as context:
            assert_sell_by_date(invalid_sell_by_date)
        self.assertEqual(str(context.exception), "Sell by date must be in the format YYYY-MM-DD")

    def test_non_string_sell_by_date(self):
        # Test with a non-string sell-by date
        non_string_sell_by_date = 12345
        with self.assertRaises(AssertionError) as context:
            assert_sell_by_date(non_string_sell_by_date)
        self.assertEqual(str(context.exception), "Sell by date must be a string")


class TestDeleteStock(unittest.TestCase):

    @patch('SmartPantryDB.SqlDatabase')
    def test_successful_deletion(self, mock_sql_database):
        # Arrange
        stock_delete = StockDelete("Freezer", "Diced Onion")

        # Act
        stock_delete.delete_item(stock_delete.stock_store, stock_delete.item_name)

        # Assert
        mock_sql_database.assert_called_with('Smart_Pantry')
        mock_sql_database.return_value.connect.assert_called_once()
        mock_sql_database.return_value.execute_query.assert_called_once_with(
            f"DELETE FROM {stock_delete.stock_store} WHERE IngredientName = '{stock_delete.item_name}'")
        mock_sql_database.return_value.connection.commit.assert_called_once()
        mock_sql_database.return_value.disconnect.assert_called_once()

    @patch('SmartPantryDB.SqlDatabase')
    def test_unsuccessful_deletion(self, mock_sql_database):
        # Arrange
        mock_sql_database.return_value.rowcount = 0
        stock_delete = StockDelete("Freezer", "Nonexistent Item")

        # Act and Assert
        with self.assertRaises(DbQueryError):
            stock_delete.delete_item(stock_delete.stock_store, stock_delete.item_name)

    @patch('SmartPantryDB.SqlDatabase', side_effect=DbQueryError("Test Error", "DELETE", None))
    def test_db_query_error_handling(self, mock_sql_database):
        # Arrange
        stock_delete = StockDelete("Freezer", "Some Item")

        # Act and Assert
        with self.assertRaises(DbQueryError):
            stock_delete.delete_item(stock_delete.stock_store, stock_delete.item_name)

        # Ensure that the mocked database was called
        mock_sql_database.assert_called_once_with()  # Adjust this based on your actual usage

    def test_invalid_table_name(self):
        # Arrange
        stock_delete = StockDelete("InvalidTable", "Some Item")

        # Act and Assert
        with self.assertRaises(AssertionError):
            stock_delete.delete_item(stock_delete.stock_store, stock_delete.item_name)

    def test_empty_item_name(self):
        # Arrange
        stock_delete = StockDelete("Freezer", "")

        # Act and Assert
        with self.assertRaises(AssertionError):
            stock_delete.delete_item(stock_delete.stock_store, stock_delete.item_name)


class TestUpdateInventory(unittest.TestCase):

    @patch('builtins.input', side_effect=['Fridge', 'Ingredient Name', '1', 'New Ingredient'])
    def test_update_ingredient_name_success(self):
        with self.assertRaises(SystemExit) as cm:
            update_inventory()
        self.assertEqual(cm.exception.code, None)

    @patch('builtins.input', side_effect=['Fridge', 'Quantity', '1', '5'])
    def test_update_quantity_success(self):
        with self.assertRaises(SystemExit) as cm:
            update_inventory()
        self.assertEqual(cm.exception.code, None)

    @patch('builtins.input', side_effect=['Fridge', 'Type of Ingredient', '1', 'New Type'])
    def test_update_type_success(self):
        with self.assertRaises(SystemExit) as cm:
            update_inventory()
        self.assertEqual(cm.exception.code, None)

    @patch('builtins.input', side_effect=['Fridge', 'Sell by Date', '1', '2023-12-31'])
    def test_update_sell_by_date_success(self):
        with self.assertRaises(SystemExit) as cm:
            update_inventory()
        self.assertEqual(cm.exception.code, None)

    @patch('builtins.input', side_effect=['InvalidTable', 'Ingredient Name', '1', 'New Ingredient'])
    def test_invalid_table_name(self):
        with self.assertRaises(SystemExit) as cm:
            update_inventory()
        self.assertEqual(cm.exception.code, 1)


class TestRetrieveStock(unittest.TestCase):
    @patch('your_module.SqlDatabase')
    def test_successful_retrieval(self, mock_sql_database):
        # Mock the database connection and result
        mock_result = [('Eggs', '12', 'Each'), ('Milk', '1', 'Liter')]
        mock_sql_database.return_value.execute_query.return_value = mock_result

        # Call the retrieve_stock function
        result = retrieve_stock("Fridge")

        # Assert that the result is as expected
        self.assertEqual(result, mock_result)

    @patch('your_module.SqlDatabase')
    def test_invalid_table_name(self):
        # Call the retrieve_stock function with an invalid table name
        with self.assertRaises(AssertionError):
            retrieve_stock("InvalidTable")

    @patch('your_module.SqlDatabase')
    def test_no_data_in_table(self, mock_sql_database):
        # Mock the database connection and result as empty
        mock_sql_database.return_value.execute_query.return_value = []

        # Call the retrieve_stock function
        with self.assertRaises(AssertionError):
            retrieve_stock("Fridge")

    @patch('your_module.SqlDatabase')
    def test_database_connection_failure(self, mock_sql_database):
        # Mock an exception during database connection
        mock_sql_database.side_effect = Exception("Connection error")

        # Call the retrieve_stock function
        with self.assertRaises(DbConnectionError):
            retrieve_stock("Fridge")

    @patch('your_module.SqlDatabase')
    def test_query_execution_failure(self, mock_sql_database):
        # Mock an exception during query execution
        mock_sql_database.return_value.execute_query.side_effect = DbQueryError("Query error", "SELECT * FROM Fridge",
                                                                                None)

        # Call the retrieve_stock function
        with self.assertRaises(DbQueryError):
            retrieve_stock("Fridge")


class TestFetchProteinData(unittest.TestCase):
    @patch('your_module.SqlDatabase')
    def test_valid_ingredient(self, mock_database):
        # Mocking the database connection and query result
        mock_connection = mock_database.return_value
        mock_connection.execute_query.return_value = [('Ingredient1', 100, 'grams')]

        result = fetch_protein_data('Ingredient1')

        # Assert that the database connection was called with the correct query
        mock_connection.execute_query.assert_called_once_with(
            "SELECT IngredientName, Quantity, UnitOfMeasurement "
            "FROM Pantry WHERE IngredientName = 'Ingredient1' "
            "UNION "
            "SELECT IngredientName, Quantity, UnitOfMeasurement "
            "FROM Fridge WHERE IngredientName = 'Ingredient1' "
            "UNION "
            "SELECT IngredientName, Quantity, UnitOfMeasurement "
            "FROM Freezer WHERE IngredientName = 'Ingredient1'"
        )

        # Assert that the function returned the expected result
        self.assertEqual(result, [('Ingredient1', 100, 'grams')])

    @patch('your_module.SqlDatabase')
    def test_invalid_ingredient(self, mock_database):
        # Mocking the database connection and query result for an invalid ingredient
        mock_connection = mock_database.return_value
        mock_connection.execute_query.return_value = []

        with self.assertRaises(DbQueryError):
            # Assert that the function raises a DbQueryError for an invalid ingredient
            fetch_protein_data('NonexistentIngredient')

    @patch('your_module.SqlDatabase', side_effect=Exception('Test error'))
    def test_database_error(self):
        # Mocking the database connection to simulate a database error
        with self.assertRaises(Exception):
            # Assert that the function raises an exception for a database error
            fetch_protein_data('Ingredient1')

    @patch('your_module.Tk', side_effect=TclError('Test Tkinter error'))
    def test_tkinter_error(self):
        # Mocking Tkinter to simulate a Tkinter error
        with self.assertRaises(TclError):
            # Assert that the function raises a TclError for a Tkinter error
            fetch_protein_data('Ingredient1')


class TestLowStock(unittest.TestCase):
    @patch('your_module.SqlDatabase')
    def test_low_stock_valid_inputs(self, mock_sql_db):
        # Mock the database connection
        mock_db_instance = mock_sql_db.return_value
        mock_db_instance.execute_query.return_value = [('Ingredient1', 50.0, 'Grams')]

        # Mock user input for adding to the shopping list
        with patch('builtins.input', side_effect=['yes']):
            shopping_list = low_stock()

        # Assert the shopping list contains the expected item
        self.assertEqual(shopping_list, [('Ingredient1', 50.0, 'Grams')])

    @patch('your_module.SqlDatabase')
    def test_low_stock_no_low_stock_ingredients(self, mock_sql_db):
        # Mock the database connection
        mock_db_instance = mock_sql_db.return_value
        mock_db_instance.execute_query.return_value = []

        # Assert that DbQueryError is raised when there are no low stock ingredients
        with self.assertRaises(DbQueryError):
            low_stock()

    @patch('your_module.SqlDatabase')
    def test_low_stock_invalid_user_input(self, mock_sql_db):
        # Mock the database connection
        mock_db_instance = mock_sql_db.return_value
        mock_db_instance.execute_query.return_value = [('Ingredient2', 30.0, 'Grams')]

        # Mock user input for adding to the shopping list
        with patch('builtins.input', side_effect=['invalid']):
            # Assert that ValueError is raised for invalid user input
            with self.assertRaises(ValueError):
                low_stock()

    @patch('your_module.SqlDatabase')
    def test_low_stock_database_error(self, mock_sql_db):
        # Mock the database connection to raise a DbConnectionError
        mock_db_instance = mock_sql_db.return_value
        mock_db_instance.connect.side_effect = DbConnectionError('Connection error')

        # Assert that DbConnectionError is raised when there is a database connection error
        with self.assertRaises(DbConnectionError):
            low_stock()


class TestShoppingList(unittest.TestCase):
    def test_connect_to_database_success(self):
        # Mock the mysql.connector.connect method to simulate a successful connection
        with patch('mysql.connector.connect', return_value=MagicMock()) as mock_connect:
            shopping_list = ShoppingList()
            shopping_list.connect_to_database('host', 'user', 'password', 'database')
            # Assert that the connection attribute is not None
            self.assertIsNotNone(shopping_list.connection)
            # Assert that the connect method was called with the correct parameters
            mock_connect.assert_called_once_with(
                host='host', user='user', password='password', database='database')

    def test_connect_to_database_error(self):
        # Mock the mysql.connector.connect method to simulate a connection error
        with patch('mysql.connector.connect', side_effect=mysql.connector.Error("Connection Error")):
            shopping_list = ShoppingList()
            shopping_list.connect_to_database('host', 'user', 'password', 'database')
            # Assert that the connection attribute is None in case of an error
            self.assertIsNone(shopping_list.connection)

    def test_populate_from_database_success(self):
        # Mock the cursor.execute and cursor.fetchall methods for a successful database query
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [('Item1', 10), ('Item2', 20)]

        with patch.object(ShoppingList, 'connection', MagicMock()):
            shopping_list = ShoppingList()
            shopping_list.populate_from_database()

            # Assert that the add_item method was called for each item in the database
            shopping_list.add_item.assert_has_calls([
                call('Item1', 10),
                call('Item2', 20)
            ], any_order=True)

    def test_populate_from_database_query_error(self):
        # Mock the cursor.execute method to simulate a database query error
        mock_cursor = MagicMock()
        mock_cursor.execute.side_effect = mysql.connector.Error("Query Error")
        with patch.object(ShoppingList, 'connection', return_value=mock_cursor):
            shopping_list = ShoppingList()
            shopping_list.connection = MagicMock()
            # Assert that the method raises a mysql.connector.Error in case of a query error
            with self.assertRaises(mysql.connector.Error):
                shopping_list.populate_from_database()

    def test_add_item_success(self):
        shopping_list = ShoppingList()
        shopping_list.add_item('NewItem', 5)
        # Assert that the item and quantity are added to the items dictionary
        self.assertEqual(shopping_list.items, {'NewItem': 5})

    def test_add_item_existing_item_error(self):
        shopping_list = ShoppingList()
        # Add an initial item
        shopping_list.items = {'ExistingItem': 10}
        # Assert that adding an existing item raises an AssertionError
        with self.assertRaises(AssertionError):
            shopping_list.add_item('ExistingItem', 5)

    def test_add_item_invalid_quantity_error(self):
        shopping_list = ShoppingList()
        # Assert that adding an item with an invalid quantity raises an AssertionError
        with self.assertRaises(AssertionError):
            shopping_list.add_item('NewItem', -5)

    def test_display_list(self):
        shopping_list = ShoppingList()
        shopping_list.add_item('Item1', 10)

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            shopping_list.display_list()
            output = mock_stdout.getvalue().strip()

        expected_output = 'Shopping List:\nItem1: 10'
        self.assertEqual(output, expected_output)

    def test_check_low_stock(self):
        shopping_list = ShoppingList()
        shopping_list.add_item('LowStockItem', 3)

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            shopping_list.check_low_stock()
            output = mock_stdout.getvalue().strip()

        expected_output = 'Low-stock items:\nLowStockItem: 3'
        self.assertEqual(output, expected_output)

    @patch('builtins.input', side_effect=['yes', 'Item2', '5', 'no'])
    def test_user_add_item(self, mock_input):
        shopping_list = ShoppingList()

        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            shopping_list.user_add_item()
            output = mock_stdout.getvalue().strip()

        expected_output = ('Do you want to add an item to the list? (yes/no): '
                           'Enter the item you want to add: Enter the quantity:'
                           )

        self.assertEqual(output, expected_output)
        mock_input.assert_has_calls([
            call('Do you want to add an item to the list? (yes/no): '),
            call('Enter the item you want to add: '),
            call('Enter the quantity: '),
            call('no')
        ], any_order=False)
        self.assertEqual(shopping_list.items, {'Item2': 5})


class TestPopulateFromDatabase(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestPopulateFromDatabase, self).__init__(*args, **kwargs)
        self.items = []

    def populate_from_database(self, data_from_database):
        for row in data_from_database:
            name, quantity = row
            self.add_item(name, quantity)

    def add_item(self, name, quantity):
        item = {'name': name, 'quantity': quantity}
        self.items.append(item)

    @patch('mysql.connector.connect')
    def test_populate_from_database_querying(self, mock_connect):
        # Mock the cursor and its execute method
        mock_cursor = mock_connect.return_value.cursor.return_value
        mock_cursor.fetchall.return_value = [('Ingredient1', 10), ('Ingredient2', 3)]

        # Create an instance of YourClass
        your_instance = TestPopulateFromDatabase()

        # Call the method to test
        your_instance.populate_from_database(mock_cursor.fetchall.return_value)

        # Assert that add_item is called with the expected arguments
        expected_calls = [call('Ingredient1', 10), call('Ingredient2', 3)]
        mock_cursor.add_item.assert_has_calls(expected_calls, any_order=True)

    @patch('builtins.input', side_effect=['yes', '5'])
    def test_populate_from_database_user_input(self, mock_input):
        # Create an instance of your class
        pantry_instance = TestPopulateFromDatabase()

        # Call the method to test
        pantry_instance.populate_from_database([])  # Provide the required parameter

        # Assert that add_item is called with the expected arguments for shopping list addition
        mock_input.assert_called_with('Ingredient1', 5)

    @patch('sys.stdout', new_callable=StringIO)
    @patch('mysql.connector.connect')
    def test_populate_from_database_exception_handling(self, mock_connect, mock_stdout):
        # Mock the cursor to raise a simulated exception
        mock_cursor = mock_connect.return_value.cursor.return_value
        mock_cursor.execute.side_effect = mysql.connector.Error("Simulated error")

        # Create an instance of your class
        pantry_instance = TestPopulateFromDatabase()

        # Call the method to test
        pantry_instance.populate_from_database([])  # Provide the required parameter

        # Assert that the error is handled appropriately (e.g., printed to console)
        self.assertTrue("Simulated error" in mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
