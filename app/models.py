from app import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.name)


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)

    # Serialize function for JSON request
    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    def __repr__(self):
        return '<Category {}>'.format(self.name)


class Book(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    author = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship(Category)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship(User)

    # Serialize function for JSON request
    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author,
            'description': self.description,
            'category': self.category.name
        }

    def __repr__(self):
        return '<Item {}>'.format(self.name)
