from flask import Flask
app = Flask(__name__)


# Restaurants
@app.route('/')
@app.route('/restaurant/')
def showRestaurant():
    return "This is restaurant Menu"


@app.route('/restaurant/new/')
def newRestaurant():
    return "Add new restaurant"


@app.route('/restaurant/edit/')
def editRestaurant():
    return "Edit an existing restaurant"


@app.route('/restaurant/delete/')
def deleteRestaurant():
    return "Delete a restaurant"


# Menus
@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu/')
def showMenu(restaurant_id):
    return "this page will be for visitin restaurant menus"


@app.route('/restaurant/<int:restaurant_id>/menu/new/')
def newMenuItem(restaurant_id):
    return "this will be used to create manu items"


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
    return "this will be used to edit manu items"


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):
    return "this will be used to delete manu items"


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
