# FUNCTIONS GO IN THIS FILE

import mysql.connector
from config import USER, PASSWORD, HOST


class DbConnectionError(Exception):
    pass


def connect_to_db(db_name):
    try:
        conn = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            auth_plugin='mysql_native_password',
            database=db_name
    )
        print('Connected to Database: {}'.format(db_name))
        return conn
    except mysql.connector.Error as err:
        raise DbConnectionError(f'Failed to connect: {err}')


# FUNCTION TO ADD ITEM TO STOCK



# FUNCTION TO DELETE ITEM FROM STOCK



# LAUREN-A FUNCTION TO UPDATE ITEM IN STOCK
def update_inventory():
    try:
        db_name = 'smart_pantry'
        conn = connect_to_db(db_name)
        cur = conn.cursor()

        # Retrieve input from user
        storage_update = input("Which stock store would you like to update? \n - Fridge \n - Freezer \n - Pantry \n : ").lower()
        column_update = input("Which column of data would you like to update? \n - Ingredient name \n - Type of ingredient \n - Quantity \n - Sell by date \n : ").lower()
        data_id = int(input("Please enter the ingredient ID: "))
        new_value = input(f"Enter the new value for the {column_update}: ")

        # Define SQL update query
        update_query = ""

        if column_update == 'ingredient name':
            update_query = f"UPDATE {storage_update} SET IngredientName = %s WHERE ID = %s"
        elif column_update == 'quantity':
            new_value = int(new_value)
            update_query = f"UPDATE {storage_update} SET Quantity = %s WHERE ID = %s"
        elif column_update == 'type of ingredient':
            update_query = f"UPDATE {storage_update} SET TypeOfIngredient = %s WHERE ID = %s"
        elif column_update == 'sell by date':
            new_value = int(new_value)
            update_query = f"UPDATE {storage_update} SET SellByDate = %s WHERE ID = %s"
        else:
            print("Invalid input.")

        # Execute the SQL update query
        cur.execute(update_query, (new_value, data_id))

        # Commit the changes to the database
        conn.commit()
        print("Record Updated successfully ")

        # Close the cursor and database connection
        cur.close()
        conn.close()

    except Exception as e:
        raise DbConnectionError("Failed to update inventory: {e}")


if __name__ == '__main__':
    update_inventory()
