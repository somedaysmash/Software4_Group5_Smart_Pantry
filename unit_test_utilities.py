
# Lauren S: Unit Testing Foundation
import mysql.connector
import unittest
from unittest.mock import patch, MagicMock, call
from tkinter import TclError
from io import StringIO
from utilities import DbConnectionError, DbQueryError, SqlDatabase, metrify


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


class TestMetrifyFunction(unittest.TestCase):

    def test_valid_conversion(self):
        # Test a valid conversion from grams to kilograms
        result = metrify('g', 'kg', 500)
        self.assertEqual(result, 0.5)

        # Test a valid conversion from milliliters to liters
        result = metrify('ml', 'liters', 1000)
        self.assertEqual(result, 1)

    def test_invalid_input_unit(self):
        # Test with an invalid input unit
        with self.assertRaises(ValueError):
            metrify('invalid_unit', 'kg', 500)

    def test_invalid_output_unit(self):
        # Test with an invalid output unit
        with self.assertRaises(ValueError):
            metrify('g', 'invalid_unit', 500)

    def test_invalid_amount(self):
        # Test with an invalid amount (negative number)
        with self.assertRaises(ValueError):
            metrify('g', 'kg', -500)

    def test_invalid_unit_and_amount(self):
        # Test with both an invalid unit and amount
        with self.assertRaises(ValueError):
            metrify('invalid_unit', 'invalid_unit', -500)


if __name__ == '__main__':
    unittest.main()
    