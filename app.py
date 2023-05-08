from flask import Flask
from routes.additional import additional
from routes.tools import tools

app = Flask(__name__, template_folder='templates')
app.register_blueprint(blueprint=additional)
app.register_blueprint(blueprint=tools)


if __name__ == '__main__':
    app.run(
        debug=True
    )