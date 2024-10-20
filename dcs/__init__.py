import os

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from dcs.models import BaseModel

db = SQLAlchemy(model_class=BaseModel)


def handle_not_found(e):
    return (
        render_template(
            "error.jinja",
            title="404 Not Found",
            description="The page could not be found",
        ),
        404,
    )


def create_app():
    app = Flask(__name__, static_url_path="/")

    if os.environ["FLASK_ENV"] == "development":
        app.config.from_object("dcs.config.development.DevelopmentConfig")
    else:
        app.config.from_object("dcs.config.production.ProductionConfig")

    db.init_app(app)

    from .blueprints import home

    app.register_blueprint(home.bp)
    app.register_error_handler(404, handle_not_found)

    from .models import comment

    with app.app_context():
        db.create_all()

    return app
