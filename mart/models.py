from mart import *
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from datetime import datetime


@login.user_loader
def load_user(id):
    return Users.query.get(int(id))


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    username = db.Column(db.String(60), nullable=False, unique=True)
    email = db.Column(db.String(60), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)

    def get_reset_token(self, expire_time=1800):
        s = Serializer(app.config['SECRET_KEY'], expire_time)
        token = s.dumps({'user_id': self.id}).decode('utf-8')
        return token

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return Users.query.get(user_id)

    def __repr__(self):
        return f"User '{self.username}', '{self.email}', '{self.password}', '{self.username}'"


class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    image_file = db.Column(db.String(125), default='default.jpg')
    create_at = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return f"(Category('{self.name}', '{self.image_file}', '{self.create_at}'))"


class SubCategories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    image_file = db.Column(db.String(125), default='default.jpg')
    create_at = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return f"(SubCategories('{self.name}', '{self.image_file}', '{self.create_at}'))"
