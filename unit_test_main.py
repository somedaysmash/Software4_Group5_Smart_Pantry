# Lauren S: Unit Testing Foundation
import unittest
from unittest.mock import patch
from main import add_stock_item_fridge, run_fridge, update_fridge, delete_stock_item_by_name


class TestMainFunctions(unittest.TestCase):
    @patch('main.requests.put')
    def test_add_stock_item_fridge(self, mock_put):
        # Arrange
        mock_put.return_value.status_code = 200
        mock_put.return_value.json.return_value = {'status': 'success'}

        # Act
        result = add_stock_item_fridge(
            'Tomato',
            'Vegetable',
            10,
            'kg',
            5,
            '2023-12-31',
            'fridge'
        )
        # inspect response data
        print('Here is the stock:', result)

        # Assert
        mock_put.assert_called_with(
            'http://127.0.0.1:5000/add_item_fridge',
            headers={'content-type': 'application/json'},
            data='{"_IngredientName": "Tomato", '
                 '"_TypeOfIngredient": "Vegetable", '
                 '"_Quantity": 10, '
                 '"_UnitOfMeasurement": "kg", '
                 '"_MinimumQuantityNeeded": 5, '
                 '"_SellByDate": "2023-12-31"}'
        )
        self.assertEqual(result, {'status': 'success'})

    @patch('builtins.input', side_effect=['Y', 'Tomato', 'Vegetable', '10', 'kg', '5', '2023-12-31'])
    def test_run_fridge(self):
        # Arrange
        expected_output = 'We have added your item\nSee you soon!'

        # Act
        with patch('builtins.print') as mock_print:
            run_fridge()

        # Assert
        mock_print.assert_called_with(expected_output)

    @patch('builtins.input', return_value='N')
    def test_run_fridge_no_add_item(self):
        # Arrange
        expected_output = 'See you soon!'

        # Act
        with patch('builtins.print') as mock_print:
            run_fridge()

        # Assert
        mock_print.assert_called_with(expected_output)

    class TestYourModule(unittest.TestCase):
        @patch('main.requests.put')
        def test_update_fridge(self, mock_put):
            # Arrange
            mock_put.return_value.status_code = 201
            mock_put.return_value.json.return_value = {'status': 'success'}

            # Act
            result = update_fridge()

            # Assert
            mock_put.assert_called_with('http://127.0.0.1:5000/update/fridge')
            self.assertEqual(result, {'status': 'success'})

    @patch('main.requests.delete')
    def test_delete_stock_by_name(self, mock_requests_delete):
        # Arrange
        mock_requests_delete.return_value.status_code = 200
        mock_requests_delete.return_value.json.return_value = {'status': 'success'}

        stock_store_input = 'fridge'
        item_name_input = 'Tomato'

        # Act
        result = delete_stock_item_by_name(stock_store_input, item_name_input)

        # Assert
        mock_requests_delete.assert_called_with(f"http://127.0.0.1:5000/delete/{stock_store_input}/{item_name_input}")
        self.assertEqual(result, {'status': 'success'})


if __name__ == '__main__':
    unittest.main()
