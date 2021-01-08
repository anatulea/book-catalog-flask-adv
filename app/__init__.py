# app/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_type):
    app = Flask()

    # '/Users/anatulea/PycharmProjects/book_catalog_flask_adv/config/dev.py'
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    app.config.from_pyfile(configuration)

    db.init_app(app)  # initialize database

    from app.catalog import main  # import blueprint
    app.register_blueprint(main)  # register blueprint

    return app
