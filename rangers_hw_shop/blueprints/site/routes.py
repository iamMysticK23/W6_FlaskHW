from flask import Blueprint, render_template, request, flash, redirect

# internal imports
from rangers_hw_shop.models import Product, db, product_schema, products_schema
from rangers_hw_shop.forms import ProductForm


# instantiate Blueprint object
site = Blueprint('site', __name__, template_folder='site_templates')



# first route
@site.route('/')
def car_shop():


    shop = Product.query.all()

    return render_template('car_shop.html', shop=shop) # displays the car shop page


# create the CREATE route
@site.route('/shop/create', methods= ['GET', 'POST'])
def create():

    createform = ProductForm()

    if request.method == 'POST' and createform.validate_on_submit():

        try:
            name = createform.name.data
            desc = createform.description.data
            image = createform.image.data
            price = createform.price.data
            quantity = createform.quantity.data

            shop = Product(name, price, quantity, image, desc)

            db.session.add(shop)
            db.session.commit()

            flash(f" {name} added successfully.", category='success')
            return redirect('/')

        except:
            flash("Process could not be completed. Please try again.")
            return redirect('/shop/create')
        
    return render_template('create.html', form=createform)


# create the UPDATE route
@site.route('/shop/update/<id>', methods= ['GET', 'POST'])
def update(id):

    updateform = ProductForm()
    product = Product.query.get(id)

    if request.method == 'POST' and updateform.validate_on_submit():
        try:
            product.name = updateform.name.data
            product.description = updateform.description.data
            product.set_image(updateform.image.data, updateform.name.data)
            product.price = updateform.price.data
            product.quantity = updateform.quantity.data


            db.session.commit()

            flash(f" {product.name} updated successfully.", category='success')
            return redirect('/')

        except:
            flash("Process could not be completed. Please try again.")
            return redirect('/shop/update')
        
    return render_template('update.html', form=updateform, product=product)

@site.route('/shop/delete/<id>')
def delete(id):

    product = Product.query.get(id)

    db.session.delete(product)
    db.session.commit()

    return redirect('/')


