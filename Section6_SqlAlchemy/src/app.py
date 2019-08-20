from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from Section6_SqlAlchemy.src.security import authenticate, identity
from Section6_SqlAlchemy.src.resources.user import UserRegister
from Section6_SqlAlchemy.src.resources.item import Item, ItemList
from Section6_SqlAlchemy.src.resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # turn of Flask-SQLAlchemy modification tracker and leaves SQLAlchemy tracker
app.secret_key = 'artie'
api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()


jwt = JWT(app, authenticate, identity)  # creates new endpoint: /auth

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == '__main__':
    from Section6_SqlAlchemy.src.db import db

    db.init_app(app)
    app.run(debug=True)
