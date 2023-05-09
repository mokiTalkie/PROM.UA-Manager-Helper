from flask import Flask
from routes.additional import additional
from routes.tools import tools


def create_app() -> Flask:
    app = Flask(__name__, template_folder='templates')
    app.register_blueprint(blueprint=additional)
    app.register_blueprint(blueprint=tools)

    return app


app = create_app()