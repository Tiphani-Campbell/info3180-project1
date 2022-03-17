"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""
import os
import numpy
from app import app, db
from flask import render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from .forms import PropertyForm
from .models import Property



###
# Routing for your application.
###

"""Display value enterd in the format $XXX,XXX"""
@app.template_filter()
def currencyFormat(x):
    if "," in x:
        a=[y for y in x if y != ","]
        y=''.join(a)
        b=numpy.float_(y)
        return "${:,.0f}".format(b)
    else:
        x = float(x)
        return "${:,.0f}".format(x)

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Tiphani Campbell")

@app.route('/properties')
def view_properties():
    """Render the property listings homepage. """
    properties = Property.query.all()
    return render_template('properties.html', properties=properties)

@app.route('/properties/create', methods=['GET','POST'])
def create():
    """Render website's property creation page"""
    propform = PropertyForm()
    if request.method == 'POST':
        if propform.validate_on_submit():
            title = propform.title.data
            description = propform.description.data
            rooms = propform.num_rooms.data
            bathrooms = propform.num_bath.data
            price = propform.price.data
            propertytype = propform.prop_type.data
            location = propform.location.data
            photo = propform.photo.data
            flash('Saved successfully!', 'success')
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            

            property = Property(title=title, no_of_bedrooms=rooms, no_of_bathrooms=bathrooms, location=location, price=price, description=description, type=propertytype, photo="uploads/"+filename)
            db.session.add(property)
            db.session.commit()
            

            return redirect(url_for('view_properties'))
        else:   
            flash_errors(propform)
    return render_template('newproperty.html', form=propform)

@app.route('/properties/<propertyid>')
def loadproperty(propertyid):
    """Render an individual property page"""
    property = Property.query.filter_by(id=int(propertyid)).first()
    return render_template('loadproperty.html', property=property)
###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
