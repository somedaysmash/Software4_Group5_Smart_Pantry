# Lauren S: Unit Testing Foundation
import unittest
# import json
from app import app
from unittest.mock import patch
# from app import welcome, kitchen, ingredient, new_item_fridge, update_fridge_stock, delete_item_from_stock


class TestWelcomeRoute(unittest.TestCase):
    def test_welcome_route(self):
        client = app.test_client()
        response = client.get('/')
        assert response.status_code == 200
        assert b'Welcome' in response.data


class TestKitchenRoute(unittest.TestCase):
    def test_kitchen_route(self):
        client = app.test_client()
        response = client.post('/kitchen', data={'stock_store': 'Fridge',
                                                 'itemName': 'item1',
                                                 'typeOfIngredient': 'type1'
                                                 })
        assert response.status_code == 200
        assert b'Updated Kitchen' in response.data


class TestIngredientRoute(unittest.TestCase):
    @patch('app.get_random_recipe')
    def test_ingredient_route(self, mock_get_random_recipe):
        mock_get_random_recipe.return_value = {'hits': [{'recipe': {'label': 'Recipe1'}}]}
        client = app.test_client()
        response = client.post('/ingredient', data={'query': 'test'})
        assert response.status_code == 200
        assert b'Recipe1' in response.data


class TestNewItemFridge(unittest.TestCase):
    def test_new_item_fridge(self):
        # Mock input data for a new fridge item
        new_item_data = {
            '_IngredientName': 'Tomato',
            '_TypeOfIngredient': 'Vegetable',
            '_Quantity': 5,
            '_UnitofMeasurement': 'pcs',
            '_MinimumQuantityNeeded': 2,
            '_SellByDate': '2023-12-31'
        }

        # Call the new_item_fridge function
        response = app.test_client().put('/add_item_fridge', json=new_item_data)

        # Assert that the item is added correctly
        assert response.status_code == 200
        assert response.json == new_item_data

        # def test_new_item_fridge_edge_cases(self):
        #     # Test with minimum and maximum values
        #     min_max_data = {
        #         '_IngredientName': 'Tomato',
        #         '_TypeOfIngredient': 'Vegetable',
        #         '_Quantity': 1,
        #         '_UnitofMeasurement': 'pcs',
        #         '_MinimumQuantityNeeded': 1,
        #         '_SellByDate': '2023-12-31'
        #     }
        #
        #     # Test with invalid data
        #     invalid_data = {
        #         '_IngredientName': 'Tomato',
        #         '_TypeOfIngredient': 'Vegetable',
        #         '_Quantity': 'invalid',
        #         '_UnitofMeasurement': 'pcs',
        #         '_MinimumQuantityNeeded': 2,
        #         '_SellByDate': 'invalid_date'
        #     }
        #
        #     # Test with minimum and maximum values
        #     response_min_max = app.test_client().put('/add_item_fridge', json=min_max_data)
        #     assert response_min_max.status_code == 200
        #     assert response_min_max.json == min_max_data
        #
        #     # Test with invalid data
        #     response_invalid = app.test_client().put('/add_item_fridge', json=invalid_data)
        #     assert response_invalid.status_code == 400  # Assuming 400 for validation error


class TestUpdateFridgeStock(unittest.TestCase):
    def test_update_fridge_stock(self):
        # Mock input data for updating fridge stock
        update_data = {}

        # Call the update_fridge_stock function
        response = app.test_client().put('/update/fridge', json=update_data)

        # Assert that the inventory is updated correctly
        assert response.status_code == 200
        assert response.json == {"message": "Fridge ingredient has been updated."}

    def test_update_fridge_stock_specific_data(self):
        # Mock input data for updating fridge stock with specific data
        specific_update_data = {'specific_key': 'specific_value'}

        # Call the update_fridge_stock function with specific data
        response_specific_update = app.test_client().put('/update/fridge', json=specific_update_data)

        # Assert that the specific data is handled correctly
        assert response_specific_update.status_code == 200
        assert response_specific_update.json == {"message": "Fridge ingredient has been updated."}


class TestDeleteItemFromStock(unittest.TestCase):
    def test_delete_item_from_stock(self):
        # Mock input data for deleting an item from the fridge
        stock_store = 'Fridge'
        item_name = 'Tomato'

        # Call the delete_item_from_stock function
        response = app.test_client().delete(f'/delete/{stock_store}/{item_name}')

        # Assert that the item is deleted correctly
        assert response.status_code == 200
        assert response.json == {"message": f"{item_name} successfully deleted from {stock_store}."}

    def test_delete_nonexistent_item_from_stock(self):
        # Mock input data for deleting a nonexistent item from the fridge
        stock_store = 'Fridge'
        item_name = 'NonexistentItem'

        # Call the delete_item_from_stock function
        response_nonexistent = app.test_client().delete(f'/delete/{stock_store}/{item_name}')

        # Assert that the response indicates that the item does not exist
        assert response_nonexistent.status_code == 404  # Assuming 404 for item not found


if __name__ == '__main__':
    unittest.main()
