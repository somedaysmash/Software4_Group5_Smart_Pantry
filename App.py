# FLASK AND @ROUTES GO HERE
import mysql.connector
from flask import Flask, jsonify, request, send_file
from utilities import add_item_fridge, add_item_freezer, add_item_pantry, update_inventory
from utilities import delete_item, _add_item, _connect_to_db


app = Flask(__name__)

@app.route('/')
def welcome():
    return '''<h1>Welcome to Smart Pantry</h1>'''

@app.route('/add_item_fridge', methods=['PUT'])
def new_item_fridge():
    new_fridge_stock = request.get_json()
    add_item_fridge(
        _IngredientName=new_fridge_stock['_IngredientName'],
        _TypeOfIngredient=new_fridge_stock['_TypeOfIngredient'],
        _Quantity=new_fridge_stock['_Quantity'],
        _UnitofMeasurement=new_fridge_stock['_UnitofMeasurement'],
        _MinimumQuantityNeeded=new_fridge_stock['_MinimumQuantityNeeded'],
        _SellByDate=new_fridge_stock['_SellByDate']
    )
    return new_fridge_stock


@app.route('/update/fridge', methods=['PUT'])
def update_fridge_stock():
    successful = update_inventory()
    if successful:
        return jsonify({"message": f"Fridge ingredient has been updated."})
    else:
        return jsonify({"error": f"Failed to update fridge ingredient."})


@app.route('/delete/<stock_store>/<item_name>', methods=['DELETE'])
def delete_item_from_stock(stock_store, item_name):
    try:
        delete_item(stock_store, item_name)
        return jsonify({"message": f"{item_name} successfully deleted from {stock_store}."})
    except:
        return jsonify({"error": f"Failed to delete {item_name} from {stock_store}."})


if __name__ == '__main__':
    app.run(debug=True)
    
    
    
# Anna's test code

@app.route('/fridge')
def index():
    # Connect to MySQL
    connection = mysql.connector.connect(**_connect_to_db)
    cursor = connection.cursor()

    # Execute a query to fetch data from your table
    cursor.execute('SELECT IngredientName FROM Fridge')
    data = cursor.fetchall()

    # Close the connection
    cursor.close()
    connection.close()

    # Read the HTML file
    with open('front-end/fridge.html', 'r') as file:
        html_content = file.read()

    # Inject the data into the HTML content
    data_html = '<ul>'
    for row in data:
        data_html += f'<li>{row}</li>'
    data_html += '</ul>'

    html_content = html_content.replace('<!-- placeholder -->', data_html)

    # Send the modified content as the response
    return send_file(html_content, mimetype='text/html')

if __name__ == '__main__':
    app.run(debug=True)