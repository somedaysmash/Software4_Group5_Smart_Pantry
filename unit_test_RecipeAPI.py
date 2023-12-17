import unittest
from unittest.mock import MagicMock, patch
from RecipeAPI import *


class TestRecipeAPIFunctions:
    @patch('RecipeAPI.requests.get')
    def test_get_random_recipe(self, mock_requests_get):
        # Set up a mock response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'hits': [{
                'recipe': {'label': 'Test Recipe', 'ingredients': [{'quantity': 100, 'measure': 'g', 'food': 'Ingredient'}]}
            }]
        }
        mock_requests_get.return_value = mock_response

        # Call the function
        result = get_random_recipe('test_query')

        # Assertions
        self.assertIsNotNone(result)
        self.assertEqual(result['label'], 'Test Recipe')
        self.assertEqual(len(result['ingredients']), 1)

    @patch('RecipeAPI.see_more_recipes', side_effect=['yes', 'no'])
    @patch('RecipeAPI.recipe_search_by_ingredient')
    def test_see_more_recipes(self, mock_recipe_search, mock_input):
        # Set up a mock response
        mock_response = MagicMock()
        mock_response.get.return_value = {'hits': [{'recipe': {'label': 'Recipe1', 'url': 'url1'}}]}
        mock_recipe_search.return_value = mock_response

        # Call the function
        see_more_recipes()

        # Assertions
        mock_recipe_search.assert_called_once_with('test_ingredient', 1, None)

    @patch('RecipeAPI.requests.get')
    def test_next_page_request(self, mock_requests_get):
        # Set up a mock response
        mock_response = MagicMock()
        mock_response.json.return_value = {'hits': [{'recipe': {'label': 'Recipe1', 'url': 'url1'}}]}
        mock_requests_get.return_value = mock_response

        # Call the function
        result = next_page_request('test_url')

        # Assertions
        self.assertIsNotNone(result)
        mock_requests_get.assert_called_once_with('test_url')

    @patch('RecipeAPI.open', create=True)
    def test_create_shopping_list(self, mock_open):
        # Call the function
        create_shopping_list([('Ingredient1', 100), ('Ingredient2', 200)])

        # Assertions
        mock_open.assert_called_once_with('static/assets/shopping_list.txt', 'w')
        mock_open().write.assert_called_once_with(' Ingredient1 (100 g)\n Ingredient2 (200 g)\n')

    @patch('RecipeAPI.requests.get')
    def test_get_random_recipe_success(self, mock_get):
        # Set up a mock response for a successful API call
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'hits': [{'recipe': {'label': 'Recipe1', 'url': 'url1'}}]
        }
        mock_get.return_value = mock_response

        # Call the function
        result = get_random_recipe('test_query')

        # Assertions
        self.assertIsNotNone(result)
        self.assertEqual(result['label'], 'Recipe1')

    @patch('RecipeAPI.requests.get')
    def test_get_random_recipe_failure(self, mock_get):
        # Set up a mock response for a failed API call
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        # Call the function
        result = get_random_recipe('test_query')

        # Assertions
        self.assertIsNone(result)

    @patch('RecipeAPI.requests.get')
    def test_recipe_search_by_ingredient_success(self, mock_get):
        # Set up a mock response for a successful API call
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'hits': [{'recipe': {'label': 'Recipe1', 'url': 'url1'}}],
            'count': 1,
            'from': 1,
            'to': 1
        }
        mock_get.return_value = mock_response

        # Call the function
        result = recipe_search_by_ingredient('test_ingredient')

        # Assertions
        self.assertIsNotNone(result)
        self.assertEqual(result['count'], 1)

    @patch('RecipeAPI.requests.get')
    def test_recipe_search_by_ingredient_failure(self, mock_get):
        # Set up a mock response for a failed API call
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        # Call the function
        result = recipe_search_by_ingredient('test_ingredient')

        # Assertions
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
