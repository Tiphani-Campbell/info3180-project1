from . import db

class Property(db.Model):
    __tablename__ = "properties"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    no_of_bedrooms = db.Column(db.Integer)
    no_of_bathrooms = db.Column(db.Integer)
    location = db.Column(db.String(100))
    price = db.Column(db.String(30))
    description = db.Column(db.Text)
    proptype = db.Column(db.String(10))
    photo = db.Column(db.String(255))

    def __init__(self, title, description, no_of_bedrooms, no_of_bathrooms, location, price, type, photo):
        self.title = title
        self.no_of_bedrooms = no_of_bedrooms
        self.no_of_bathrooms = no_of_bathrooms
        self.location = location
        self.price = price
        self.description = description
        self.proptype = type
        self.photo = photo
    
    def __repr__(self):
        return '<Title %r>' % (self.title)

    