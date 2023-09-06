from flask import Blueprint, render_template


# instantiate Blueprint object
site = Blueprint('site', __name__, template_folder='site_templates')



# first route
@site.route('/')
def car_shop():
    return render_template('car_shop.html') # displays the car shop page
