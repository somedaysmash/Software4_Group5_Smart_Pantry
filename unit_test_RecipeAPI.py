# Lauren S: Unit Testing Foundation
import unittest
from unittest.mock import patch, mock_open, MagicMock
import requests
from RecipeAPI import (DbConnectionError,
                       get_random_recipe,
                       recipe_search_by_ingredient,
                       next_page_request,
                       create_shopping_list,
                       run,
                       check_stock_for_recipe,
                       update_pantry,
                       )


class TestGetRandomRecipe(unittest.TestCase):

    def test_get_random_recipe_successful_api_call(self):
        # Mock the requests.get method to simulate a successful API response
        with self.assertRaises(requests.exceptions.RequestException):
            data = get_random_recipe('protein')
        self.assertIsNotNone(data)

    def test_get_random_recipe_network_error(self):
        # Mock the requests.get method to simulate a network error
        with self.assertRaises(requests.exceptions.RequestException):
            data = get_random_recipe('protein')
        self.assertIsNone(data)

    def test_get_random_recipe_data_format(self):
        # Mock the requests.get method to simulate a successful API response
        with self.assertRaises(requests.exceptions.RequestException):
            data = get_random_recipe('protein')
        self.assertTrue('label' in data and 'ingredients' in data and 'totalWeight' in data)

    def test_get_random_recipe_invalid_query_parameter(self):
        # Mock the requests.get method to simulate an API response with no data
        with self.assertRaises(requests.exceptions.RequestException):
            data = get_random_recipe('')
        self.assertIsNone(data)


class TestRecipeSearchByIngredient(unittest.TestCase):

    @patch('requests.get')
    def test_recipe_search_by_ingredient_success(self, mock_requests_get):
        # Setup mock response for a successful API call
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'hits': [{'recipe': {'label': 'Recipe 1'}}]}

        # Configure the mock to return the mock response
        mock_requests_get.return_value = mock_response

        # Call the function with test data
        result = recipe_search_by_ingredient()

        # Assertions
        self.assertIsNotNone(result)
        self.assertIn('hits', result)
        self.assertEqual(len(result['hits']), 1)
        self.assertEqual(result['hits'][0]['recipe']['label'], 'Recipe 1')

    @patch('requests.get')
    def test_recipe_search_by_ingredient_network_error(self, mock_requests_get):
        # Setup mock response for a network error
        mock_requests_get.side_effect = Exception('Network error')

        # Call the function with test data
        result = recipe_search_by_ingredient()

        # Assertions
        self.assertIsNone(result)


class TestNextPageRequest(unittest.TestCase):

    @patch('requests.get')
    def test_next_page_request_success(self, mock_requests_get):
        # Mocking a successful API response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'hits': [{'recipe': {'label': 'Recipe 1'}}],
                                           '_links': {'next': {'href': 'next_page_url'}}}
        mock_requests_get.return_value = mock_response

        # Call the function with a sample URL
        result = next_page_request('sample_url')

        # Assertions
        self.assertIsNotNone(result)
        self.assertIn('hits', result)
        self.assertIn('_links', result)
        self.assertIn('next', result['_links'])
        self.assertEqual(result['_links']['next']['href'], 'next_page_url')

    @patch('requests.get')
    def test_next_page_request_network_error(self, mock_requests_get):
        # Mocking a network error
        mock_requests_get.side_effect = requests.RequestException('Network error')

        # Call the function with a sample URL
        result = next_page_request('sample_url')

        # Assertions
        self.assertIsNone(result)


class TestCreateShoppingList(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open)
    @patch('builtins.print')
    def test_create_shopping_list(self, mock_print, mock_file):
        # Test Case 1: Verify the shopping list is created correctly with provided data
        test_missing_ingredients = [('ingredient1', 100), ('ingredient2', 150)]
        expected_content = 'Shopping List:\n- ingredient1 (100 g)\n- ingredient2 (150 g)\n'

        create_shopping_list(test_missing_ingredients)

        # Assertions
        mock_file.assert_called_once_with('shopping_list.txt', 'w')
        mock_file().write.assert_called_once_with(expected_content)

        # Test Case 2: Verify the correct message is printed to the console
        mock_print.assert_called_once_with('Your shopping list can be found here: shopping_list.txt')

    @staticmethod
    def create_shopping_list(missing_ingredients):
        # Construct the content for the shopping list
        shopping_list_content = "Shopping List:\n"
        for ingredient, quantity in missing_ingredients:
            shopping_list_content += f"- {ingredient} ({quantity} g)\n"

        # Write the content to the shopping_list.txt file
        with open('shopping_list.txt', 'w') as shopping_list_file:
            shopping_list_file.write(shopping_list_content)

        # Print a message to the console
        print('Your shopping list can be found here: shopping_list.txt')


class TestRun(unittest.TestCase):
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['yes'])
    @patch('your_module.recipe_search_by_ingredient')
    @patch('your_module.next_page_request')
    @patch('your_module.check_stock_for_recipe')
    @patch('your_module.create_shopping_list')
    def test_run_with_more_recipes(self, mock_create_shopping_list, mock_check_stock_for_recipe, mock_next_page_request,
                                   mock_recipe_search, mock_input, mock_print):
        # Mock the necessary functions and input
        mock_input.return_value = 'yes'
        mock_recipe_search.return_value = {'count': 2, 'hits': [{'recipe': {'label': 'Recipe 1', 'url': 'url1'}},
                                                                {'recipe': {'label': 'Recipe 2', 'url': 'url2'}}]}
        mock_next_page_request.return_value = {'hits': [{'recipe': {'label': 'Recipe 3', 'url': 'url3'}}]}
        mock_check_stock_for_recipe.return_value = [('ingredient1', 100)]

        # Call the run function
        run()

        # Assertions
        mock_print.assert_called_with('Would you like to see more recipes? (yes/no) ')
        mock_create_shopping_list.assert_called_once_with([('ingredient1', 100)])

        # Lauren S: Do we need to add more assertions?


class TestCheckStockForRecipe(unittest.TestCase):
    @patch('RecipeAPI.SqlDatabase')
    def test_check_stock_for_recipe(self, mock_sql_database):
        # Setup mock database and test data
        mock_db_instance = mock_sql_database.return_value
        mock_db_instance.execute_query.side_effect = [
            [('ingredient1', 100)],  # Fridge has 100g of ingredient1
            [],  # Freezer has none
            [('ingredient1', 200)]  # Pantry has 200g of ingredient1
        ]

        # Call the function with test data
        ingredients_and_weight = [('ingredient1', 150)]  # Recipe requires 150g of ingredient1
        result = check_stock_for_recipe(ingredients_and_weight)

        # Assertions
        self.assertEqual(result, [('ingredient1', 50)])  # 150g - 100g - 0g = 50g missing


class TestUpdatePantry(unittest.TestCase):

    @patch('your_module.SqlDatabase')
    def test_update_pantry_success(self, mock_sql_database):
        # Setup mock database instance
        mock_db_instance = mock_sql_database.return_value
        mock_db_instance.execute_query.side_effect = [
            # Result for Fridge
            [(10,)],  # Quantity available in Fridge
            # Result for Freezer
            [(5,)],  # Quantity available in Freezer
            # Result for Pantry
            [(15,)],  # Quantity available in Pantry
        ]

        # Call the function with test data
        ingredients_and_weight = [('Ingredient1', 7), ('Ingredient2', 3)]
        update_pantry(ingredients_and_weight)

        # Assertions
        expected_queries = [
            # Query to get quantity from Fridge for Ingredient1
            ("SELECT Quantity FROM Fridge WHERE IngredientName = %s", ('Ingredient1',)),
            # Query to get quantity from Freezer for Ingredient1
            ("SELECT Quantity FROM Freezer WHERE IngredientName = %s", ('Ingredient1',)),
            # Query to get quantity from Pantry for Ingredient1
            ("SELECT Quantity FROM Pantry WHERE IngredientName = %s", ('Ingredient1',)),
            # Query to update quantity in Fridge for Ingredient1
            ("UPDATE Fridge SET Quantity = %s WHERE IngredientName = %s", (3, 'Ingredient1')),
            # Query to get quantity from Fridge for Ingredient2
            ("SELECT Quantity FROM Fridge WHERE IngredientName = %s", ('Ingredient2',)),
            # Query to get quantity from Freezer for Ingredient2
            ("SELECT Quantity FROM Freezer WHERE IngredientName = %s", ('Ingredient2',)),
            # Query to get quantity from Pantry for Ingredient2
            ("SELECT Quantity FROM Pantry WHERE IngredientName = %s", ('Ingredient2',)),
            # Query to update quantity in Pantry for Ingredient2
            ("UPDATE Pantry SET Quantity = %s WHERE IngredientName = %s", (12, 'Ingredient2')),
        ]
        for call_args, expected_args in zip(mock_db_instance.execute_query.call_args_list, expected_queries):
            self.assertEqual(call_args, expected_args)

        # Ensure the disconnect method is called
        mock_db_instance.disconnect.assert_called_once()

    @patch('your_module.SqlDatabase')
    def test_update_pantry_db_connection_error(self, mock_sql_database):
        # Setup mock database instance to raise DbConnectionError
        mock_sql_database.side_effect = DbConnectionError("Connection failed")

        # Call the function with test data
        ingredients_and_weight = [('Ingredient1', 7), ('Ingredient2', 3)]

        # Assertions
        with self.assertRaises(DbConnectionError):
            update_pantry(ingredients_and_weight)

        # Ensure the disconnect method is called even in case of connection error
        mock_sql_database.return_value.disconnect.assert_called_once()


if __name__ == '__main__':
    unittest.main()
